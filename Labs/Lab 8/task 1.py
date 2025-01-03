import random

def create_distance_matrix(num_cities):
    matrix = [[random.randint(10, 100) for _ in range(num_cities)] for _ in range(num_cities)]
    for i in range(num_cities):
        matrix[i][i] = 0  
    return matrix

def initialize_population(pop_size, num_cities):
    population = [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]
    return population
    
def calculate_distance(tour, distance_matrix):
    total_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_distance += distance_matrix[tour[-1]][tour[0]]  
    return total_distance

def evaluate_fitness(population, distance_matrix):
    fitness = []
    for tour in population:
        distance = calculate_distance(tour, distance_matrix)
        fitness.append(1 / distance)  
    return fitness

def select_parents(population, fitness, num_parents=2):
    selected = random.choices(population, weights=fitness, k=num_parents)
    return selected


def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size

    child[start:end] = parent1[start:end]
    pointer = end
    for gene in parent2:
        if gene not in child:
            if pointer == size:
                pointer = 0
            child[pointer] = gene
            pointer += 1
    return child

# Mutation to introduce diversity
def mutate(tour, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic Algorithm for TSP
def genetic_algorithm_tsp(distance_matrix, pop_size, num_generations):
    num_cities = len(distance_matrix)
    population = initialize_population(pop_size, num_cities)
    
    for generation in range(num_generations):
        fitness = evaluate_fitness(population, distance_matrix)
        
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, fitness)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            
            # Apply mutation
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population
    

    final_fitness = evaluate_fitness(population, distance_matrix)
    best_index = final_fitness.index(max(final_fitness))
    best_tour = population[best_index]
    best_distance = calculate_distance(best_tour, distance_matrix)
    
    return best_tour, best_distance


cities = 5
pop_size = 10
generations = 50


distance_matrix = create_distance_matrix(cities)
best_tour, best_distance = genetic_algorithm_tsp(distance_matrix, pop_size, generations)

print("Best tour:", best_tour)
print("Best distance:", best_distance)



# import random
# import numpy
# class Chromosome: 
#     def __init__(self, genes): 
#          self.genes = genes
#          self.fitness = 0
     
#     def calculate_fitness(self): 
#         # Calculate total value if weight is within limit,
#         #  else set fitness to 0
#         total_weight = total_value = 0
#         for i in range(len(self.genes)):
#             if self.genes[i] == 1:
#                 total_value += values[i]
#                 total_weight += weights[i]
#         if total_weight > weight_limit:
#             self.fitness = 0
#         else:
#             if total_weight> 0:     
#                 self.fitness=  total_value / total_weight
     
# class GeneticAlgorithm: 
#     def __init__(self, population_size, mutation_rate, 
# crossover_rate, generations): 
#         self.population_size  = population_size
#         self.mutation_rate = mutation_rate
#         self.crossover_rate = crossover_rate
#         self.generations = generations
#         self.population = self.initialize_population()
     
#     def initialize_population(self): 
#         population = []
#         for i in range(self.population_size):
#             gene = [random.randint(0,1) for i in range(len(values))]
#             ch = Chromosome(gene)
#             ch.calculate_fitness() 
#             population.append(ch)
#         return population
     
 
 
#     def selection(self): 
        
     
#     def crossover(self, parent1, parent2): 
#         # Perform crossover to produce offspring 
#         if random.random() < self.crossover_rate:
#             ran_num = random.randint(1,len(parent1)-1)
#             child1 = parent1[:ran_num] + parent2[ran_num:]
#             child2 = parent2[:ran_num] + parent1[ran_num:]
#             return child1 , child2
#         return parent1 , parent2
     
#     def mutate(self, chromosome): 
#         # Apply mutation by flipping random bits 
#         for i in range(len((chromosome))):
#             if random.random() <= self.mutation_rate:
#                 self.generations[i] = 1- self.generations[i]
#         pass 
     
#     def evolve(self): 
#         for _ in range(self.generations):
#             new_population = []
#             while len(new_population) < self.population_size:
#                 parent1 = self.selection()
#                 parent2 = self.selection()
#                 child1, child2 = self.crossover(parent1, parent2)
#                 new_population.append(self.mutate(child1))
#                 if len(new_population) < self.population_size:
#                     new_population.append(self.mutate(child2))
#             # self.population = new_population
     
#     def get_best_solution(self): 
#         # Identify and return the best chromosome in the 
#         pass
# weight_limit = 50
# weights = [10,20,30,15,25]
# values = [60,100,120,75,90]
# population_size = 10
# mutation_rate = 0.01
# crossover_rate = 0.7
# generations = 20
