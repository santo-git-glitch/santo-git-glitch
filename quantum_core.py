import os, urllib.request, json
from datetime import datetime, timezone

USER = "santo-git-glitch"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def fetch_data():
    h = {"User-Agent": "GearHeart-Quantum-SMC"}
    if TOKEN: h["Authorization"] = f"token {TOKEN}"
    try:
        u = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/users/{USER}", headers=h), timeout=10).read().decode())
        rl = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/users/{USER}/repos?per_page=100", headers=h), timeout=10).read().decode())
        st = sum(r.get("stargazers_count", 0) for r in rl if isinstance(r, dict))
        fk = sum(r.get("forks_count", 0) for r in rl if isinstance(r, dict))
        return {"repos": u.get("public_repos", 1), "followers": u.get("followers", 0), "stars": st, "forks": fk}
    except Exception:
        return {"repos": 14, "followers": 8, "stars": 25, "forks": 6}
def build_matrix(d):
    rp, st, fk, fl = d["repos"], d["stars"], d["forks"], d["followers"]
    bio_km = round(1480.5 + (rp * 142.8) + (st * 89.4), 1)
    smc_load = min(99.99, round(94.2 + (rp * 0.25) + (fk * 0.4), 2))
    q_ops = (rp * 12) + (st * 19) + (fk * 9)
    ts = datetime.now(timezone.utc).strftime("%Y.%m.%d // %H:%M UTC")
    svg = f'''<svg width="900" height="480" viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="void" cx="50%" cy="50%" r="75%"><stop offset="0%" stop-color="#0b192c"/><stop offset="65%" stop-color="#040812"/><stop offset="100%" stop-color="#010205"/></radialGradient>
    <linearGradient id="holo" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#00f3ff"/><stop offset="50%" stop-color="#9d00ff"/><stop offset="100%" stop-color="#ffbe0b"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="900" height="480" rx="16" fill="url(#void)" stroke="#1e293b" stroke-width="2"/>
  <path d="M15 60V15h55M885 60V15h-55M15 420v45h55M885 420v45h-55" fill="none" stroke="#00f3ff" stroke-width="2.5" filter="url(#glow)"/>
  <text x="35" y="42" fill="#00f3ff" font-family="monospace" font-size="14" font-weight="bold" letter-spacing="2">HOLOGRAPHIC TRAVELER CONSOLE // SMC-BIO ENGINE v9.8</text>
  <text x="35" y="62" fill="#94a3b8" font-family="monospace" font-size="11">TRAVELER: {USER.upper()} | DIMENSIONAL SYNC: {ts} | GEAR-HEART: LOCKED</text>
  <g transform="translate(450, 225)">
    <circle r="115" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <circle r="92" fill="none" stroke="#ffbe0b" stroke-width="3" stroke-dasharray="14 8" opacity="0.75">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="18s" repeatCount="indefinite"/>
    </circle>
    <circle r="68" fill="none" stroke="#00f3ff" stroke-width="2.5" stroke-dasharray="8 6" opacity="0.85">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>
    </circle>
    <ellipse rx="110" ry="34" fill="none" stroke="#9d00ff" stroke-width="1.5">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>
    </ellipse>
    <circle r="16" fill="#ff0055" filter="url(#glow)">
      <animate attributeName="r" values="12;19;12;16;12" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <circle r="6" fill="#ffffff"/>
  </g>
  <rect x="35" y="90" width="230" height="58" rx="6" fill="#091322" stroke="#00f3ff"/><text x="48" y="112" fill="#94a3b8" font-family="monospace" font-size="10">MASTER BIO-KILOMETER</text><text x="48" y="135" fill="#00f3ff" font-family="monospace" font-size="18" font-weight="bold">{bio_km} KM/CYC</text>
  <rect x="35" y="165" width="230" height="58" rx="6" fill="#091322" stroke="#9d00ff"/><text x="48" y="187" fill="#94a3b8" font-family="monospace" font-size="10">SMC ENGINE COHERENCE</text><text x="48" y="210" fill="#c084fc" font-family="monospace" font-size="18" font-weight="bold">{smc_load}% ACTIVE</text>
  <rect x="35" y="240" width="230" height="58" rx="6" fill="#091322" stroke="#ffbe0b"/><text x="48" y="262" fill="#94a3b8" font-family="monospace" font-size="10">GEAR-HEART TORQUE</text><text x="48" y="285" fill="#ffbe0b" font-family="monospace" font-size="18" font-weight="bold">{q_ops} Q-RPM</text>
  <rect x="635" y="90" width="230" height="58" rx="6" fill="#091322" stroke="#00f3ff"/><text x="648" y="112" fill="#94a3b8" font-family="monospace" font-size="10">QUANTUM NODES</text><text x="648" y="135" fill="#00f3ff" font-family="monospace" font-size="18" font-weight="bold">{rp} SECTORS</text>
  <rect x="635" y="165" width="230" height="58" rx="6" fill="#091322" stroke="#ff0055"/><text x="648" y="187" fill="#94a3b8" font-family="monospace" font-size="10">PHOTON RESONANCE</text><text x="648" y="210" fill="#ff4d8d" font-family="monospace" font-size="18" font-weight="bold">{st} STARS ★</text>
  <rect x="635" y="240" width="230" height="58" rx="6" fill="#091322" stroke="#10b981"/><text x="648" y="262" fill="#94a3b8" font-family="monospace" font-size="10">TIMELINE BRANCHES</text><text x="648" y="285" fill="#34d399" font-family="monospace" font-size="18" font-weight="bold">{fk} FORKS | {fl} LINK</text>
  <rect x="35" y="365" width="830" height="82" rx="8" fill="#050b14" stroke="#334155"/>
  <line x1="35" y1="388" x2="865" y2="388" stroke="#1e293b"/>
  <text x="50" y="381" fill="#ffbe0b" font-family="monospace" font-size="10" font-weight="bold">[HOLOGRAPHIC TRAVELER CONSOLE // LIVE TELEMETRY STREAM]</text>
  <text x="50" y="407" fill="#00f3ff" font-family="monospace" font-size="11">&gt; [SMC_CORE] Bio-Synthesizer calibrated at {bio_km} km neural span | Zero Decoherence</text>
  <text x="50" y="424" fill="#c084fc" font-family="monospace" font-size="11">&gt; [GEAR_HEART] Mechanical-Quantum pulse synchronized with {rp} active repositories</text>
  <text x="50" y="441" fill="#34d399" font-family="monospace" font-size="11">&gt; [NAV_MATRIX] Multiverse trajectory locked // Ready for next code synthesis...</text>
</svg>'''
    with open("quantum_matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    build_matrix(fetch_data())
    print("Gear-Heart & SMC Bio-Engine SVG generated!")
