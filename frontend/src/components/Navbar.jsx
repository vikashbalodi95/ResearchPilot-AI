function Navbar({ backendStatus, onNewResearch }) {
  const statusLabel = { checking: "Checking connection", ready: "AI workspace ready", offline: "Backend offline" }[backendStatus];

  return (
    <nav className="navbar">
      <a className="logo" href="#home" aria-label="ResearchPilot home"><span className="logo-mark">R</span><span>Research<strong>Pilot</strong></span></a>

      <div className={`nav-status nav-status-${backendStatus}`}><span className="status-dot" /><span>{statusLabel}</span></div>

      <div className="nav-links">
        <a href="#research">Research</a>
        <button type="button" onClick={onNewResearch}>New research <span>+</span></button>
      </div>
    </nav>
  );
}

export default Navbar;