import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from competitor import Competitor
from simulation import Simulation
from inference import infer_parameters


def main():
    competitors = [
        Competitor(mu=20, sigma=5, name="Alice"),
        Competitor(mu=18, sigma=6, name="Bob"),
        Competitor(mu=15, sigma=4, name="Carol"),
    ]

    sim = Simulation(competitors)
    results = sim.run_round_robin(rounds=30)

    inferred = infer_parameters(results)
    print("Inferred parameters:")
    for c in inferred:
        print(f"{c.name}: mu={c.mu:.2f}, sigma={c.sigma:.2f}")


if __name__ == "__main__":
    main()
