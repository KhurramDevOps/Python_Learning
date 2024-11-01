def fahrenheit_to_celsius():
    user_input = float(input("Enter Temperature in Fahrenheit : "))
    degrees_celsius = (user_input - 32) * 5.0/9.0
    
    print(f"\nTemperature: {user_input}F = {degrees_celsius}C")

if __name__ == "__main__":
    fahrenheit_to_celsius()