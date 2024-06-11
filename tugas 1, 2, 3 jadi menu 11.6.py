def menu_utama():
    while True:
        print("\nSistem Manajemen Transaksi")
        print("1. Tugas 1 Data mahasiswa")
        print("2. Tugas 2 Inventaris barang")
        print("3. Tugas 3 Pengelolaan keuangan")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            def input_data_mahasiswa():
                mahasiswa_list = []
                n = int(input("masukan jumlah mahasiswa: "))
                
                for i in range(n):
                    print(f"\nMasukan data mahasiswa ke-{i+1}:\n")
                    nama = input("Nama: ")
                    nim = input("NIM: ")
                    nilai1 = float(input("Nilai ke-1: "))
                    nilai2 = float(input("Nilai ke-2: "))
                    nilai3 = float(input("Nilai ke-3: "))
                    nilai4 = float(input("Nilai ke-4: "))
                    mahasiswa = {
                        "nama": nama,
                        "nim": nim,
                        "nilai ke-1":nilai1,
                        "nilai ke-2":nilai2,
                        "nilai ke-3":nilai3,
                        "nilai ke-4":nilai4,
                    }
                    mahasiswa_list.append(mahasiswa)
                    
                return mahasiswa_list

            def tampilkan_data_mahasiswa(mahasiswa_list):
                for i, mahasiswa in enumerate(mahasiswa_list):
                    rata_rata = (mahasiswa['nilai ke-1'] + mahasiswa['nilai ke-2'] + mahasiswa['nilai ke-3'] + mahasiswa['nilai ke-4']) / 4
                    print(f"Mahasiswa ke-{i+1};")
                    print(f"Nama        : {mahasiswa['nama']}")
                    print(f"Nim         : {mahasiswa['nim']}")
                    print(f"Rata-rata  : {rata_rata:.2f}")
                    
            def cari_nilai_tertinggi_terendah(mahasiswa_list):
                rata_rata_tertinggi = None
                rata_rata_terendah = None
                mahasiswa_tertinggi = None
                mahasiswa_terendah = None
                
                for mahasiswa in mahasiswa_list:
                    rata_rata = (mahasiswa['nilai ke-1'] + mahasiswa['nilai ke-2'] + mahasiswa['nilai ke-3'] + mahasiswa['nilai ke-4']) / 4
                    
                    if rata_rata_tertinggi is None or rata_rata > rata_rata_tertinggi:
                        rata_rata_tertinggi = rata_rata
                        mahasiswa_tertinggi = mahasiswa
                    
                    if rata_rata_terendah is None or rata_rata < rata_rata_terendah:
                        rata_rata_terendah = rata_rata
                        mahasiswa_terendah = mahasiswa
                
                print("Mahasiswa dengan rata-rata nilai tertinggi:")
                print(f"Nama       : {mahasiswa_tertinggi['nama']}")
                print(f"NIM        : {mahasiswa_tertinggi['nim']}")
                print(f"Rata-rata  : {rata_rata_tertinggi:.2f}")
                
                print("Mahasiswa dengan rata-rata nilai terendah:")
                print(f"Nama       : {mahasiswa_terendah['nama']}")
                print(f"NIM        : {mahasiswa_terendah['nim']}")
                print(f"Rata-rata  : {rata_rata_terendah:.2f}")
                    
            mahasiswa_list = input_data_mahasiswa()
            print("\n")
            print("                  Menampilkan Data ")
            print("========================================================")
            print("\n")
            tampilkan_data_mahasiswa(mahasiswa_list)
            print("\n")
            cari_nilai_tertinggi_terendah(mahasiswa_list)
            break
            
        elif pilihan == '2':
            inventory = []

            def input_barang():
                nama = input("Masukkan nama barang: ")
                kode = input("Masukkan kode barang: ")
                barang = {"nama": nama,
                        "kode": kode
                        }
                inventory.append(barang)
                print("Barang berhasil ditambahkan!")

            def tampilkan_barang():
                if not inventory:
                    print("Tidak ada barang dalam inventaris.")
                else:
                    for barang in inventory:
                        print(f"Nama: {barang['nama']}, Kode: {barang['kode']}")

            def cari_barang():
                kode = input("Masukkan kode barang yang dicari: ")
                for barang in inventory:
                    if barang['kode'] == kode:
                        print(f"Nama: {barang['nama']}, Kode: {barang['kode']}")
                        return
                print("Barang tidak ditemukan.")

            def hapus_barang():
                kode = input("Masukkan kode barang yang ingin dihapus: ")
                for barang in inventory:
                    if barang['kode'] == kode:
                        inventory.remove(barang)
                        print("Barang berhasil dihapus!")
                        return
                print("Barang tidak ditemukan.")

            def main():
                while True:
                    print("\nSistem Manajemen Inventaris")
                    print("1. Tambah Barang")
                    print("2. Tampilkan Semua Barang")
                    print("3. Cari Barang")
                    print("4. Hapus Barang")
                    print("5. Keluar")
                    pilihan = input("Masukkan pilihan Anda: ")
                    
                    if pilihan == '1':
                        input_barang()
                    elif pilihan == '2':
                        tampilkan_barang()
                    elif pilihan == '3':
                        cari_barang()
                    elif pilihan == '4':
                        hapus_barang()
                    elif pilihan == '5':
                        print("Keluar dari program.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

            if __name__ == "__main__":
                main()
            break
        
        elif pilihan == '3':
            transaksi = []

            def input_transaksi():
                jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
                if jenis not in ['pemasukan', 'pengeluaran']:
                    print("Jenis transaksi tidak valid. Masukkan 'pemasukan' atau 'pengeluaran'.")
                    return
                jumlah = float(input("Masukkan jumlah transaksi: "))
                transaksi.append({'jenis': jenis, 'jumlah': jumlah})
                print("Transaksi berhasil ditambahkan!")

            def tampilkan_transaksi():
                if not transaksi:
                    print("Tidak ada transaksi.")
                else:
                    for t in transaksi:
                        print(f"Jenis: {t['jenis'].capitalize()}, Jumlah: {t['jumlah']}")

            def total_pemasukan():
                total = sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pemasukan')
                print(f"Total Pemasukan: {total}")

            def total_pengeluaran():
                total = sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pengeluaran')
                print(f"Total Pengeluaran: {total}")

            def saldo_akhir():
                pemasukan = sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pemasukan')
                pengeluaran = sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pengeluaran')
                saldo = pemasukan - pengeluaran
                print(f"Saldo Akhir: {saldo}")

            def main():
                while True:
                    print("\nSistem Manajemen Transaksi")
                    print("1. Tambah Transaksi")
                    print("2. Tampilkan Semua Transaksi")
                    print("3. Tampilkan Total Pemasukan")
                    print("4. Tampilkan Total Pengeluaran")
                    print("5. Tampilkan Saldo Akhir")
                    print("6. Keluar")
                    pilihan = input("Masukkan pilihan Anda: ")
                    
                    if pilihan == '1':
                        input_transaksi()
                    elif pilihan == '2':
                        tampilkan_transaksi()
                    elif pilihan == '3':
                        total_pemasukan()
                    elif pilihan == '4':
                        total_pengeluaran()
                    elif pilihan == '5':
                        saldo_akhir()
                    elif pilihan == '6':
                        print("Keluar dari program.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

            if __name__ == "__main__":
                main()
            break

        elif pilihan == '4':
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


menu_utama()