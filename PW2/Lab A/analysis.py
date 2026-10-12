import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

mean_accel = np.mean(a)
std_accel = np.std(a)
print(f"Mean acceleration: {mean_accel}")
print(f"Standard deviation of acceleration: {std_accel}")

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_recovered - y))
print(f"Largest position difference: {max_diff}")

plt.figure(figsize=(8, 8))

plt.subplot(3, 1, 1)
plt.plot(t, y, label="Position (y)")
plt.ylabel("Position (m)")
plt.title("Free Fall Motion Analysis")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, label="Velocity (v)", color="orange")
plt.ylabel("Velocity (m/s)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, label="Acceleration (a)", color="green")
plt.axhline(-9.81, color="red", linestyle="--", label="Theoretical -9.81")
plt.ylabel("Accel (m/s^2)")
plt.xlabel("Time (s)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("motion.png", dpi=300)
plt.show()