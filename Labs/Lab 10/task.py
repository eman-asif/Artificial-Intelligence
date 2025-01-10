import random
def initialize_population(pop_size, string_length):
    return [''.join(random.choice('01') for _ in range(string_length)) for _ in range(pop_size)]

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring

def mutate(individual, mutation_rate):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '0' if individual[i] == '1' else '1'
    return ''.join(individual)


def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        next_generation = []
        
        for _ in range(pop_size // 2): 
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring1 = mutate(crossover(parent1, parent2), mutation_rate)
            offspring2 = mutate(crossover(parent2, parent1), mutation_rate)
            next_generation.extend([offspring1, offspring2])
        
        population = next_generation[:pop_size]  
        best_fitness = max(fitness_scores)
        print(f"Generation {generation + 1} - Best Fitness: {best_fitness}")
        
        if best_fitness == string_length:
            print("Optimal solution found!")
            break
    
    best_solution = max(population, key=calculate_fitness)
    return best_solution

if __name__ == "__main__":
    string_length = 20
    pop_size = 50
    num_generations = 100
    mutation_rate = 0.01
    
    solution = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print(f"Best Solution: {solution}")