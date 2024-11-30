# data yang dimasukan pasti string
data = input("Jawaban Data: ")

print("data = ", data,",type =", type(data))

# jika ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))

print("data = ", angka,",type =",type(angka))

#jika ingin mengambil boolean, maka
biner = bool(int(input("masukan nilai boolean: "))) # lebih mudah jika dimasukkan int

print("data = ",biner,",type =",type(biner))