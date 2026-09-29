import random
import math

print(10*'=',"Блок 2: парольна безпека (варіант 1)",10*'=')
pool = ['D'] * 10 + ['L'] * 26#створення набору символів з цифр(D) та букв (L)
simulations = 100000

# Теоретичні розрахунки
total_passwords = math.perm(36, 6)
p_A_theor = math.perm(26, 6) / total_passwords
p_B_theor = (math.perm(10, 2) * math.perm(26, 4)) / total_passwords
p_A_intersect_B_theor = 0.0  #пароль не може бути тільки з букв та мати 2 цифри
p_A_union_B_theor = p_A_theor + p_B_theor
p_not_A_theor = 1.0 - p_A_theor

count_A = 0
count_B = 0
count_intersect = 0
count_union = 0
count_not_A = 0

for i in range(simulations):
    pwd = random.sample(pool, 6)#генерація унікальної комбінації
    is_A = all(c == 'L' for c in pwd)#пароль тільки з букв
    is_B = (pwd[0] == 'D' and pwd[1] == 'D' and #першa цифри потім 4 букви
            pwd[2] == 'L' and pwd[3] == 'L' and 
            pwd[4] == 'L' and pwd[5] == 'L')
    
    if is_A: count_A += 1
    if is_B: count_B += 1
    if is_A and is_B: count_intersect += 1
    if is_A or is_B: count_union += 1
    if not is_A: count_not_A += 1

print(f"{'подія':<12} | {'теорія':<15} | {'статистика':<15} | {'похибка':<15}")
print("-" * 65)

events = [
    ("P(A)", p_A_theor, count_A / simulations),
    ("P(B)", p_B_theor, count_B / simulations),
    ("P(A ∩ B)", p_A_intersect_B_theor, count_intersect / simulations),
    ("P(A U B)", p_A_union_B_theor, count_union / simulations),
    ("P(не A)", p_not_A_theor, count_not_A / simulations)
]

for name, theor, stat in events:
    print(f"{name:<12} | {theor:<15.5f} | {stat:<15.5f} | {abs(theor - stat):<15.5f}")