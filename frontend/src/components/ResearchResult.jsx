import { useState } from "react";

function ResearchResult({ query, result, status, error, onRegenerate }) {
  const lines = result ? result.split(/\n+/).filter(Boolean) : [];
  const [copied, setCopied] = useState(false);

  const copyResult = async () => {
    try {
      await navigator.clipboard.writeText(result);
      setCopied(true);
      setTimeout(() => setCopied(false), 1600);
    } catch {
      setCopied(false);
    }
  };
  return (
    <section className="results">
      <div className="result-card">

        <div className="panel-kicker"><span>FIELD NOTES</span><span className="panel-number">02</span></div>
        <div className="result-heading"><div><span className="result-badge">{status === "success" ? "Ready to read" : "Awaiting a question"}</span><h2>Research output</h2></div>{status === "success" && <span className="result-time">LIVE SYNTHESIS</span>}</div>
        {!query && status === "idle" && <div className="empty-state"><div className="empty-orbit">+</div><h3>Your thinking starts here.</h3><p>Your answer will land in this space, with room to pause, scan, and follow the thread.</p></div>}
        {status === "loading" && <div className="loading-state"><div className="loading-bar" /><h3>Following the thread...</h3><p>ResearchPilot is reading your question and shaping a response.</p></div>}
        {status === "error" && <div className="empty-state"><div className="empty-orbit error-orbit">!</div><h3>That connection missed a beat.</h3><p>{error}</p></div>}
        {status === "success" && <div className="result-content"><div className="result-actions"><button type="button" onClick={copyResult}>{copied ? "Copied" : "Copy answer"}</button><button type="button" onClick={onRegenerate}>Regenerate</button></div><p className="query-label">YOUR QUESTION</p><p className="query-text">{query}</p><div className="answer-block"><p className="query-label">SYNTHESIS</p>{lines.map((line, index) => <p key={`${line}-${index}`}>{line}</p>)}</div></div>}

      </div>
    </section>
  );
}

export default ResearchResult;