from competitor import Competitor
from simulation import Simulation
from inference import infer_parameters


def test_round_robin_and_inference():
    competitors = [
        Competitor(mu=10, sigma=2, name="A"),
        Competitor(mu=12, sigma=3, name="B"),
    ]
    sim = Simulation(competitors)
    results = sim.run_round_robin(rounds=5)
    assert len(results) == 5  # two competitors -> one match per round

    inferred = {c.name: c for c in infer_parameters(results)}
    assert set(inferred.keys()) == {"A", "B"}
    for c in competitors:
        assert inferred[c.name].sigma >= 0
