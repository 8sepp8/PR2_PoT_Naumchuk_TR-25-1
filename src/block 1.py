import random

print(10*'='," Блок 1: Дослідження колізії",10*'=')
N_space = 365
k_values = [5, 10, 15, 20, 23, 30, 40, 50, 60, 70, 80]
simulations = 10000

print(f"{'k':<5} | {'P(теор)':<15} | {'W(стат)':<15} | {'похибка':<15}")
print("-" * 55)

for k in k_values:
    p_no_collision = 1.0
    for i in range(k):
        p_no_collision *= (1.0 - i / N_space)
    p_theor = 1.0 - p_no_collision
    
    collisions = 0 #Симуляція методом монте карло
    for _ in range(simulations):
        items = [random.randint(1, N_space) for _ in range(k)] #генерація рандомних чисел від 1 до 365
        if len(set(items)) < len(items):
            collisions += 1
            
    w_stat = collisions / simulations#вирахування статистичної частоти
    error = abs(w_stat - p_theor)
    
    print(f"{k:<5} | {p_theor:<15.5f} | {w_stat:<15.5f} | {error:<15.5f}")