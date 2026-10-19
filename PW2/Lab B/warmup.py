"""
PW2 Lab B Part 2 -- three routes to a minimum.
Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1         (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- Helper: Gradient Descent Implementation ----------
def gradient_descent(grad_func, x0, lr=0.01, steps=10000, tol=1e-8):
    x = x0
    for _ in range(steps):
        step = lr * grad_func(x)
        x -= step
        if abs(step) < tol:
            break
    return x

# ---------- 2A: Easy convex function ----------
def f(x):   return (x - 3)**2 + 1
def df(x):  return 2 * (x - 3)
def d2f(x): return 2.0

x0 = 0.0
gd_2a = gradient_descent(df, x0, lr=0.1)
nt_2a = newton(df, x0, fprime=d2f)
sl_2a = minimize(lambda x: f(x[0]), [x0], method="SLSQP").x[0]

print("--- PART 2A: Easy Function ---")
print(f"Gradient descent: x = {gd_2a:.6f}, f(x) = {f(gd_2a):.6f}")
print(f"Newton:           x = {nt_2a:.6f}, f(x) = {f(nt_2a):.6f}")
print(f"SLSQP:            x = {sl_2a:.6f}, f(x) = {f(sl_2a):.6f}")


# ---------- 2B: Harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

print("\n--- PART 2B: Harder Function ---")
for start_x0 in [0.0, 2.0]:
    gd_2b = gradient_descent(dg, start_x0, lr=0.01)
    nt_2b = newton(dg, start_x0, fprime=d2g)
    sl_2b = minimize(lambda x: g(x[0]), [start_x0], method="SLSQP").x[0]
    
    curv = d2g(nt_2b)
    if curv > 0:
        pt_type = "local minimum"
    elif curv < 0:
        pt_type = "local maximum"
    else:
        pt_type = "inflection / zero curvature"

    print(f"\nStarting x0 = {start_x0}:")
    print(f"  - Gradient descent: x = {gd_2b:.6f}, g(x) = {g(gd_2b):.6f}")
    print(f"  - Newton's method:  x = {nt_2b:.6f}, g(x) = {g(nt_2b):.6f}, g''(x) = {curv:.4f} ({pt_type})")
    print(f"  - SLSQP minimize:   x = {sl_2b:.6f}, g(x) = {g(sl_2b):.6f}")