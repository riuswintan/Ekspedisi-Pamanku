uang_jalan = int(input("Masukkan uang jalan per hari: "))
jumlah_hari = int(input("Masukkan jumlah hari dalam sebulan: "))
print("""Apakah anda ingin menggunakan sampel plat kendaraan dari kami?
ketik 'Y' untuk menggunakan, ketik 'N' untuk memasukkan data.""")
answer = input()
if answer == "Y":
    list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
else:
    list_plat_nomor = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
      elements = int(input())
      list_plat_nomor.append(elements)
print("Plat nomor kendaraan yang digunakan adalah   :",list_plat_nomor) 
# Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
kendaraan_genap = 0
kendaraan_ganjil = 0 
for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1 
    else:
        kendaraan_ganjil += 1
# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0
total_pengeluaran_ganjil = 0
total_pengeluaran_genap = 0

while i<= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
        total_pengeluaran_genap += (kendaraan_genap * uang_jalan) 
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)
        total_pengeluaran_ganjil += (kendaraan_ganjil * uang_jalan)  
    i += 1
# Cetak total pengeluaran
print("Total pengeluaran untuk kendaraan plat genap :",total_pengeluaran_genap)
print("Total pengeluaran untuk kendaraan plat ganjil:",total_pengeluaran_ganjil)    
print("Total pengeluaran untuk seluruh kendaraan    :",total_pengeluaran)
