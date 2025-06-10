from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple
from competitor import Competitor
from arena import Arena

@dataclass
class MatchResult:
    winner: str
    loser: str
    winner_ability: float
    loser_ability: float

@dataclass
class Simulation:
    competitors: List[Competitor]
    arena: Arena = field(default_factory=Arena)

    def run_round_robin(self, rounds: int = 1) -> List[MatchResult]:
        """Run a round-robin tournament among competitors."""
        results: List[MatchResult] = []
        for _ in range(rounds):
            for i, a in enumerate(self.competitors):
                for b in self.competitors[i+1:]:
                    winner, loser, w_abil, l_abil = self.arena.compete(a, b)
                    results.append(MatchResult(winner.name or str(id(winner)),
                                                loser.name or str(id(loser)),
                                                w_abil, l_abil))
        return results
