import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def fitness_function(x):
    return -(x - 37)**2 + 2500

gga_table = []
init_pop = [12, 45, 67, 32, 85]
new_pop = []

for i in range(len(init_pop)):
    fitness = [fitness_function(x) for x in init_pop]

    if len(fitness) < 2:
        break
    #Tournament selection: picks best two as parents
    p1_idx, p2_idx = np.argsort(fitness)[-2:]
    
    

    p1, p2 = init_pop[p1_idx], init_pop[p2_idx]
    cross_x = (p1 + p2)/2
    mut_dx = np.random.uniform(-5,5)
    new_x = cross_x + mut_dx

    entry = [1, i, p1,p2, cross_x,mut_dx, new_x, fitness_function(new_x)]
    gga_table.append(entry)
    new_pop.append(new_x)


    gga_df = pd.DataFrame(gga_table, columns=[
        'Gen', 'ID', 'Parent1', 'Parent2', 'Crossover', 'Mut_Δx','New_X','fitness(x)'
    ])

    gga_csv = os.path.join(script_dir, "gga_trace.csv")

    if os.path.exists(gga_csv):
        gga_df.to_csv(gga_csv, mode="a", index=False, header=False)
    else:
        gga_df.to_csv(gga_csv, index=False)

    plt.figure(figsize=(7,4))
    plt.plot(gga_df['ID'], gga_df['fitness(x)'], marker='o', label='Fitness')
    plt.title('GGA Fitness Progress')
    plt.xlabel('Individual ID')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.legend()
    plt.show()