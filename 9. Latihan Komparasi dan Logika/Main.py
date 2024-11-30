# membuat gabungan area rentang dari angka

# +++++++3-----------10+++++++

inputUser = float(input('masukan angka yang bernilai\n kurang dari 3 \natau \nlebih besar dari 10'))

# +++++++3---------------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

#-------------------10+++++++++
#Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =", isLebihDari)

# +++++++3-----------10+++++++

isCorrect = isKurangDari or isLebihDari
print("Angka yang ada masukan = ", isCorrect)

# -------3+++++++++++10-------
#kasus irisan
print("\n",10*"=","\n")
inputUser = float(input('masukan angka yang bernilai\n lebih dari 3 \natau \nkurang dari 10'))

# -------3++++++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# +++++++++++++++++10---------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

# -------3+++++++++++10-------

isCorrect = isKurangDari and isLebihDari
print("Angka yang ada masukan = ", isCorrect)
