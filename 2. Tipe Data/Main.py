# Tipe data : angka satuan (integer)

#tipe data tanpa ada koma (integer)
data_integer = 1
print(type(data_integer))
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data kedua : angka dengan koma(float)
data_float = 2.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#tipe data : kumpulan kumpulan (string)
data_string = "kala"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#tipe data : biner true/false (boolean)
data_boolean = True
print("data : ", data_boolean)
print("- bertipe : ", type(data_boolean))

##tipe data khusus

#bilangan kompleks
data_complex = complex(7, 8)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.7)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
