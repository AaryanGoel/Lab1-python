
Temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
celsius = 0
fahremheit = 0
if unit == "f" or unit == "F":
  fahrenheit = Temp
  celsius = ((fahrenheit - 32) / 1.8)
  print(f"{fahrenheit}° in Fahrenheit is equivalent to {celsius}° Celsius.")
elif unit == "c" or unit == "C":
  celsius = Temp
  fahrenheit = float((celsius * 1.8)) + 32
  print(f"{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")