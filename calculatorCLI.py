print("Calculator CLI")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Pembagian")
print("4. Perkalian")

print("-------------")

#logika 

def penjumlahan(x,y):
    return x+y
    
def pengurangan(x,y):
    return x-y
    
def pembagian(x,y):
    return x/y
    
def perkalian(x,y):
    return x*y

fitur_cal = input("Pilih Sesuai Kebutuhan : ")
 
if fitur_cal in ('1', '2', '3', '4'):
   num1 = float(input("Masukan angka 1 : "))
   num2 = float(input("Masukan angka 2 : ")) 
print("---------")
    
if fitur_cal == '1':
    print("Hasil : ", penjumlahan(num1, num2))
elif fitur_cal == '2':
    print("Hasil kurang : ", pengurangan(num1, num2))
elif fitur_cal == '3':
    print("Hasil : ", pembagian(num1, num2))
elif fitur_cal == '4':
    print("hasil : ", perkalian(num1, num2))
    
print("program selesai, terimakasih supportnya")
