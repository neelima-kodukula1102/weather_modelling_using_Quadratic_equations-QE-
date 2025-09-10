import matplotlib.pyplot as plt

# Quadratic weather function
def quadratic_weather_model(t):
    a, b, c = -0.2, 1.5, 24
    return a*t**2 + b*t + c

times_to_check = [0, 6, 12, 18, 24]
colors = ['blue', 'green']  # 2 sprints

plt.figure(figsize=(8,5))
print("\n=== AGILE MODE ===")

for sprint in range(2):
    temps = [quadratic_weather_model(t) + sprint*2 for t in times_to_check]  # offset per sprint
    plt.plot(times_to_check, temps, marker='s', linestyle='-', color=colors[sprint], label=f"Sprint {sprint+1}")
    print(f"Sprint {sprint+1}:")
    for t, temp in zip(times_to_check, temps):
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")

plt.title("Agile Model - weather model")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("agile_model.png")
plt.show()


