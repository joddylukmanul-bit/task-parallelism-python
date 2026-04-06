from concurrent.futures import ThreadPoolExecutor
import time

data_nilai = [78, 85, 90, 66, 88, 92, 74, 81, 69, 95]

# Task 1: Hitung rata-rata
def hitung_rata():
    print("Task 1: Menghitung rata-rata...")
    time.sleep(2)
    rata = sum(data_nilai) / len(data_nilai)
    print("Task 1 selesai: Rata-rata =", rata)
    return rata

# Task 2: Cari nilai tertinggi
def nilai_tertinggi():
    print("Task 2: Mencari nilai tertinggi...")
    time.sleep(1)
    maks = max(data_nilai)
    print("Task 2 selesai: Nilai tertinggi =", maks)
    return maks

# Task 3: Klasifikasi lulus/tidak
def klasifikasi():
    print("Task 3: Mengklasifikasi kelulusan...")
    time.sleep(3)
    lulus = [n for n in data_nilai if n >= 75]
    tidak_lulus = [n for n in data_nilai if n < 75]
    print("Task 3 selesai")
    return (lulus, tidak_lulus)

# Task 4: Simulasi simpan data
def simpan_data():
    print("Task 4: Menyimpan data ke database...")
    time.sleep(4)
    print("Task 4 selesai: Data tersimpan")
    return "Sukses"

def main():
    print("=== PROGRAM ANALISIS NILAI (PARALEL) ===\n")

    with ThreadPoolExecutor(max_workers=4) as executor:
        f1 = executor.submit(hitung_rata)
        f2 = executor.submit(nilai_tertinggi)
        f3 = executor.submit(klasifikasi)
        f4 = executor.submit(simpan_data)

        hasil1 = f1.result()
        hasil2 = f2.result()
        hasil3 = f3.result()
        hasil4 = f4.result()

    print("\n=== SEMUA TASK SELESAI ===")
    print("Rata-rata:", hasil1)
    print("Nilai tertinggi:", hasil2)
    print("Lulus:", hasil3[0])
    print("Tidak lulus:", hasil3[1])
    print("Status simpan:", hasil4)

if __name__ == "__main__":
    main()