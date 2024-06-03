a = float(input('Masukkan Bilangan Pertama: '))
o = input('Masukkan operator: ')
b = float(input('Masukkan Bilangan Kedua: '))

a1 = (a + b)
b1 = (a - b)
c1 = (a * b)
d1 = (a / b)
e1 = (a **b)

if o == '+':
    print('Hasil dari', a, '+', b, 'adalah' ,a1)
elif o == '-':
    print('Hasil dari', a, '-', b, 'adalah' ,b1)
elif o == '*':
    print('Hasil dari', a, '*', b, 'adalah' ,c1)
elif o == '/':
    print('Hasil dari', a, '/', b, 'adalah' ,d1)
elif o == '^':
    print('Hasil dari', a, '^', b, 'adalah', e1)
else:
    print('Karena terjadi kesalahan silahkan ulangi')
