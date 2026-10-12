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