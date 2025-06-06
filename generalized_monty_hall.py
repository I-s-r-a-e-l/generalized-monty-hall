# Generalized Monty Hall Simulation Project for Portfolio

import random
import matplotlib.pyplot as plt
import numpy as np


def monty_hall_simulation(num_trials, n_doors, switch):
  
    """
    Simulate the generalized Monty Hall problem over a number of trials.

    Args:
        num_trials (int): Number of simulation iterations.
        n_doors (int): Total number of doors in the game.
        switch (bool): Whether the player switches after the host reveals doors.

    Returns:
        float: Proportion of wins when using the selected strategy.
    """

    if n_doors < 3:
          raise ValueError("There must be at least 3 doors.")

    wins = 0
    doors = list(range(n_doors))

    for trial in range(num_trials):
        car_location = random.choice(doors)
        initial_choice = random.choice(doors)

        # Host reveals all doors leaving (not the car, not the initial choice)
        available_doors_to_open = [d for d in doors if d != car_location and d != initial_choice]
        doors_opened_by_host = random.sample(available_doors_to_open, n_doors - 2)

        # Player's final choice
        if switch:
            # Only one door remains unopened and unchosen
            final_choice = next(d for d in doors if d != initial_choice and d not in doors_opened_by_host)
        else:
            final_choice = initial_choice

        if final_choice == car_location:
            wins += 1

    win_rate = wins / num_trials
    return wins, win_rate

def run_simulations_for_n_doors(n_values, num_trials):

    """
    Run Monty Hall simulations across different numbers of doors.

    Args:
        n_values (list of int): List of door counts to simulate.
        num_trials (int): Number of trials per simulation.

    Returns:
        tuple: Two lists of win rates for no-switch and switch strategies.
    """

    no_switch_win_rates = []
    switch_win_rates = []
    no_switch_errors = []
    switch_errors = []

    for n in n_values:
        no_switch_wins, no_switch_rate = monty_hall_simulation(num_trials, n, switch=False)
        switch_wins, switch_rate = monty_hall_simulation(num_trials, n, switch=True)

        # Confidence intervals
        no_switch_se = np.sqrt(no_switch_rate * (1 - no_switch_rate) / num_trials)
        switch_se = np.sqrt(switch_rate * (1 - switch_rate) / num_trials)

        no_switch_win_rates.append(no_switch_rate)
        switch_win_rates.append(switch_rate)
        no_switch_errors.append(1.96 * no_switch_se)
        switch_errors.append(1.96 * switch_se)

    return no_switch_win_rates, switch_win_rates, no_switch_errors, switch_errors

def plot_generalized_results(n_values, no_switch_win_rates, switch_win_rates, no_switch_errors, switch_errors):

    """
    Plot simulation results for the generalized Monty Hall problem.

    Args:
        n_values (list of int): Number of doors used in each simulation.
        no_switch_win_rates (list of float): Win rates when not switching.
        switch_win_rates (list of float): Win rates when switching.
    """

    plt.figure(figsize=(10, 6))

    plt.errorbar(n_values, no_switch_win_rates, yerr=no_switch_errors, fmt='o-', capsize=5, label='No Switch Strategy')
    plt.errorbar(n_values, switch_win_rates, yerr=switch_errors, fmt='o-', capsize=5, label='Switch Strategy')
    
    plt.plot(n_values, [1/n for n in n_values], '--', color='blue', label='Theoretical No Switch (1/n)')
    plt.plot(n_values, [(n-1)/n for n in n_values], '--', color='orange', label='Theoretical Switch ((n-1)/n)')

    plt.xlabel('Number of Doors (n)')
    plt.ylabel('Winning Probability')
    plt.title('Generalized Monty Hall Problem (n Doors)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/generalized_win_rates.png")
    plt.show()

if __name__ == "__main__":
    n_values = [3, 5, 10, 25, 50, 100]
    num_trials = 10000

    no_switch_rates, switch_rates, no_switch_errs, switch_errs = run_simulations_for_n_doors(n_values, num_trials)
    plot_generalized_results(n_values, no_switch_rates, switch_rates, no_switch_errs, switch_errs)
