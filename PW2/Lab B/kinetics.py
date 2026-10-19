"""
PW2 Lab B Part 3 -- fit a reaction rate constant.
First-order reaction decays as C(t) = C0 * exp(-k*t).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Read experimental data from CSV
data = np.genfromtxt("kinetics.csv", delimiter=",", names=True)
t = data["time"]
C = data["concentration"]

# Initial concentration: first measured value
C0 = C[0]

# Total squared error function
def total_error(k):
    predicted = C0 * np.exp(-k[0] * t)
    return np.sum((C - predicted)**2)

# Minimize the error using SLSQP method with bounds
result = minimize(
    total_error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k_fitted = result.x[0]
print(f"Fitted rate constant k = {k_fitted:.6f}")
print(f"Total squared error = {result.fun:.6f}")

# Plot measured data and fitted curve
t_fit = np.linspace(t.min(), t.max(), 300)
C_fit = C0 * np.exp(-k_fitted * t_fit)

plt.figure(figsize=(8, 5))
plt.scatter(t, C, color='red', label="Measured data")
plt.plot(t_fit, C_fit, color='blue', label=f"Fitted model (k={k_fitted:.4f})", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-order reaction kinetics fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("kinetics.png", dpi=300)
plt.show()