import matplotlib.pyplot as plt

try:
    with open("inputs_multiple.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise ValueError("Input file is empty")
except FileNotFoundError:
    print("Error: 'inputs_multiple.txt' not found in current folder.")
    exit()
except ValueError as ve:
    print("Error:", ve)
    exit()

for idx, line in enumerate(lines, 1):
    a, b, c, t = map(float, line.strip().split())
    T = a * t**2 + b * t + c
    print(f"Set {idx}: a={a}, b={b}, c={c}, t={t} -> T={T:.2f} °C")

    times = list(range(0, int(t)+6))
    temps = [a * x**2 + b * x + c for x in times]

    plt.plot(times, temps, marker="o", label=f"Temperature curve Set {idx}")
    plt.scatter([t], [T], color="red", label=f"Predicted t={t}")

plt.xlabel("Time (t)")
plt.ylabel("Temperature (°C)")
plt.title("Weather Modeling (File Input - Multiple Sets)")
plt.legend()
plt.grid(True)
plt.savefig("graph_version4.png", bbox_inches="tight")
plt.show()
