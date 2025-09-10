import matplotlib.pyplot as plt

# Quadratic weather function
def quadratic_weather_model(t):
    a, b, c = -0.2, 1.5, 24
    return a*t**2 + b*t + c

hours = list(range(0, 25, 6))  # 0,6,12,18,24
temps = [quadratic_weather_model(h) for h in hours]

plt.plot(hours, temps, marker='o', linestyle='-', color='blue')
plt.title("Waterfall Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("waterfall_model.png")  # saves the plot
plt.show()

# Print values like before
print("=== WATERFALL MODEL ===")
for h, temp in zip(hours, temps):
    print(f"Time: {h} hrs -> Temp: {temp:.2f}°C")
