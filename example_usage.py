"""Example usage for Multi-Agent Debate Judge & Hallucination Arbiter."""
from client import MultiAgentDebateArbiter

if __name__ == "__main__":
    proposals = [
        {"agent_id": "solver_alpha", "answer": "Detailed analysis with verified sources.", "citations": ["doc1", "doc2"], "self_contradictions": 0},
        {"agent_id": "solver_beta", "answer": "Short guess.", "citations": [], "self_contradictions": 1}
    ]
    res = MultiAgentDebateArbiter.arbitrate_proposals(proposals)
    print("Winning Agent:", res["winning_agent"], "Score:", res["winning_score"])
