def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # Cek apakah parameter nama ada nilainya atau tidak
  if(nama !=""):
    # Simpan panjang nama kedalam variabel lenNama
    lenNama = len(nama)
    # Deklarasi variabel iNama dengan nilai 1 untuk kebutuhan perulangan
    iNama = 1
    # Lakukan perulangan sebanyak nilai yang ada di variabel lenNama
    while iNama <= lenNama:
      # Cek nilai urutan perulangan sama dengan nilai variabel lenNama
      if(iNama == lenNama):
        # print nama dengan String Slicing sesuai urutan perulangan dengan tambahan tanda seru !
        print(nama[0:iNama] + "!")
        # tambahkan nilai iNama dengan 1
        iNama = iNama + 1
      else:
        # print nama dengan String Slicing sesuai urutan perulangan
        print(nama[0:iNama])
        # tambahkan nilai iNama dengan 1
        iNama = iNama + 1
  else:
    # print jika parameter nama tidak ada nilainya
    return print("Tidak ada nama yang dicetak")

def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # Deklarasi variabel count dengan nilai 0
  count = 0
  # Lakukan perulangan menggungakan for dari parameter kata1
  for value in kata1:
    # Cek apakah nilai hasil perulangan ada di parameter kata2
    if value in kata2:
      # jika ada maka tambahkan nilai count dengan 1
      count = count + 1
  # Return count
  return print(count)

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # Cek jika parameter operator sama dengan -
  if operator == "-":
    # maka bil1 - bil2
    ret = bil1 - bil2
  # Cek jika parameter operator sama dengan *
  elif operator == "*":
    # maka bil1 * bil2
    ret = bil1 * bil2
  # jika parameter operator tidak keduanya
  else:
    # maka bil1 + bil2
    ret = bil1 + bil2
  # Return ret
  return print(ret)



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()