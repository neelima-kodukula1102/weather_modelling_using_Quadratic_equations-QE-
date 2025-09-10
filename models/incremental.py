import matplotlib.pyplot as plt

# Quadratic weather function
def quadratic_weather_model(t):
    a, b, c = -0.2, 1.5, 24
    return a*t**2 + b*t + c

hours = list(range(0, 25, 6))  # every 6 hours
colors = ['blue', 'green', 'red']  # 3 increments

plt.figure(figsize=(8,5))
print("\n=== INCREMENTAL MODE ===")

for inc in range(3):
    temps = [quadratic_weather_model(h) + inc*2 for h in hours]  # small offset per increment
    plt.plot(hours, temps, marker='d', linestyle='-', color=colors[inc], label=f"Increment {inc+1}")
    print(f"Increment {inc+1}:")
    for h, temp in zip(hours, temps):
        print(f"Time: {h} hrs -> Temp: {temp:.2f}°C")
    print("---")

plt.title("Incremental Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("incremental_model.png")
plt.show()

