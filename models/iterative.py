import matplotlib.pyplot as plt

a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a*t**2 + b*t + c

print("=== ITERATIVE MODEL ===")
times = list(range(0, 25, 12))
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    temps = []
    for t in times:
        temp = quadratic_weather_model(t)
        temps.append(temp)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    plt.plot(times, temps, marker='o', label=f"Iteration {iteration}")
    print("---")

plt.title("Iterative Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("iterative_graph.png")
plt.show()
