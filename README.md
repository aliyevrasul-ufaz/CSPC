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