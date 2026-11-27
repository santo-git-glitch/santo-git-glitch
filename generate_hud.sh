#!/usr/bin/env bash
REPOS=$(gh api "/users/santo-git-glitch/repos?per_page=100" --jq "length")
TIME=$(date -u "+%Y-%m-%d %H:%M UTC")
LEAKS=$(gh api "/search/code?q=user:santo-git-glitch+ghp_+OR+github_pat_" --jq ".total_count" 2>/dev/null || echo 0)
STATUS="SHIELD ACTIVE • 0 LEAKS"; COLOR="#00f2fe"
if [ "$LEAKS" -gt 0 ]; then STATUS="ALERT: $LEAKS TOKEN EXPOSURE"; COLOR="#ff4d4d"; fi
printf '<svg width="680" height="165" viewBox="0 0 680 165" xmlns="http://www.w3.org/2000/svg"><rect width="680" height="165" rx="14" fill="#050810" stroke="" stroke-width="1.5"/><path d="M25 82 Q 55 25, 85 82 T 145 82" fill="none" stroke="" stroke-width="2.5"><animate attributeName="d" values="M25 82 Q 55 25, 85 82 T 145 82; M25 82 Q 55 140, 85 82 T 145 82; M25 82 Q 55 25, 85 82 T 145 82" dur="3s" repeatCount="indefinite"/></path><text x="170" y="45" fill="" font-family="monospace" font-size="16" font-weight="bold">QUANTUM SENTINEL // REV-4.0</text><text x="170" y="74" fill="#e6edf3" font-family="monospace" font-size="13">SECURITY STATUS: []</text><text x="170" y="100" fill="#8b949e" font-family="monospace" font-size="12">ACTIVE NODES:  REPOS • LAST SCAN: </text><rect x="170" y="118" width="470" height="4" rx="2" fill="#161b22"/><rect x="170" y="118" width="470" height="4" rx="2" fill="" opacity="0.8"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.5s" repeatCount="indefinite"/></rect></svg>
' "$COLOR" "$COLOR" "$COLOR" "$STATUS" "$REPOS" "$TIME" "$COLOR" > quantum.svg
