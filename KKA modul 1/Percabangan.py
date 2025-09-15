usia = int (input("Masukkan usia anda "))
if usia >0 and usia <= 13:
    print("Anda dalam kategori Anak-anak")
elif usia >=14 and usia <=24:
    print("Anda dalam kategori remaja")
elif usia >=25 and usia <=49:
    print("Anda dalam kategori dewasa")
elif usia > 50:
    print("Anda dalam kategori lansia")
else:
    print("Masukkan usia anda dengan benar")