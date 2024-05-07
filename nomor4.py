def bmi():
    berat_badan = float(input('Masukan berat badan (kg) : '))
    tinggi_badan = float(input('Masukan tinggi badan : '))
    penghitungan_bmi = berat_badan / (tinggi_badan * 2)

    while True:
        if penghitungan_bmi <= 18.5:
            print(penghitungan_bmi, 'Nilai BMI anda', penghitungan_bmi, 'kategori berat badan kurang')
        if penghitungan_bmi <= 24.9:
            print(penghitungan_bmi, 'Nilai BMI anda', penghitungan_bmi, 'kategori berat badan normal')
        if penghitungan_bmi <= 29.9 or penghitungan_bmi :
            print(penghitungan_bmi, 'Nilai BMI anda', penghitungan_bmi, 'kategori kelebihan berat badan')
        if penghitungan_bmi >= 30:
            print(penghitungan_bmi, 'Nilai BMI anda', penghitungan_bmi, 'kategori obesitas')
        else:
            print('tidak valid')
        break