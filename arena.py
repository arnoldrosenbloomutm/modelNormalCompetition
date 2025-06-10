from typing import Tuple
from competitor import Competitor

class Arena:
    """Runs competitions between competitors."""

    @staticmethod
    def compete(a: Competitor, b: Competitor) -> Tuple[Competitor, Competitor, float, float]:
        """Run a single competition and return winner/loser and their abilities."""
        ability_a = a.sample_ability()
        ability_b = b.sample_ability()

        if ability_a > ability_b:
            return a, b, ability_a, ability_b
        else:
            return b, a, ability_b, ability_a
