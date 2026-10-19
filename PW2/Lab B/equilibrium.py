"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.
Reaction: H2 + I2 <=> 2 HI
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# K imbalance function (equals zero at equilibrium)
def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K

# Method 1: Use scipy.optimize.newton for root-finding
x_newton = newton(k_imbalance, 0.5)

# Method 2: Use scipy.optimize.minimize to minimize squared imbalance
def objective(x):
    return k_imbalance(x[0])**2

result = minimize(
    objective,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)
x_slsqp = result.x[0]

print(f"Newton equilibrium extent x = {x_newton:.6f}")
print(f"SLSQP equilibrium extent x  = {x_slsqp:.6f}")

# Calculate equilibrium amounts
x_eq = x_newton
h2_eq = a - x_eq
i2_eq = b - x_eq
hi_eq = 2 * x_eq

print("\nEquilibrium composition:")
print(f"H2 = {h2_eq:.6f} mol")
print(f"I2 = {i2_eq:.6f} mol")
print(f"HI = {hi_eq:.6f} mol")

# Plot amounts as reaction progresses
x_values = np.linspace(0, 0.999, 300)
h2_values = a - x_values
i2_values = b - x_values
hi_values = 2 * x_values

plt.figure(figsize=(8, 5))
plt.plot(x_values, h2_values, label="H2", color='blue')
plt.plot(x_values, i2_values, label="I2", color='green')
plt.plot(x_values, hi_values, label="HI", color='orange')
plt.axvline(x_eq, color='red', linestyle="--", label=f"Equilibrium x={x_eq:.4f}")
plt.xlabel("Reaction extent x (mol)")
plt.ylabel("Amount (mol)")
plt.title("Chemical equilibrium composition")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("equilibrium.png", dpi=300)
plt.show()