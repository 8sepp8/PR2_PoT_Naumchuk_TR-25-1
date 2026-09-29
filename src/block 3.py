import random
import matplotlib.pyplot as plt

print(10*'=',"Блок 3: геометрична ймовірніть складної області",10*'=')
exact_area = 0.181695
N_values = [100, 1000, 10000, 100000, 1000000]
frequencies = []

print(f"{'N':<10} | {'W(D) (стат)':<15} | {'S(D) (теор)':<15} | {'похибка':<15}")
print("-" * 60)

for n in N_values:
    matches = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if y <= x**2 and y >= 1 - x:# перевірка потрапляння точки в задану область
            matches += 1
            
    w_d = matches / n
    frequencies.append(w_d)
    error = abs(w_d - exact_area)
    print(f"{n:<10} | {w_d:<15.6f} | {exact_area:<15.6f} | {error:<15.6f}")

plt.plot(N_values, frequencies, marker='o', label='статистична частота W(D)')
plt.axhline(y=exact_area, color='r', linestyle='--', label='точна площа S(D)')
plt.xscale('log')
plt.xlabel('Кількість згенерованих точок N (логарифмічна шкала)')
plt.ylabel('Ймовірність / Площа')
plt.title('Оцінка геометричної ймовірності методом Монте-Карло')
plt.legend()
plt.grid(True, linestyle="--")
plt.show()