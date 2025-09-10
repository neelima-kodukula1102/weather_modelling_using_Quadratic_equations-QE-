# Weather modeling using quadratic equation (Keyboard Input + Graph)

import matplotlib.pyplot as plt

# === Take coefficients and time from user ===
print("=== Weather Model: Keyboard Input Version ===")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))

# === Calculate predicted temperature ===
T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f} °C")

# === Graph code ===
times = list(range(0, int(t)+6))  # Plot from 0 to a few steps beyond t
temps = [a * x**2 + b * x + c for x in times]

plt.plot(times, temps, marker="o", label="Temperature curve")
plt.scatter([t], [T], color="red", label=f"Predicted t={t}")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.title("Weather Modeling (Keyboard Input)")
plt.legend()
plt.grid(True)

plt.savefig("graph_version2.png", bbox_inches="tight")  # Save graph
plt.show()  # Display graph
