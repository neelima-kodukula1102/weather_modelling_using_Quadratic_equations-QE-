import matplotlib.pyplot as plt

a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a*t**2 + b*t + c

print("=== INCREMENTAL MODEL ===")
increments = [0, 8, 16, 24]
for inc in range(1, 4):
    print(f"Increment {inc}:")
    temps = []
    for t in increments:
        temp = quadratic_weather_model(t)
        temps.append(temp)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    plt.plot(increments, temps, marker='o', label=f"Increment {inc}")
    print("---")

plt.title("Incremental Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("incremental_graph.png")
plt.show()
