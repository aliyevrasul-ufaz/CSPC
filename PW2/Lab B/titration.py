"""
PW2 Lab B Part 5 -- find a titration's equivalence point.
Computed using np.gradient on pH versus volume_base.
"""
import numpy as np
import matplotlib.pyplot as plt

# Read titration data from CSV
data = np.genfromtxt("titration.csv", delimiter=",", names=True)
V = data["volume_base"]
pH = data["pH"]

# Compute the slope of the pH curve
slope = np.gradient(pH, V)

# Find the volume where the slope is largest (equivalence point)
index = np.argmax(slope)
V_eq = V[index]

print(f"Equivalence point volume = {V_eq:.2f} mL")
print(f"Maximum slope = {slope[index]:.4f} pH/mL")

# Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: pH versus volume
axes[0].plot(V, pH, marker=".", markersize=3, color='purple')
axes[0].axvline(V_eq, color='red', linestyle="--", label=f"V_eq = {V_eq:.1f} mL")
axes[0].set_xlabel("Volume of base added (mL)")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration curve")
axes[0].legend()
axes[0].grid(True)

# Right: slope versus volume
axes[1].plot(V, slope, color='green')
axes[1].axvline(V_eq, color='red', linestyle="--", label=f"V_eq = {V_eq:.1f} mL")
axes[1].scatter([V_eq], [slope[index]], color='red', zorder=5)
axes[1].set_xlabel("Volume of base added (mL)")
axes[1].set_ylabel("Slope (pH/mL)")
axes[1].set_title("Slope of the titration curve")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig("titration.png", dpi=300)
plt.show()