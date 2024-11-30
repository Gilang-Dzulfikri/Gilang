print("\nPROGRAM KONVERSI TEMPERATUR\n")

reamur = float(input('masukan suhu dalam reamur : '))
print("suhu adalah ",reamur, "Reamur")

# Celcius
celcius = (5/4) * reamur
print("suhu dalam reamur adalah ",celcius, "Celcius")

# fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam kelvin adalah ",kelvin, "Kelvin")