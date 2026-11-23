import os, urllib.request, json
from datetime import datetime

USERNAME = "santo-git-glitch"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get_github_data():
    headers = {"User-Agent": "Quantum-AI-Core"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
    try:
        req = urllib.request.Request(f"https://api.github.com/users/{USERNAME}", headers=headers)
        u = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
        req_r = urllib.request.Request(f"https://api.github.com/users/{USERNAME}/repos?per_page=100", headers=headers)
        r_list = json.loads(urllib.request.urlopen(req_r, timeout=10).read().decode())
        stars = sum(r.get("stargazers_count", 0) for r in r_list if isinstance(r, dict))
        forks = sum(r.get("forks_count", 0) for r in r_list if isinstance(r, dict))
        return {"repos": u.get("public_repos", 1), "followers": u.get("followers", 0), "stars": stars, "forks": forks}
    except Exception:
        return {"repos": 12, "followers": 5, "stars": 18, "forks": 4}
def generate_svg(data):
    repos, stars, forks, followers = data["repos"], data["stars"], data["forks"], data["followers"]
    coherence = min(99.99, round(92.5 + (repos * 0.35) + (stars * 0.2), 2))
    entanglement = (repos * 4) + (stars * 7) + (forks * 3)
    theta, phi = round((repos * 17) % 180, 1), round((stars * 29 + followers * 13) % 360, 1)
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    svg = f'''<svg width="850" height="380" viewBox="0 0 850 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%"><stop offset="0%" stop-color="#0d1b2a"/><stop offset="100%" stop-color="#020408"/></radialGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="850" height="380" rx="14" fill="url(#bg)" stroke="#1e293b" stroke-width="2"/>
  <path d="M20 50V20h40M830 50V20h-40M20 330v30h40M830 330v30h-40" fill="none" stroke="#00f3ff" stroke-width="2" filter="url(#glow)"/>
  <text x="40" y="45" fill="#00f3ff" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="2">QUANTUM-AI NEURAL CORE // {USERNAME.upper()}</text>
  <text x="40" y="65" fill="#94a3b8" font-family="monospace" font-size="11">STATE: |ψ⟩ = α|0⟩ + β|1⟩ | θ={theta}° φ={phi}° | SYNC: {ts}</text>
  <g transform="translate(425, 200)">
    <circle r="95" fill="none" stroke="#1e293b" stroke-dasharray="4 4"/>
    <ellipse rx="95" ry="32" fill="none" stroke="#00f3ff" stroke-width="1.5"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/></ellipse>
    <ellipse rx="32" ry="95" fill="none" stroke="#9d00ff" stroke-width="1.5"><animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="10s" repeatCount="indefinite"/></ellipse>
    <circle r="10" fill="#00f3ff" filter="url(#glow)"><animate attributeName="r" values="8;13;8" dur="3s" repeatCount="indefinite"/></circle>
    <text x="-8" y="-110" fill="#00f3ff" font-family="monospace" font-size="11">|0⟩</text>
    <text x="-8" y="120" fill="#9d00ff" font-family="monospace" font-size="11">|1⟩</text>
  </g>
  <rect x="40" y="105" width="190" height="50" rx="6" fill="#0f172a" stroke="#00f3ff"/><text x="52" y="125" fill="#94a3b8" font-family="monospace" font-size="10">QUBIT COHERENCE</text><text x="52" y="145" fill="#00f3ff" font-family="monospace" font-size="16" font-weight="bold">{coherence}%</text>
  <rect x="40" y="175" width="190" height="50" rx="6" fill="#0f172a" stroke="#9d00ff"/><text x="52" y="195" fill="#94a3b8" font-family="monospace" font-size="10">ENTANGLED NODES</text><text x="52" y="215" fill="#c084fc" font-family="monospace" font-size="16" font-weight="bold">{repos} REPOS</text>
  <rect x="40" y="245" width="190" height="50" rx="6" fill="#0f172a" stroke="#ffbe0b"/><text x="52" y="265" fill="#94a3b8" font-family="monospace" font-size="10">SYNAPSE WEIGHT</text><text x="52" y="285" fill="#ffbe0b" font-family="monospace" font-size="16" font-weight="bold">{entanglement} Q-OPS</text>
  <rect x="620" y="105" width="190" height="50" rx="6" fill="#0f172a" stroke="#00f3ff"/><text x="632" y="125" fill="#94a3b8" font-family="monospace" font-size="10">PHOTON STARS</text><text x="632" y="145" fill="#00f3ff" font-family="monospace" font-size="16" font-weight="bold">{stars} ★</text>
  <rect x="620" y="175" width="190" height="50" rx="6" fill="#0f172a" stroke="#9d00ff"/><text x="632" y="195" fill="#94a3b8" font-family="monospace" font-size="10">QUANTUM FORKS</text><text x="632" y="215" fill="#c084fc" font-family="monospace" font-size="16" font-weight="bold">{forks} BRANCHES</text>
  <rect x="620" y="245" width="190" height="50" rx="6" fill="#0f172a" stroke="#10b981"/><text x="632" y="265" fill="#94a3b8" font-family="monospace" font-size="10">OBSERVERS</text><text x="632" y="285" fill="#34d399" font-family="monospace" font-size="16" font-weight="bold">{followers} LINKED</text>
  <text x="40" y="348" fill="#64748b" font-family="monospace" font-size="10">ARCHITECTURE: LINUX // PYTHON // AI-AUTOMATION // ZERO-DECOHERENCE</text>
</svg>'''
    with open("quantum_matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_svg(get_github_data())
