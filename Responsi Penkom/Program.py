import os
import time
from prettytable import PrettyTable
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def ulang():
    print("==============================================")
    print('Gunakan Program Agroindustri Lagi? (Ya/Tidak)')
    ulang=input().lower()
    if ulang == "Ya" or ulang == "ya":
        os.system('cls')
        print("==========================")
        print('Pilih Basah atau Kering: ')
        memilih = input().lower()
        if memilih =='Basah' or memilih == 'basah' or memilih == 1:
            basah()
        if memilih =='kering' or memilih == 'kering' or memilih == 2:
            kering()
    else :
        os.system('cls')
        print('Terima Kasih!!!!!')
        print('Program Akan Keluar Dalam 3 Detik...')
        time.sleep(3)
        os.system('cls')
        while ulang != 'Basah' or ulang != 'basah' or ulang != 'Kering' or ulang != 'kering':
            break

def login():
    print("==================================================================")
    print('||\tSelamat Datang Di Program Penghitungan Agroindustri\t||')
    print("==================================================================")
    print('||\t      Silahkan Pilih Opsi Penghitungan Berikut: \t||')
    print("==================================================================")
    print('||\t\t\t  1. Basah\t\t\t\t||')
    print('||\t\t\t  2. Kering\t\t\t\t||')
    global masuk
    print("==================================================================")
    masuk = int(input('Masukkan Opsi Pilihan (1/2): '))
    os.system('cls')
login()

