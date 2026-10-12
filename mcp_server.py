"""MCP server for Multi-Agent Debate Judge & Hallucination Arbiter."""
import sys
import json
from client import MultiAgentDebateArbiter

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "arbitrate_agent_debate",
                "description": "Scores competing agent responses by citation grounding and logical consistency",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "proposals": {"type": "array"}
                    },
                    "required": ["proposals"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "arbitrate_agent_debate":
            proposals = params.get("arguments", {}).get("proposals", [])
            res = MultiAgentDebateArbiter.arbitrate_proposals(proposals)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
