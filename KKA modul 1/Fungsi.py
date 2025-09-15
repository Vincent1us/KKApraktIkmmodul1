def luas_keliling(phi, jari):
    luas=phi*(jari*jari)
    keliling = 2*phi*jari
    return luas, keliling
hasil_luas, hasil_keliling = luas_keliling(3.15,5)
print("Luas : ", hasil_luas)
print("Keliling ",hasil_keliling)