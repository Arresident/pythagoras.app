from math import sqrt
print("Asumsikan sisi-sisi adalah a,b,c dengan c sebagai sisi miring")
formula = input('Sisi mana yang ingin anda hitung = ')

if formula == 'c':
    sisiA = int(input('Masukkan panjang sisi a = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
    
    sisiC = sqrt(sisiA*sisiA + sisiB*sisiB)
    print('Panjang sisi c adalah', sisiC)

elif formula == 'a':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
    
    sisiA = sqrt(sisiC*sisiC - sisiB*sisiB)
    print('Panjang sisi c adalah', sisiA)

elif formula == 'b':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiA = int(input('Masukkan panjang sisi a = '))
    
    sisiB = sqrt(sisiC*sisiC - sisiA*sisiA)
    print('Panjang sisi b adalah', sisiB)

else:
    print('Input Salah')