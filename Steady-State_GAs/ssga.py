import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# --- Ensure files save inside this script’s folder ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def fitness_function_ssga(x):
    """Example fitness function — you can change this for your use case."""
    return -(x - 50)**2 + 3000  # Parabolic fitness centered around 50

# --- Parameters ---
population_size = 6
generations = 10
mutation_rate = 0.2

# --- Initialize population ---
population = np.random.uniform(0, 100, population_size)

# --- Storage for results ---
ssga_records = []

for gen in range(generations):
    # Evaluate fitness
    fitness = np.array([fitness_function_ssga(x) for x in population])

    # Select two best parents
    if len(fitness) < 2:
        print("Not enough individuals to select parents.")
        break
    p1_idx, p2_idx = np.argsort(fitness)[-2:]
    p1, p2 = population[p1_idx], population[p2_idx]

    # Crossover (average of parents)
    child = (p1 + p2) / 2

    # Mutation
    if np.random.rand() < mutation_rate:
        mutation_amount = np.random.uniform(-5, 5)
        child += mutation_amount
    else:
        mutation_amount = 0

    # Evaluate child fitness
    child_fitness = fitness_function_ssga(child)

    # Replace worst individual
    worst_idx = np.argmin(fitness)
    population[worst_idx] = child

    # Record data
    ssga_records.append([
        gen + 1, p1, p2, child, mutation_amount, child_fitness, np.mean(fitness)
    ])

ssga_df = pd.DataFrame(ssga_records, columns=[
    "Generation", "Parent1", "Parent2", "Child", "Mutation", "Child_Fitness", "Avg_Fitness"
])

csv_path = os.path.join(script_dir, "ssga_trace.csv")

if os.path.exists(csv_path):
    ssga_df.to_csv(csv_path, mode='a', index=False, header=False)
else:
    ssga_df.to_csv(csv_path, index=False)

# --- Graph Display ---
plt.figure(figsize=(8, 5))
plt.plot(ssga_df["Generation"], ssga_df["Avg_Fitness"], 'bo-', label="Average Fitness")
plt.plot(ssga_df["Generation"], ssga_df["Child_Fitness"], 'ro--', label="Child Fitness")
plt.title("SSGA Fitness Progress")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
