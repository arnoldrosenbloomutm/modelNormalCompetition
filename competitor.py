from dataclasses import dataclass
import numpy as np

@dataclass
class Competitor:
    """Represents a competitor with a normal ability distribution."""
    mu: float
    sigma: float
    name: str | None = None

    def sample_ability(self) -> float:
        """Draw a random ability for a single competition."""
        return float(np.random.normal(self.mu, self.sigma))
