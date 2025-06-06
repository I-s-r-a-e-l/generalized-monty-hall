# 🧠 Generalized Monty Hall Simulation

This project simulates and visualizes the classic and generalized Monty Hall problem using Monte Carlo methods.

## 🎯 Purpose

To demonstrate counterintuitive outcomes in probability through simulation and help build intuition for switching strategies — especially in multi-door generalizations.

---

## 📁 Structure

- `classic_monty_hall.py` – 3-door Monty Hall simulation  
- `generalized_monty_hall.py` – N-door generalized version  
- `notebook/monty_hall_analysis.ipynb` – Jupyter notebook with explanations, plots, CI  
- `figures/` – Saved plots  
- `tests/test_monty.py` – Unit tests  
- `requirements.txt` – Required packages  
- `LICENSE` – MIT license  
- `README.md` – This file  
- `.gitignore` – Files to ignore  

---

## 🔢 What Is the Monty Hall Problem?

> A contestant chooses 1 of 3 doors. One hides a car; the others, goats.  
> The host, who knows what's behind the doors, opens another door revealing a goat.  
> Should the contestant stick or switch?

**Answer:** You should switch — the probability of winning increases from 1/3 to 2/3.

This project generalizes the problem to **n doors**, where the switching advantage grows with n.

---

## 🧪 Simulation Overview

We run Monte Carlo simulations to empirically confirm that:

- Without switching: Winning probability ≈ 1/n
- With switching: Winning probability ≈ (n - 1)/n

We also compute **confidence intervals** and **visualize convergence**.

---

## 📈 Example Plots

![Monty Hall Plot](figures/generalized_win_rates.png)
*(This plot will appear once the simulation outputs are saved to the `figures/` folder.)*

---

## 🧰 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/I-s-r-a-e-l/generalized-monty-hall.git
   cd generalized-monty-hall
   ```

2. **Install requirements**  
   (Use a virtual environment if you prefer)  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulations**  
   ```bash
   python classic_monty_hall.py
   python generalized_monty_hall.py
   ```

4. **Explore the notebook**  
   Launch Jupyter and open the notebook:  
   ```bash
   jupyter notebook
   # then open notebook/monty_hall_analysis.ipynb
   ```

## ✅ Features

- ✅ Classic 3-door version  
- ✅ Generalized to arbitrary number of doors (n)  
- ✅ Monte Carlo simulation  
- ✅ Matplotlib visualizations  
- ✅ Theoretical vs empirical probability  
- ✅ Confidence intervals  
- ✅ Unit tests  
- ✅ Optional animated simulation (WIP)

## 🔍 Key Insights

- Switching always increases your chances  
- As n increases, switching approaches 100% win rate  
- Monte Carlo is a great tool to validate theoretical probabilities  

## ⚙️ Technologies

- Python 3  
- NumPy  
- Matplotlib  
- Jupyter Notebook  
- Pytest  

## 📜 License

This project is licensed under the MIT License — feel free to use or adapt!

## 🙋‍♂️ About

Developed by Israel Adeboga to explore probability, simulation, and analytical reasoning in preparation for quantitative finance roles.
