
Temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")

if (unit == "f" or "F"):
  celsius = ((Temp - 32) / 1.8)
  print(f"{Temp}° in Fahrenheit is equivalent to {celsius}° Celsius.")
else: 
  fahrenheit = (Temp * 1.8) + 32
  print(f"{Temp}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")