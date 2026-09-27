import { useEffect, useState } from "react";
import "./index.css";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import ResearchInput from "./components/ResearchInput";
import ResearchResult from "./components/ResearchResult";
import Footer from "./components/Footer";

const API_URL = import.meta.env.VITE_API_URL || "";

async function requestJson(path, options = {}) {
  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 45_000);

  try {
    const response = await fetch(`${API_URL}${path}`, {
      ...options,
      signal: controller.signal,
    });
    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      throw new Error(data.detail || "The request could not be completed.");
    }

    return data;
  } catch (requestError) {
    if (requestError.name === "AbortError") {
      throw new Error("The request took too long. Please try again.");
    }
    throw requestError;
  } finally {
    window.clearTimeout(timeout);
  }
}

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [status, setStatus] = useState("idle");
  const [error, setError] = useState("");
  const [history, setHistory] = useState([]);
  const [uploadedFile, setUploadedFile] = useState("");
  const [uploadStatus, setUploadStatus] = useState("idle");
  const [backendStatus, setBackendStatus] = useState("checking");

  useEffect(() => {
    requestJson("/health")
      .then(() => setBackendStatus("ready"))
      .catch(() => setBackendStatus("offline"));
  }, []);

  const runResearch = async (prompt) => {
    const trimmedPrompt = prompt.trim();

    if (trimmedPrompt.length < 5) {
      setError("Add a little more detail so the research has useful direction.");
      return;
    }

    setQuery(trimmedPrompt);
    setStatus("loading");
    setError("");

    try {
      const data = await requestJson("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: trimmedPrompt }),
      });

      setResult(data.response);
      setBackendStatus("ready");
      setStatus("success");
      setHistory((currentHistory) => [trimmedPrompt, ...currentHistory.filter((item) => item !== trimmedPrompt)].slice(0, 3));
    } catch (requestError) {
      setStatus("error");
      setBackendStatus("offline");
      setError(requestError.message || "Unable to connect to ResearchPilot.");
    }
  };

  const uploadPdf = async (file) => {
    if (!file) return;

    if (file.type !== "application/pdf" && !file.name.toLowerCase().endsWith(".pdf")) {
      setUploadStatus("error");
      setError("Please choose a PDF file.");
      return;
    }

    if (file.size > 15 * 1024 * 1024) {
      setUploadStatus("error");
      setError("That PDF is larger than 15 MB. Please choose a smaller file.");
      return;
    }

    setUploadStatus("loading");
    setUploadedFile("");

    try {
      const formData = new FormData();
      formData.append("file", file);
      const data = await requestJson("/upload", { method: "POST", body: formData });
      setUploadedFile(data.filename || file.name);
      setUploadStatus("success");
      setError("");
      setBackendStatus("ready");
    } catch (uploadError) {
      setUploadStatus("error");
      setError(uploadError.message || "PDF upload failed.");
      setBackendStatus("offline");
    }
  };

  return (
    <div className="app">
      <Navbar backendStatus={backendStatus} onNewResearch={() => document.getElementById("research")?.scrollIntoView({ behavior: "smooth" })} />

      <main>
        <Hero />
        <div className="workspace-grid">
          <ResearchInput query={query} onQueryChange={setQuery} onResearch={runResearch} status={status} error={error} history={history} onUpload={uploadPdf} uploadedFile={uploadedFile} uploadStatus={uploadStatus} />
          <ResearchResult query={query} result={result} status={status} error={error} onRegenerate={() => runResearch(query)} />
        </div>
      </main>

      <Footer />
    </div>
  );
}

export default App;