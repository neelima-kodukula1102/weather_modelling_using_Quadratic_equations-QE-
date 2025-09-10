import matplotlib.pyplot as plt

a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a*t**2 + b*t + c

print("=== WATERFALL MODEL ===")
times = list(range(0, 25, 6))
temps = []
for t in times:
    temp = quadratic_weather_model(t)
    temps.append(temp)
    print(f"Time: {t} hrs -> Predicted Temp: {temp:.2f}°C")

plt.plot(times, temps, marker='o', color='blue', label='Waterfall Temp')
plt.title("Waterfall Model Temperature Prediction")
plt.xlabel("Time (hrs)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("waterfall_graph.png")
plt.show()
