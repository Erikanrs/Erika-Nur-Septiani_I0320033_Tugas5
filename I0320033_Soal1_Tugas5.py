# menyapa pengunjung hotel

print('=======HOTEL APAYA=======')
print('Mohon lengkapi biodata anda:')

nama = input('Masukan nama anda:')

print('1. Wanita')
print('2. Pria')

jeniskelamin = input('pilihlah jenis kelamin anda:')

if jeniskelamin == "1":
    print('Selamat datang, Nyonya', nama , '!')
else jeniskelamin == "2":
    print('Selamat datang, Tuan', nama ,'!')
print()