import matplotlib.pyplot as plt

try:
    with open("inputs_single.txt", "r") as f:
        lines = f.readlines()
        if len(lines) < 4:
            raise ValueError("Input file must have 4 lines: a, b, c, t")
except FileNotFoundError:
    print("Error: 'inputs_single.txt' not found in current folder.")
    exit()
except ValueError as ve:
    print("Error:", ve)
    exit()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f} °C")

times = list(range(0, int(t)+6))
temps = [a * x**2 + b * x + c for x in times]

plt.plot(times, temps, marker="o", label="Temperature curve")
plt.scatter([t], [T], color="red", label=f"Predicted t={t}")
plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.title("Weather Modeling (File Input - Single Set)")
plt.legend()
plt.grid(True)
plt.savefig("graph_version3.png", bbox_inches="tight")
plt.show()
