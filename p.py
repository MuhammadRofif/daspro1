#Membuat program kasir sederhana yang terdapat pembeli dan admin
nama_rubik = ["rubik 2x2", "rubik 3x3", "rubik 4x4", "rubik 5x5", "rubik 6x6"]
kode = [1, 2, 3, 4, 5]
harga_rubik = [10000, 30000, 50000, 70000, 90000]
A = False
#login sebagai pengguna /pengelola jika pengguna maka  melanjutkan program yang dibawah jika pengelola dilanjutkan ke baris no 68
while not A: 
    a = input("Login sebagai pengguna/pengelola? : ")
    if a == "pengguna":
        a1 = input("Nama : ")
        b1 = int(input("Pin : "))
        while not b1 == 23:
            print("\nPin salah!")
            b1 = int(input("Pin : "))
        else:
            B = False
            while not B:
                print("-------------------------------------------------------")
                print("              Rubik STORE             ")
                print("-------------------------------------------------------")
                print("No  Kode:    Nama Rubik:             Harga:      ")
                print("{}".format(kode[0]),"   1        {}".format(nama_rubik[0]),"          Rp. {}".format(harga_rubik[0]))
                print("{}".format(kode[1]),"   2        {}".format(nama_rubik[1]),"          Rp. {}".format(harga_rubik[1]))
                print("{}".format(kode[2]),"   3        {}".format(nama_rubik[2]),"          Rp. {}".format(harga_rubik[2]))
                print("{}".format(kode[3]),"   4        {}".format(nama_rubik[3]),"          Rp. {}".format(harga_rubik[3]))
                print("{}".format(kode[4]),"   5        {}".format(nama_rubik[4]),"          Rp. {}".format(harga_rubik[4]))
                print("=======================================================")
                

                no = int(input("No : "))
                x = 0
                total = []
                while x < no:
                    kode_produk = int((input("Kode : ")))
                    jumlah_produk = int(input("Jumlah pesanan : "))
                    x += 3
    
                    y = kode_produk
                    if y == kode[0]:
                        total.append(jumlah_produk*harga_rubik[0])
                        total0 = jumlah_produk*harga_rubik[0]
                        print("Total harga keseluruhan barang   : Rp.", total0)
                    elif y == kode[1]:
                        total.append(jumlah_produk*harga_rubik[1])
                        total1 = jumlah_produk*harga_rubik[1]
                        print("Total harga keseluruhan barang   : Rp.", total1)
                    elif y == kode[2]:
                        total.append(jumlah_produk*harga_rubik[2])
                        total2 = jumlah_produk*harga_rubik[2]
                        print("Total harga keseluruhan barang   : Rp.", total2)
                    elif y == kode[3]:
                        total.append(jumlah_produk*harga_rubik[3])
                        total3 = jumlah_produk*harga_rubik[3]
                        print("Total harga keseluruhan barang   : Rp.", total3)
                    elif y == kode[4]:
                        total.append(jumlah_produk*harga_rubik[4])
                        total4= jumlah_produk*harga_rubik[4]
                        print("Total harga keseluruhan barang   : Rp.", total4)
                        #jika y maka akan memesan lagi,jika tidak akan kembali ke menu login karena mengimplementasi dari a true maka kemenu 
                    menu = input(" Mau pesan lagi? pilih Y jika Ya, pilih T jika Tidak {Y}/{T} = ")
                if menu == "T" or menu == "t":
                    B = True
                else:
                    A = True      
    elif a == "pengelola":
        a1 = input("Nama : ")
        b1 = input("Pin : ")
        while not b1 == "14":
            print("\nPin salah!")
            b1 = input("Pin : ")
        else:
            print("Silahkan memilih menu berikut : ")
            print("\n[1]. Menu CRUD", "\n[2]. Kembali ke menu kasir", "\n[3]. Keluar")
            abc = int(input("Pilih (1/2/3): "))
            
            if abc == 3:
                print("Silahkan Login")
            
            elif abc == 2:
                print("\nLogin sebagai pengguna untuk kembali ke menu kasir\n")
            
            elif abc == 1:
                no = False
                while not no:
                    print("Pilih perintah yang anda inginkan?")
                    print("\n[1]. CREATE(Menambah Data)", "\n[2]. READ(Menampilkan Data)", "\n[3]. UPDATE(Mengubah /Mengedit Data)", "\n[4]. DELETE(Menghapus Data")
                    pilihan = int(input("Masukkan pilihan : "))
                    if pilihan == 1:
                        nama_rubik.append(str(input("Masukan nama/jenis rubik : ")))
                        print(nama_rubik)
                        kode.append(str(input("Masukan kode rubik : ")))
                        print(kode)
                        harga_rubik.append(str(input("Masukan harga rubik : ")))
                        print(harga_rubik)
                        print("\n----- Nama berhasil di tambahkan -----\n")
                    
                    elif pilihan ==2:
                        print("No  Kode:    Nama Rubik:             Harga:      ")
                        print("{}".format(kode[0]),"   1        {}".format(nama_rubik[0]),"          Rp. {}".format(harga_rubik[0]))
                        print("{}".format(kode[1]),"   2        {}".format(nama_rubik[1]),"          Rp. {}".format(harga_rubik[1]))
                        print("{}".format(kode[2]),"   3        {}".format(nama_rubik[2]),"          Rp. {}".format(harga_rubik[2]))
                        print("{}".format(kode[3]),"   4        {}".format(nama_rubik[3]),"          Rp. {}".format(harga_rubik[3]))
                        print("{}".format(kode[4]),"   5        {}".format(nama_rubik[4]),"          Rp. {}".format(harga_rubik[4]))
                        print("{}".format(kode[5]),"   6        {}".format(nama_rubik[5]),"          Rp. {}".format(harga_rubik[5]))
                                                            
                        print("\n----- Produk berhasil di Ditampilkan -----\n")
                    elif pilihan == 3:
                        ab = int(input("Banyak produk yang ingin diperbaharui/update namanya : "))
                        b = 0
                        while b < ab:
                            print("\nProduk ke -", b + 1)
                            print("Kode produk : ",kode)
                            dc = int(input("Masukkan kode produk yang ingin di perbaharui/update : "))
                            ubah_nama = (input("Ubah nama menjadi : "))
                            b += 1
                            if dc == kode[0]:
                                nama_rubik[0] = ubah_nama
                            elif dc == kode[1]:
                                nama_rubik[1] = ubah_nama
                            elif dc == kode[2]:
                                nama_rubik[2] = ubah_nama
                            elif dc == kode[3]:
                                nama_rubik[3] = ubah_nama
                            elif dc == kode[4]:
                                nama_rubik[4] = ubah_nama
                        print("\n----- Nama berhasil di update -----\n")
                    
                    elif pilihan == 4:
                        c = 0
                        bc = int(input("Banyak produk yang ingin di hapus dari daftar produk : "))  
                        while c < bc:
                            print("\nProduk ke -", c + 1)
                            print("Kode produk  : ",kode)
                            cd = int(input("Masukan kode produk yang ingin di hapus dari daftar produk : "))
                            c += 1
                            if cd == kode[0]:
                                kode[0] = "------"
                                nama_rubik[0] = "--------"
                                harga_rubik[0] = "-------"
                            
                            elif cd == kode[1]:
                                kode[1] = "------"
                                nama_rubik[1] = "--------"
                                harga_rubik[1] = "-------"
                            
                            elif cd == kode[2]:
                                kode[2] = "------"
                                nama_rubik[2] = "--------"
                                harga_rubik[2] = "-------"
                            
                            elif cd == kode[3]:
                                kode[3] = "------"
                                nama_rubik[3] = "--------"
                                harga_rubik[3] = "-------"
                            elif cd == kode[4]:
                                kode[4] = "------"
                                nama_rubik[4] = "-------------"
                                harga_rubik[4] = "-------"
                                print("\n----- Produk berhasil di hapus -----\n")
                    
                    menu = input("Apakah ingin kembali ke menu awal?pilih Y jika Ya, pilih T jika Tidak {Y}/{T} : ")
                    if menu == "T" or menu == "t":
                        no = True
                    else:
                        no = False
                            
                    
                    