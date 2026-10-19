PW1 — Lab A: Reproducible Foundations
What I built: Built the CSPC repository structure, set up the conda environment, implemented unit tests in pytest, and conducted a performance comparison between pure Python loops and vectorized NumPy operations.

Speed comparison (loop vs NumPy):

Loop: 3.1025 s

NumPy: 0.0004 s

Speed-up: 8597.8x faster

Tests: All passing? Yes.

Conclusion: Vectorized NumPy implementation offers significantly higher execution speed compared to pure Python loops when simulating radioactive decay for large numbers of atoms. All unit tests successfully verified that simulation output matches analytical physical decay law.

PW1 — Lab B
The observed decay data was compared with the analytical decay law N(t) = N0 * exp(-λt), using λ = 0.3.

The observed data follows the overall decreasing trend as the analytical decay curve.

Snakemake was used to automate the generation of figures from observed CSV data and Python plotting scripts.

PW2 — Lab A: Motion from Tracking Data
Mean Acceleration
The mean acceleration calculated from free-fall position measurements was -8.5797 m/s².

The result was compared with theoretical gravitational acceleration of approximately -9.81 m/s².

Noise Observation
Acceleration data was much noisier than position data because numerical differentiation amplifies small measurement errors.

Calculating acceleration requires differentiating position data twice, making noise more noticeable.

Integration and Position Recovery
Integrating noisy acceleration back to velocity and then to position produced a reconstructed position close to original measurements.

The largest absolute difference was 0.7846 m, showing integration reduced the effect of noise.

PW2 — Lab B: Optimization in Chemistry
Part 2 — Three routes to a minimum
For the easy convex function, gradient descent, Newton's method, and SLSQP all found the minimum near x = 3.

For the harder function, results depended on the method and starting point. Newton's method can converge to a maximum or minimum because it solves g'(x) = 0. The sign of g''(x) identifies the type of stationary point.

Part 3 — Reaction kinetics
The first-order model C(t) = C0 * exp(-k*t) was fitted to measured concentration data by minimizing the sum of squared errors using SLSQP.

Fitted rate constant: k ≈ 0.2618

The fitted curve was compared with measured data and saved in kinetics.png.

Part 4 — Chemical equilibrium
The equilibrium extent was calculated using Newton's method and SLSQP, and both methods gave the same result.

Equilibrium extent: x ≈ 0.6638

Equilibrium amounts:

H₂ ≈ 0.3362 mol

I₂ ≈ 0.3362 mol

HI ≈ 1.3277 mol

The composition curve is saved in equilibrium.png.

Part 5 — Titration (bonus)
The equivalence point was identified as the volume where the numerical slope of the pH curve was largest.

Equivalence point volume: 50.0 mL

The titration curve and its derivative slope are saved in titration.png.