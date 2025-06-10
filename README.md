# modelNormalCompetition

This repository models a collection of competitors with normally distributed abilities.
A simple arena runs repeated competitions between competitors. After observing the
outcomes it is possible to infer the original mean (`mu`) and standard deviation
(`sigma`) for each competitor.

## Installation

Create a virtual environment (optional) and install dependencies:

```bash
pip install -r requirements.txt
```

## Running a simulation

A demo script is available in `examples/run_simulation.py`:

```bash
python examples/run_simulation.py
```

This creates a few competitors, runs a round-robin tournament and prints the
parameters inferred from the observed abilities.

## Running tests

Execute the unit tests with:

```bash
pytest
```
