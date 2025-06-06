import pytest
from classic_monty_hall import monty_hall_simulation
from generalized_monty_hall import generalized_monty_hall_simulation  # Assuming you have this function

def test_classic_no_switch_probability():
    # Run a large number of trials without switching
    prob = monty_hall_simulation(num_trials=100000, switch=False)
    # It should be close to 1/3 within some tolerance
    assert abs(prob - 1/3) < 0.02

def test_classic_switch_probability():
    prob = monty_hall_simulation(num_trials=100000, switch=True)
    # Should be close to 2/3 within some tolerance
    assert abs(prob - 2/3) < 0.02

def test_generalized_simulation():
    # Example with 4 doors, switching should win about 3/4
    prob = generalized_monty_hall_simulation(num_trials=100000, num_doors=4, switch=True)
    assert abs(prob - 3/4) < 0.02
