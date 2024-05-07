berat_badan = int(input('Masukan berat badan (kg) : '))
tinggi_badan = int(input('Masukan tinggi badan : '))
penghitungan_bmi = berat_badan//tinggi_badan ** 2
print(penghitungan_bmi, 'Nilai BMI anda')
if penghitungan_bmi < 18.5:
    print(penghitungan_bmi, 'kategori berat badan kurang')
if penghitungan_bmi 18.5 <= 24.9:
    print(penghitungan_bmi, 'kategori berat badan normal')
if penghitungan_bmi 25 <= 29.9:
    print(penghitungan_bmi, 'kategori kelebihan berat badan')
if penghitungan_bmi, >= 30:
    print(penghitungan_bmi, 'kategori obesitas')
