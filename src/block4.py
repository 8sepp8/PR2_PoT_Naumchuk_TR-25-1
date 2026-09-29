import random

print(10*'='," Блок 4: тестове покритя",10*'=')
total_configurations = 81
test_subset_size = 9
simulations = 10000

p_theor = test_subset_size / total_configurations
print(f"загальна кількість конфігурацій: {total_configurations}")
print(f"загальна кількість тестового набору: {test_subset_size}")
print(f"теоретична ймовірніть: P = {test_subset_size}/{total_configurations} = {p_theor:.4f}\n")

hits = 0
for i in range(simulations):
    random_config = random.randint(1, total_configurations)
    if random_config <= test_subset_size:
        hits += 1

w_stat = hits / simulations
error = abs(w_stat - p_theor)

print(f"проведенно симуляцій: {simulations}")
print(f"потрапляння в тестову множину: {hits}")
print(f"статистична частота: W = {w_stat:.4f}")
print(f"абсолютна похибка: {error:.4f}")