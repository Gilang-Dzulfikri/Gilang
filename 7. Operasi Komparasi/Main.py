#====operasi komparasi====

# setiap hasil dari operasi komparasi adalah boolean

#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar (>)
print('======== lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)

# kurang dari (<)
print('======== kurang dari (<)')
hasil = b < 1
print(b,"<",1,"=",hasil)

# lebih besar sama dengan (>=)
print('======== lebih besar sama dengan dari (=>)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)

# kurang dari sama dengan (<=)
print('======== kurang dari sama dengan dari (<=)')
hasil = b <= 3
print(b,'<=',3,'=',hasil)

# sama dengan (==)
print('======== sama dengan dari (==)')
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan (!=)
print('======== tidak sama dengan dari (!=)')
hasil = 4 != 3
print(a,'!=',3,'=',hasil)

# is dan is not
# 'is' sebagai komparasi objek identitas
x = 6 # ini adalah assigment membuat object
y = 6
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 6
y = 6
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)
