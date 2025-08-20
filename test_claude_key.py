import os
import requests

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

print("CLAUDE_API_KEY loaded:", bool(CLAUDE_API_KEY))

if not CLAUDE_API_KEY:
    raise Exception("CLAUDE_API_KEY is missing!")

# Minimal test request
payload = {
    "model": "claude-3",
    "messages": [{"role": "user", "content": "Hello Claude, just testing API key."}],
    "max_tokens": 50
}

headers = {
    "Authorization": f"Bearer {CLAUDE_API_KEY}",
    "Content-Type": "application/json",
}

try:
    resp = requests.post(CLAUDE_API_URL, headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    print("✅ API call successful! Response snippet:")
    print(data.get("completion", data))
except requests.exceptions.HTTPError as e:
    print("❌ API call failed:", e.response.text)
