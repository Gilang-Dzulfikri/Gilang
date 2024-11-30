print("\nPROGRAM KONVERSI TEMPERATUR\n")

kelvin = float(input('masukan suhu dalam kelvin : '))
print("suhu adalah ",kelvin, "Kelvin")

# Celcius
celcius = kelvin - 273
print("suhu dalam reamur adalah ",celcius, "Celcius")

# fahrenheit
reamur = 4/5 * (kelvin - 273)
print("Suhu dalam fahrenheit adalah ",reamur, "Reamur")