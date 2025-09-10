import matplotlib.pyplot as plt

a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a*t**2 + b*t + c

print("=== AGILE MODEL ===")
times = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    temps = []
    for t in times:
        temp = quadratic_weather_model(t)
        temps.append(temp)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    plt.plot(times, temps, marker='o', label=f"Sprint {sprint}")
    print("---")

plt.title("Agile Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("agile_graph.png")
plt.show()
