try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        jumlah_hari = 31
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        jumlah_hari = 30
    elif bulan == 2:
        jumlah_hari = 29
    else:
        raise ValueError
    print("Jumlah hari:", jumlah_hari)
except ValueError:
    print("Bulan yang diinputkan tidak valid.")
    