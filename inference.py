from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, List
import numpy as np
from simulation import MatchResult

@dataclass
class InferredCompetitor:
    name: str
    mu: float
    sigma: float


def infer_parameters(results: Iterable[MatchResult]) -> List[InferredCompetitor]:
    """Infer mu and sigma for each competitor from match results."""
    abilities: Dict[str, List[float]] = {}
    for r in results:
        abilities.setdefault(r.winner, []).append(r.winner_ability)
        abilities.setdefault(r.loser, []).append(r.loser_ability)

    inferred = []
    for name, samples in abilities.items():
        mu = float(np.mean(samples))
        sigma = float(np.std(samples, ddof=1)) if len(samples) > 1 else 0.0
        inferred.append(InferredCompetitor(name, mu, sigma))
    return inferred
