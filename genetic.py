# -*- coding: utf-8 -*-

import random
population=[]        # популяция
population_size=10   # размер популяции
chromosomes_length=5 # число генов (количество переменных в уравнении)
tournament_size=5    # число особей для турнирной селекции
crossover_rate=0.8   # процент особей для скрещивания
mutation_rate=0.5    # процент особей для мутации
solutions = []
# u * w * x * y * z^2 + z + x^2*y^2 + w*y^2 + u * y^2*z^2=40

# Начальная популяция (генерируется случайным образом)
for i in range(population_size):
    population.append([random.randint(-100,100) for i in range(chromosomes_length)])

# Функция приспособленности (fitness function)
def evaluation(population):
    fitness=[]
    f_objective=[]
    for individual in population:
        u = individual[0]
        w = individual[1]
        x = individual[2]
        y = individual[3]
        z = individual[4]
        health = ((u * w * x * y * (z**2)) + z + (x**2)*(y**2) + w*(y**2) + u * (y**2)*(z**2))-40
        f_objective.append(health)
        if(health == 0):
            solutions.append(individual.copy())

    for health in f_objective:
        if health != -1:
            fitness.append(1.0/(1+health))

    return fitness

# Проверка, найдено ли решение
def check(fitness,population,iteration):
    for health in fitness:
        if health==1:
            print("The solution is found after %d generations:"%(i))
            print(solutions[0])
            return 1
        else:
            return 0

# Турнирная селекция
def tournament(probablity,population):
    gen=[]
    parents=[]
    for j in range(population_size):
        team=[]
        for i in range(tournament_size):
            x=random.randint(0,population_size-1)
            team.append(probablity[x])
        gen.append(max(team))
        del team
    for parent in gen:
        parents.append(population[probablity.index(parent)])
    return parents

# Функция селекции
def selection(fitness):
    probablity=[]
    total_fitness=sum(fitness)
    for fit in fitness:
        probablity.append(fit/total_fitness)
    parents=tournament(probablity,population)
    return parents

# Функция скрещивания
def crossover(parents):
    i=0
    cross_number=int(crossover_rate*population_size)
    for i in range(cross_number):
        cross_location=random.randint(0,chromosomes_length-1)
        father=random.randint(0,len(parents)-1)
        mother=random.randint(0,len(parents)-1)
        if mother != father:
            geneF=parents[father][cross_location]
            geneM=parents[mother][cross_location]
            parents[father][cross_location]=geneM
            parents[mother][cross_location]=geneF
    return parents

# Функция мутации
def mutation(parents):
    for i in range(int(population_size*mutation_rate)):
        mutant=random.randint(0,len(parents)-1)
        mutant_gene=random.randint(0,chromosomes_length-1)
        parents[mutant][mutant_gene]=random.randint(0,30)
        return parents

# Алгоритма
for i in range(500000):
    fitness=evaluation(population)     # оценка приспособдленности
    parents=selection(fitness)         # селекция
    parents=crossover(parents)         # скрещивание
    parents=mutation(parents)          # мутация
    population[:]=parents[:]           # формирование новой популяции
    if check(fitness,population,i)==1: # проверка результата
        break