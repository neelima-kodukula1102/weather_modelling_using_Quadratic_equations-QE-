import matplotlib.pyplot as plt  
a = 0.4
b = -2.5
c = 27
t = 6
T = a * t**2 + b * t + c
print("=== Weather Model: Hardcoded Version ===")
print(f"Predicted temperature at t={t}: {T:.2f} °C")

times = list(range(0, 11))  # t = 0..10
temps = [a * x**2 + b * x + c for x in times]  

plt.plot(times, temps, marker="o", label="Temperature curve")
plt.scatter([t], [T], color="red", label=f"Predicted t={t}")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.title("Weather Modeling (Hardcoded Values)")
plt.legend()
plt.grid(True)

plt.savefig("graph_version1.png", bbox_inches="tight") 
plt.show() 
