# classic_monty_hall.py — Monty Hall Simulation for 3-Door Setup

import random
import matplotlib.pyplot as plt
import numpy as np


def monty_hall_simulation(num_trials: int, switch: bool) -> float:
    
    """
    Simulates the classic Monty Hall problem.

    Args:
        num_trials (int): Number of trials to simulate.
        switch (bool): Whether the player switches doors after the host reveals a goat.

    Returns:
        win_rate (float): Proportion of wins.
    """

    wins = 0
    for _ in range(num_trials):
        doors = [0, 1, 2]
        car_location = random.choice(doors)
        initial_choice = random.choice(doors)

        # Host reveals a goat door
        goat_doors = [d for d in doors if d != initial_choice and d != car_location]
        door_opened_by_host = random.choice(goat_doors)

        # Player's final choice
        if switch:
            final_choice = [d for d in doors if d != initial_choice and d != door_opened_by_host][0]
        else:
            final_choice = initial_choice

        if final_choice == car_location:
            wins += 1

    win_rate = wins / num_trials
    return win_rate


def run_simulations() -> tuple[list[int], list[float], list[float]]:
    
    """
    Runs simulations for various trial counts and both strategies (switch vs no switch).

    Returns:
        tuple: Trial counts, win rates without switching, and win rates with switching.
    """

    trial_counts = [10, 100, 500, 1000, 5000, 10000, 50000, 100000]
    no_switch_win_rates = []
    switch_win_rates = []

    for count in trial_counts:
        no_switch_win_rates.append(monty_hall_simulation(num_trials=count, switch=False))
        switch_win_rates.append(monty_hall_simulation(num_trials=count, switch=True))

    return trial_counts, no_switch_win_rates, switch_win_rates


def plot_results(trial_counts: list[int], no_switch_win_rates: list[float], switch_win_rates: list[float]) -> None:
    
    """
    Plots and saves the results of the Monty Hall simulations.

    Args:
        trial_counts (list[int]): Number of trials used in each simulation run.
        no_switch_win_rates (list[float]): Win rates without switching.
        switch_win_rates (list[float]): Win rates with switching.
    """

    plt.figure(figsize=(10, 6))
    plt.plot(trial_counts, no_switch_win_rates, label='No Switch Strategy', marker='o')
    plt.plot(trial_counts, switch_win_rates, label='Switch Strategy', marker='o')
    plt.axhline(1/3, color='blue', linestyle='--', label='Expected (No Switch)')
    plt.axhline(2/3, color='orange', linestyle='--', label='Expected (Switch)')
    plt.xscale('log')
    plt.xlabel('Number of Simulations (log scale)')
    plt.ylabel('Winning Probability')
    plt.title('Monty Hall Problem: No Switch vs Switch Strategy')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/classic_win_rates.png")
    plt.show()


if __name__ == "__main__":
    trial_counts, no_switch_win_rates, switch_win_rates = run_simulations()
    plot_results(trial_counts, no_switch_win_rates, switch_win_rates)
