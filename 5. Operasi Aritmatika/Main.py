#=======operasi aritmatika=======

a = 12
b = 5

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi perpangkatan (eksponen) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi sisa pembagian (modulus) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

#=======prioritas operasi=========

x = 3
y = 2
z = 5

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
# kurung akan mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,"=",hasil)