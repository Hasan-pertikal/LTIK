import numpy as np

def soal_1():
    arrC = np.array([21, 23, 24, 27, 22, 31, 29, 24, 26, 27])
    for i in arrC:
        fah = (i * (9/5)) + 32
        print(f"Suhu dalam Fahrenheit: {round(fah, 2)} F")

def soal_2():
    arrNilai = ([70, 72, 71, 74, 73, 75, 76, 77, 78, 79,
                 90, 90, 92, 92, 94, 95, 96, 99, 98, 97,
                 80, 81, 82, 83, 84, 89, 86, 87, 88, 85])
    arrNilai.sort()
    listNilai = list(arrNilai)
    listNilai.reverse()
    arrNilai = np.array(listNilai)

    x = 1

    for i in arrNilai:
        print(f"Nilai tertinggi ke-{x}: {i}")
        x += 1
        if x == 6:
            break

def soal_3():
    arrKeuntungan = np.array([13, 17, 21, 19, 14, 17, 21, 29, 34, 24, 15, 17, 18, 25])

    rataRata = np.mean(arrKeuntungan)
    rataRata = round(rataRata, 2)
    kMax = np.max(arrKeuntungan)
    kMin = np.min(arrKeuntungan)
    hariMax = np.where(arrKeuntungan == kMax)[0]
    hariMin = np.where(arrKeuntungan == kMin)[0]

    print(f"Rata-rata keuntungan: Rp. {rataRata} rb")
    print(f"Keuntungan tertinggi: Rp. {kMax} rb", f"-> terjadi pada hari ke-{hariMax[0] + 1}")
    print(f"Keuntungan terendah : Rp. {kMin} rb", f"-> terjadi pada hari ke-{hariMin[0] + 1}")

print("*" * 18)
soal_1()
#soal_2()
#soal_3()
print("*" * 18)