import { useRef } from "react";

const prompts = [
  "How is generative AI changing software development?",
  "What are the strongest arguments for nuclear energy?",
  "Explain the current state of solid-state batteries.",
];

function ResearchInput({ query, onQueryChange, onResearch, status, error, history, onUpload, uploadedFile, uploadStatus }) {
  const isLoading = status === "loading";
  const isUploading = uploadStatus === "loading";
  const inputRef = useRef(null);

  const handleKeyDown = (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
      event.preventDefault();
      onResearch(query);
    }
  };

  const choosePrompt = (prompt) => {
    onQueryChange(prompt);
    inputRef.current?.focus();
  };

  return (
    <section className="research-section" id="research">
      <div className="research-box">
        <div className="panel-kicker"><span>RESEARCH BRIEF</span><span className="panel-number">01</span></div>

        <div className="input-header">
          <div>
            <h2>What are you curious about?</h2>
            <p>
              Write a question with enough context for a useful answer.
            </p>
          </div>

          {query && (
            <button
              className="clear-button"
              onClick={() => onQueryChange("")}
              type="button"
            >
              Reset
            </button>
          )}
        </div>

        <textarea
          value={query}
          ref={inputRef}
          onChange={(e) => onQueryChange(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="e.g. What should product teams know about open-source AI models in 2026?"
          rows="6"
          maxLength="1000"
          aria-label="Research question"
        />

        <div className="input-footer">
          <span>
            {query.length} / 1000 characters
          </span>

          <button
            className="generate-button"
            onClick={() => onResearch(query)}
            disabled={!query.trim() || isLoading}
            type="button"
          >
            {isLoading ? "Thinking..." : "Run research"}
            <span>{isLoading ? "..." : "->"}</span>
          </button>
        </div>

        <div className="upload-row">
          <label className={`upload-button ${isUploading ? "uploading" : ""}`} htmlFor="pdf-upload">
            <span className="upload-icon">+</span>
            {isUploading ? "Uploading PDF..." : "Attach a PDF"}
          </label>
          <input id="pdf-upload" type="file" accept="application/pdf,.pdf" disabled={isUploading} onChange={(event) => onUpload(event.target.files?.[0])} />
          {uploadedFile && <span className="upload-success">Attached: {uploadedFile}</span>}
        </div>

        {error && <p className="form-error" role="alert">{error}</p>}

        <div className="prompt-list"><span>Try a prompt</span>{prompts.map((prompt) => <button key={prompt} type="button" onClick={() => choosePrompt(prompt)}>{prompt}</button>)}</div>
        {history.length > 0 && <div className="history-list"><span>Recent</span>{history.map((item) => <button key={item} type="button" onClick={() => choosePrompt(item)}>{item}</button>)}</div>}
      </div>
    </section>
  );
}

export default ResearchInput;