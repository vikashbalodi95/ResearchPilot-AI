function Hero() {
  const metrics = [
    { label: "Research flow", value: "AI-powered" },
    { label: "Documents", value: "PDF ready" },
    { label: "Insight mode", value: "Context-first" },
  ];

  return (
    <section className="hero" id="home">
      <div className="eyebrow"><span className="eyebrow-line" /> AI research, made legible</div>

      <h1>
        Turn questions
        <br />
        <span>into clarity.</span>
      </h1>

      <p>
        Ask a sharp question. Get a considered answer shaped by context,
        synthesis, and the details that matter.
      </p>

      <div className="hero-metrics" aria-label="Product highlights">
        {metrics.map((metric) => (
          <div className="metric-pill" key={metric.label}>
            <span>{metric.label}</span>
            <strong>{metric.value}</strong>
          </div>
        ))}
      </div>

      <div className="hero-meta"><span>01 / Ask</span><span>02 / Synthesize</span><span>03 / Understand</span></div>
    </section>
  );
}

export default Hero;