def basah():
    os.system('cls')
    def lagi1():
        print('Menu Sebelumnya? (Ya/Tidak)')
        lagi=input().lower()
        if lagi == "Ya" or lagi == "ya":
            os.system('cls')
            basah()
        elif lagi == "Tidak" or lagi == 'tidak' :
            def stop():
                while lagi == 'Tidak' or lagi == 'tidak':
                    break
            print("===============================================")
            stop()
            os.system('cls')
            ulang()
        else:
            os.system('cls')
            print("===============================================")
            print("Masukkan Input yang Benar !!!")
            lagi1()
    if masuk == 1:
        print("=======================================")
        print('||\t1. Indeks Berat Badan\t     ||')
        print('||\t2. Indeks Jumlah Kalori\t     ||')
        print("=======================================")
        opsi = int(input('Masukkan Opsi Pilihan (1/2): '))
        os.system('cls')

        if opsi == 1:
            print("===============================================")
            berat, tinggi = (
            float(input("Masukkan Berat Badan dalam Kilogram (kg): ")),
            float(input("Masukkan Tinggi dalam Meter Kuadrat (m)^2: "))  
            )
            print("===============================================")

            def hitung_BMI():
                return berat/tinggi
            print("Hasil BMI : ", round(hitung_BMI(), 1))

            def definisi():
                BMI = float(hitung_BMI())
                if 18.5<= BMI <=25 :
                    print("Anda Memiliki Berat Ideal")
                    print("===============================================")
                elif BMI < 18.5 :
                    print("Anda Kekurangan Berat Badan")
                    print("===============================================")
                elif BMI > 25 :
                    print("Anda Kelebihan Berat Badan")
                    print("===============================================")
            definisi()
            lagi1()

        if opsi == 2:
            print("=================================")
            print('1. Karbohidrat')
            print('2. Lemak')
            print('3. Protein')
            print('4. Kalori Ideal')
            print("=================================")
            proksimat = int(input('Masukkan Opsi Pilihan (1/2/3/4): '))
            os.system('cls')

            if proksimat == 1:
                def karbo():
                    print("=======================================")
                    gram_karbo = (
                    int(input('Masukkan Nilai Gram Karbohidrat: ')))
                    print("=======================================")
                    if gram_karbo > 0:
                        def hitung_karbo(gram_karbo):
                            return gram_karbo * 4
                        print("Kalori Dari Karbohidrat = ", hitung_karbo(gram_karbo))
                        print("=======================================")
                        lagi1()
                    else:
                        print('Masukkan Nilai Lebih dari 0')
                        karbo()
                karbo()
            if proksimat == 2:
                def lemak():
                    print("=======================================")
                    gram_lemak = (
                    int(input('Masukkan Nilai Gram Lemak: ')))
                    print("=======================================")
                    if gram_lemak > 0:
                        def hitung_lemak(gram_lemak):
                            return gram_lemak * 9
                        print("Kalori Dari Lemak = ", hitung_lemak(gram_lemak))
                        print("=======================================")
                        lagi1()
                    else:
                        print('Masukkan Nilai Lebih dari 0')
                        lemak()
                lemak()
            if proksimat == 3:
                def protein():
                    print("=======================================")
                    gram_protein = (
                    int(input('Masukkan Nilai Gram Protein: ')))
                    print("=======================================")
                    if gram_protein > 0:
                        def hitung_protein(gram_protein):
                            return gram_protein * 4
                        print("Kalori Dari Protein = ", hitung_protein(gram_protein))
                        print("=======================================")
                        lagi1()
                    else:
                        print('Masukkan Nilai Lebih dari 0')
                        protein()
                protein()
            if proksimat == 4:
                def saran_menu():
                    print("========================================================")
                    berat = float(input('Berat Badan Anda (dalam kg): '))
                    if berat > 0:
                        tinggi = float(input('Tinggi Badan Anda (dalam cm): '))
                        if tinggi > 0:
                            umur = float(input('Usia Anda (dalam tahun): '))
                            if umur > 0:
                                print("========================================================")
                                print('1. Tidak Pernah atau Sangat Jarang Olahraga')
                                print('2. Sedikit Aktif (Olahraga Ringan 1-3 hari seminggu)')
                                print('3. Cukup Aktif (Olahraga Sedang 3-5 hari seminggu)')
                                print('4. Sangat Aktif (Olahraga Berat 6-7 hari seminggu)')
                                print('5. Ekstra Aktif (Olahraga Sangat Berat 6-7 hari seminggu)')
                                print("========================================================")
                                aktif = int(input('Tingkat Aktivitas Anda (1/2/3/4/5): '))
                                if aktif > 0:
                                    if aktif == 1:
                                        aktivitas = 1.2
                                    if aktif == 2:
                                        aktivitas = 1.375
                                    if aktif == 3:
                                        aktivitas = 1.55
                                    if aktif == 4:
                                        aktivitas = 1.725
                                    if aktif == 5:
                                        aktivitas = 1.9
                                    
                                    if aktivitas > 0:
                                        gender = str(input('Jenis Kelamin Anda? (L/P) '))
                                        print("=========================================================")
                                        if gender == 'L' or gender == 'l':
                                            BMR = ((88.362) + (13.397 * berat) + (4.799 * tinggi) - (5.677 * umur)) * (aktivitas)
                                            print('Jumlah Kalori Ideal yang Anda Konsumsi Adalah ' + str(round(BMR,1)))
                                            print("=========================================================")
                                            lagi1()
                                        else:
                                            BMR = int(((447.593) + (9.247 * berat) + (3.098 * tinggi) - (4.330 * umur)) * (aktivitas))
                                            print('Jumlah Kalori Ideal yang Anda Konsumsi Adalah ' + BMR)
                                            print("====================================================")
                                            lagi1()
                saran_menu()
            else:
                while proksimat != 1 or proksimat != 2 or proksimat != 3 or proksimat != 4:
                    break
basah()

