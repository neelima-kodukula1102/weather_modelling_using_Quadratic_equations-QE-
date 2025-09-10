import matplotlib.pyplot as plt

# Quadratic weather function
def quadratic_weather_model(t):
    a, b, c = -0.2, 1.5, 24
    return a*t**2 + b*t + c

hours = list(range(0, 25, 12))  # 0, 12, 24
colors = ['blue', 'green', 'red']  # 3 iterations

plt.figure(figsize=(8,5))
print("\n=== ITERATIVE MODE ===")

for iteration in range(3):
    temps = [quadratic_weather_model(h) + iteration*2 for h in hours]  # small offset per iteration
    plt.plot(hours, temps, marker='^', linestyle='-', color=colors[iteration], label=f"Iteration {iteration+1}")
    print(f"Iteration {iteration+1}:")
    for h, temp in zip(hours, temps):
        print(f"Time: {h} hrs -> Temp: {temp:.2f}°C")
    print("---")

plt.title("Iterative Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("iterative_model.png")
plt.show()






