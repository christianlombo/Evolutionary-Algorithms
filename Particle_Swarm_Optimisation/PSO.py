import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def fitness_function(x):
    return -(x-35)**2 + 2500

# PSO demo: show first iteration trace for all particles
pso_table = []
np.random.seed(0)
positions = np.array([12, 45, 67, 32, 85], dtype=float)
velocities = np.zeros_like(positions)  # start at zero velocity
personal_best = positions.copy()
pbest_fitness = np.array([fitness_function(x) for x in positions])
gbest = positions[np.argmax(pbest_fitness)]
gbest_fit = np.max(pbest_fitness)
for i in range(len(positions)):
    r1, r2 = np.random.rand(2)
    # PSO velocity update parameters
    w, c1, c2 = 0.5, 2, 2
    velocities[i] = w*velocities[i] + c1*r1*(personal_best[i]-positions[i]) + c2*r2*(gbest-positions[i])
    new_x = positions[i]+velocities[i]
    pso_table.append([
        1, i, positions[i], velocities[i], fitness_function(positions[i]), personal_best[i],
        pbest_fitness[i], gbest, gbest_fit, r1, r2, new_x
    ])
# Output DataFrame
cols = ['Iter','P.ID','x','v','f(x)','pbest','fpbest','gbest','fgbest','r1','r2','Newx']
pso_df = pd.DataFrame(pso_table, columns=cols)

pso_csv = os.path.join(script_dir, "pso_trace.csv")

if os.path.exists(pso_csv):
    pso_df.to_csv(pso_csv, mode='a', index=False, header=False)
else:
    pso_df.to_csv(pso_csv, index=False)

# Plot results
plt.figure(figsize=(7,4))
plt.plot(pso_df['P.ID'], pso_df['f(x)'], 'bo-', label='Fitness per Particle')
plt.axhline(pso_df['fgbest'].iloc[0], color='r', linestyle='--', label='Global Best')
plt.title('PSO Particle Fitness (Iteration 1)')
plt.xlabel('Particle ID')
plt.ylabel('Fitness')
plt.legend()
plt.grid(True)
plt.show()