def kering():
    def lagi2():
        print('Menu Sebelumnya? (Ya/Tidak)')
        lagi=input().lower()
        if lagi == "Ya" or lagi == "ya":
            os.system('cls')
            kering()
        elif lagi == "Tidak" or lagi == 'tidak' :
            def stop():
                while lagi == 'Tidak' or lagi == 'tidak':
                    break
            print("===============================================")
            stop()
            os.system('cls')
            ulang()
        else:
            os.system('cls')
            print("===============================================")
            print("Masukkan Input yang Benar !!!")
            lagi2()
    if masuk == 2:
        print('==================================================')
        print('||\t1. Kalkulator Total Belanja\t\t||')
        print('||\t2. Kalkulator Prediksi Regresi Linear\t||')
        print('==================================================')
        opsi = int(input('Masukkan Opsi Pilihan (1/2): '))
        print('==================================================')
        os.system('cls')

        if opsi == 1:
            def main():
                os.system('cls')
                hitung()
                restart()
            global Barang
            global Kuantitas
            global Harga
            global Diskon
            global Diskon_Sesungguhnya
            global Jumlah_Akhir
            Barang = []
            Kuantitas = []
            Harga = []
            Diskon = []
            Diskon_Sesungguhnya = []
            Jumlah_Akhir = []
            def hitung():
                print('==============================================')
                nama_barang = str(input('Masukkan Nama Barang: '))
                Barang.append(nama_barang)
                kuantitas_barang = int(input('Kuantitas: '))
                Kuantitas.append(kuantitas_barang)
                harga_barang = float(input('Harga: '))
                Harga.append(harga_barang)
                print('==============================================')
                jumlah_diskon = float(input('Persentase Diskon (Isikan 0 Bila Tidak Ada): '))
                if jumlah_diskon != 0:
                    Diskon.append(jumlah_diskon)
                    b = jumlah_diskon / 100
                    Diskon_Sesungguhnya.append(b)
                elif jumlah_diskon == 0:
                    Diskon.append('-')
                    b = 0 / 100
                    Diskon_Sesungguhnya.append(b)
                
            def restart():
                os.system('cls')
                print('========================================')
                restart=input(str("Apakah Anda Ingin Input Barang Lagi? : ").lower())
                if restart == "Ya" or restart == "ya":
                    main()
                else:
                    for i in range(len(Barang)):
                        my_list1= Kuantitas[i]*Harga[i]-(Kuantitas[i]*Harga[i]*Diskon_Sesungguhnya[i])
                        Jumlah_Akhir.append(my_list1)
                        global e
                        e = sum(Jumlah_Akhir)
                    table = PrettyTable(['Barang','Kuantitas','Harga','Diskon (%)','Total'])
                    for z in range(len(Kuantitas)):
                        table.add_row([Barang[z],Kuantitas[z],Harga[z],Diskon[z],Jumlah_Akhir[z]])
                    print(table)
                    print('========================================')
                    print('Jumlah Uang Yang Harus Anda Bayar: ', e)
                    print('========================================')
            main()
            lagi2()

        if opsi == 2:
            def utama():
                os.system('cls')
                regresi()
                ulangi()
            def regresi():
                print('========================================')
                data1 = pd.read_csv(input('File CSV Yang Akan Dianalisis: '))
                print('========================================')
                p = input('Variabel Independen: ')
                q = input('Variabel Dependen: ')
                print('========================================')
                x = data1[p]
                y = data1[q]
                plt.scatter(x,y)
                plt.title('Hubungan Dua Variabel')
                plt.xlabel(p)
                plt.ylabel(q)
                plt.show()
                o = data1[[p]]
                p = data1[[q]]
                model = LinearRegression().fit(o,p)
                a = model.intercept_
                b = model.coef_
                r = model.score(o,p)
                k = np.asarray(a, dtype='float64')
                l = np.asarray(b, dtype='float64')
                m = np.asarray(r, dtype='float64')
                j = float(input("Masukkan Data Ke-X: "))
                prediksi = (j * l) + k
                tampil = prediksi.flatten()
                kores = m.flatten()
                print('Koefisien R Kuadrat Sebesar ', kores)
                print('Perkiraan Pada Data Ke-X adalah', tampil)
                print('========================================')
                time.sleep(10)
            def ulangi():
                restart=input(str("Apakah Anda Ingin Analisis Lagi? : "))
                if restart == "Ya" or restart == "ya":
                    utama()
                else:
                    os.system('cls')
                    print('========================================')
            utama()
            lagi2()                   

kering()
        











