# Evolutionary-Algorithms
__Overview__
This project focuses on using Evolutionary Algortithms such as Genetic Algorithms (Generational genetic algorithms and Steady-State genetic algorithms) and Particle Swarm Optimisation (PSO) to find the maximum of a parabolic function

Each EA will be run on its own, results will be stored in a CSV, and graphs will be generates which will show fitness of individuals.

Purpose of this project is to demonstrate optimization by using EAs, as well as exploring the differences between each algorithm paradigms, and showing the convergence of solutions throguh each generation.

## Algorithms Used
1. Generational genetic algorithm (GGA):
   - Entire population is replaced after each generation
   - Selects the top individuals as parents for crossover
   - Applies mutation to offspring
   - Fitness is recalculated for each individual through each generation
2. Steady-State genetic algorithm (SSGA):
   - Replaces only the worst individual in each generation
   - Keeps individuals with good fitness to ensure gradual evolution through each generation
   -  Mutation is probabilistic
3. Particle Swarm Optimisation (PSO):
   - Simulates a swarm of particles exploring search space
   - Each particle updates there position based on personal best and global best positions
   - Try finds balance between exploration and exploitation

