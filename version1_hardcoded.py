def predict_temperature(a, b, c, t):
    """Quadratic temperature prediction: T(t) = a*t^2 + b*t + c"""
    return a * t**2 + b * t + c
a, b, c = 0.4, -2.5, 27
t = 6   
T = predict_temperature(a, b, c, t)
print("=== Weather Model: Hardcoded Version ===")
print(f"Equation: T(t) = {a}t² + {b}t + {c}")
print(f"Predicted temperature at t={t}: {T:.2f} °C")
