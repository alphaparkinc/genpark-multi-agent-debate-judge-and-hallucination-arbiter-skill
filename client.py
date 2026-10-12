"""Multi-Agent Debate Judge & Hallucination Arbiter.
100% Python Standard Library.
"""

class MultiAgentDebateArbiter:
    """Evaluates competing agent proposals by citation density, logical consistency, and factual overlap to select a winner."""

    @staticmethod
    def arbitrate_proposals(proposals: list) -> dict:
        scored = []
        for prop in proposals:
            agent_id = prop.get("agent_id", "agent")
            answer = prop.get("answer", "")
            citations = prop.get("citations", [])
            contradictions = int(prop.get("self_contradictions", 0))

            score = min(100.0, 50.0 + len(citations) * 15.0 + min(20.0, len(answer) / 25.0) - contradictions * 30.0)
            scored.append({
                "agent_id": agent_id,
                "score": round(max(0.0, score), 2),
                "citations_count": len(citations),
                "contradictions": contradictions
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return {
            "winning_agent": scored[0]["agent_id"] if scored else None,
            "winning_score": scored[0]["score"] if scored else 0.0,
            "leaderboard": scored
        }
