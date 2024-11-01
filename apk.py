import random

def tampilkan_identitas_program():
    print("=" * 80)
    print(r"   _____  _____  __  __  _    _  _                  _____  _____ ")
    print(r"  / ____||_   _||  \/  || |  | || |         /\     / ____||_   _|")
    print(r" | (___    | |  | \  / || |  | || |        /  \   | (___    | |  ")
    print(r"  \___ \   | |  | |\/| || |  | || |       / /\ \   \___ \   | |  ")
    print(r"  ____) | _| |_ | |  | || |__| || |____  / ____ \  ____) | _| |_ ")
    print(r" |_____/ |_____||_| _|_|_\____/ |______|/_/    \_\|_____/ |_____|")
    print(r"  / ____|    /\    / ____|| |  | |    /\                         ")
    print(r" | |  __    /  \  | |     | |__| |   /  \                        ")
    print(r" | | |_ |  / /\ \ | |     |  __  |  / /\ \                       ")
    print(r" | |__| | / ____ \| |____ | |  | | / ____ \                      ")
    print(r"  \_____|/_/____\_\\_____||_|__|_|/_/    \_\ __ _    _  _   _    ")
    print(r"     /\    |  __ \ |_   _| / ____|       | |/ /| |  | || \ | |   ")
    print(r"    /  \   | |__) |  | |  | (___  ______ | ' / | |  | ||  \| |   ")
    print(r"   / /\ \  |  _  /   | |   \___ \|______||  <  | |  | || . ` |   ")
    print(r"  / ____ \ | | \ \  _| |_  ____) |       | . \ | |__| || |\  |   ")
    print(r" /_/    \_\|_|  \_\|_____||_____/        |_|\_\ \____/ |_| \_|   ")
    print("                                                                  ")
    print("=" * 80)
    print("Selamat datang di Simulasi Gacha Aris-Kun!")
    print("Dapatkan karakter dengan melakukan gacha menggunakan gems.")
    print("=" * 80)

kurs_konversi = 5000
harga_gacha = 50    

pengguna = {
    "saldo": 0,
    "gems": 0
}

daftar_karakter = [
    "Paijo", "Paimin", "Sukinem", "Siti", "Parno",
    "Muhammad", "Nur", "Slamet", "Sadikin", "Adi"
]

def tampilkan_saldo():
    print(f"Saldo Anda: Rp {pengguna['saldo']}")

def tampilkan_gems():
    print(f"Gems Anda: {pengguna['gems']} gems")

def tambah_saldo():
    print("\n--- Pilih Nominal Top-up ---")
    print("1. Rp 100,000")
    print("2. Rp 200,000")
    print("3. Rp 500,000")
    print("4. Rp 1,000,000")
    print("5. Masukkan Nominal Lain")
    print("0. Kembali")

    pilihan = input("Pilih nominal (0-5): ")
    
    if pilihan == "1":
        jumlah = 100000
    elif pilihan == "2":
        jumlah = 200000
    elif pilihan == "3":
        jumlah = 500000
    elif pilihan == "4":
        jumlah = 1000000
    elif pilihan == "5":
        try:
            jumlah = int(input("Masukkan jumlah saldo yang ingin ditambahkan (Rp): "))
            if jumlah <= 0:
                print("Nominal harus lebih dari 0.")
                return
        except ValueError:
            print("Nominal tidak valid.")
            return
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid.")
        return
    
    pengguna["saldo"] += jumlah
    print(f"Saldo berhasil ditambahkan sebesar Rp {jumlah}.")
    tampilkan_saldo()


def beli_gems():
    print("\n--- Pilih Jumlah Gems ---")
    print("1. 5 Gems (Rp 25,000)")  
    print("2. 10 Gems (Rp 50,000)") 
    print("3. 20 Gems (Rp 100,000)")
    print("4. 50 Gems (Rp 250,000)")
    print("5. Masukkan Jumlah Gems Lain")
    print("0. Kembali")

    pilihan = input("Pilih jumlah gems (0-5): ")
    
    if pilihan == "1":
        jumlah_gems = 5
    elif pilihan == "2":
        jumlah_gems = 10
    elif pilihan == "3":
        jumlah_gems = 20
    elif pilihan == "4":
        jumlah_gems = 50
    elif pilihan == "5":
        try:
            jumlah_gems = int(input("Masukkan jumlah gems yang ingin dibeli: "))
            if jumlah_gems <= 0:
                print("Jumlah gems harus lebih dari 0.")
                return
        except ValueError:
            print("Jumlah gems tidak valid.")
            return
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid.")
        return
    
    biaya = jumlah_gems * kurs_konversi
    if pengguna["saldo"] >= biaya:
        pengguna["saldo"] -= biaya
        pengguna["gems"] += jumlah_gems
        print(f"Berhasil membeli {jumlah_gems} gems seharga Rp {biaya}.")
    else:
        print("Saldo tidak mencukupi untuk membeli gems.")
    tampilkan_saldo()
    tampilkan_gems()

def lakukan_gacha():
    print("\n--- Pilih Jumlah Spin ---")
    print("Pilih salah satu opsi di bawah ini untuk melakukan spin:")
    print("1. 10x Spin (sekali) - Biaya: Rp", harga_gacha * 10 * kurs_konversi)
    print("2. 10x Spin (dua kali) - Biaya: Rp", harga_gacha * 10 * 2 * kurs_konversi)
    print("3. 10x Spin (tiga kali) - Biaya: Rp", harga_gacha * 10 * 3 * kurs_konversi)
    print("4. 1x Spin (sepuluh kali) - Biaya: Rp", harga_gacha * 1 * 10 * kurs_konversi)
    print("0. Kembali - Kembali ke menu sebelumnya.")

    pilihan = input("Pilih tipe spin (0-4): ")
    
    if pilihan == "1":
        jumlah_spin = 10
        frekuensi = 1
    elif pilihan == "2":
        jumlah_spin = 10
        frekuensi = 2
    elif pilihan == "3":
        jumlah_spin = 10
        frekuensi = 3
    elif pilihan == "4":
        jumlah_spin = 1
        frekuensi = 10
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid. Silakan pilih angka dari 0 hingga 4.")
        return
    
    total_biaya = jumlah_spin * frekuensi * harga_gacha
    if pengguna["gems"] >= total_biaya:
        pengguna["gems"] -= total_biaya
        print(f"\nMelakukan Spin {jumlah_spin} karakter sebanyak {frekuensi} kali...")
        for i in range(frekuensi):
            print(f"\nSpin {i + 1} dari {frekuensi}:")
            for _ in range(jumlah_spin):
                karakter = random.choice(daftar_karakter)
                print(f"  - Anda mendapatkan karakter: {karakter}")
        print(f"\nTotal gems yang digunakan: {total_biaya}")
    else:
        print("Gems tidak mencukupi untuk melakukan spin.")
    
    tampilkan_gems()

def menu_utama():
    tampilkan_identitas_program()
    
    while True:
        print("\n--- Menu Utama ---")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Beli Gems")
        print("4. Lihat Gems")
        print("5. Lakukan Gacha")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            tampilkan_saldo()
        elif pilihan == "2":
            tambah_saldo()
        elif pilihan == "3":
            beli_gems()
        elif pilihan == "4":
            tampilkan_gems()
        elif pilihan == "5":
            lakukan_gacha()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan Simulasi Gacha Aris-Kun!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

menu_utama()