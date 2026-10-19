# CSPC Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

PW1
Lab A: Reproducible Foundations
What I built:
Built the CSPC repository structure, set up the conda environment, implemented unit tests in pytest, and conducted a performance comparison between pure Python loops and vectorized NumPy operations.
Speed comparison (loop vs NumPy):
 loop: 3.1025 s
 numpy: 0.0004 s
 speed-up: 8597.8x faster
Tests: all passing? yes
Conclusion:
Vectorized NumPy implementation offers significantly higher execution speed compared to pure Python loops when simulating radioactive decay for large numbers of atoms. All unit tests successfully verified that the simulation output matches the analytical physical decay law. 
## PW1 — Lab B

The observed decay data was compared with the analytical decay law
N(t) = N0 exp(-λt), using λ = 0.3.

The observed data follows the same overall decreasing trend as the analytical decay curve.

Snakemake was used to automate the generation of the figure from the observed CSV data and the Python plotting script.
## PW2 — Lab A: Motion from Tracking Data

### Mean Acceleration
The mean acceleration calculated from the free-fall position measurements was -8.579687500000008 m/s². The result was compared with the theoretical gravitational acceleration of approximately –9.81 m/s².

### Noise Observation
The acceleration data was much noisier than the position data because numerical differentiation amplifies small measurement errors. Calculating acceleration requires differentiating the position data twice, which makes the noise more noticeable.

### Integration and Position Recovery
Integrating the noisy acceleration back to velocity and then to position produced a reconstructed position that was close to the original measurements. The largest absolute difference was 0.7845625000002201 m, showing that integration reduced the effect of noise.
## PW2 — Lab B: Optimization in Chemistry

### Part 2 — Three routes to a minimum
For the easy convex function, gradient descent, Newton's method, and SLSQP all found the minimum near x = 3.
For the harder function, the results depended on the method and the starting point. Newton's method can converge to a maximum or a minimum because it solves g'(x) = 0. The sign of g''(x) identifies the type of stationary point.

### Part 3 — Reaction kinetics
The first-order model C(t) = C0 * exp(-k*t) was fitted to the measured concentration data by minimizing the sum of squared errors using SLSQP.
- Fitted rate constant: $k \approx 0.2618$
- The fitted curve was compared with the measured data and saved in `kinetics.png`.

### Part 4 — Chemical equilibrium
The equilibrium extent was calculated using Newton's method and SLSQP. Both methods gave the same result.
- Equilibrium extent: $x \approx 0.6638$
- Equilibrium amounts:
  - $H_2 \approx 0.3362$ mol
  - $I_2 \approx 0.3362$ mol
  - $HI \approx 1.3277$ mol
- The composition curve is saved in `equilibrium.png`.

### Part 5 — Titration (bonus)
The equivalence point was identified as the volume where the numerical slope of the pH curve was largest.
- Equivalence point volume: $50.0$ mL
- The titration curve and its derivative slope are saved in `titration.png`.