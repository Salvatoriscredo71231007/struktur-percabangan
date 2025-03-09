#Latihan 5.1
def cek_angka(a, b, c):
  if a == b or a == c or b == c:
    return False
  elif (a + b == c) or (a + c == b) or (b + c == a):
    return True
  else:
    return False

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

hasil = cek_angka(a, b, c)
print(f"Hasil: {hasil}")

#Latihan 5.2
def cek_digit_belakang(a, b, c):
  return (a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c % 10)
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))
hasil = cek_digit_belakang(a, b, c)
print(f"Hasil: {hasil}")

#Latihan 5.3
celcius_to_fahrenheit = lambda c: (9/5) * c + 32
celcius_to_reamur = lambda c: 0.8 * c

c1 = 100
f1 = celcius_to_fahrenheit(c1)
print(f"Input C = {c1}. Output F = {f1}")
c2 = 80
r2 = celcius_to_reamur(c2)
print(f"Input C = {c2}. Output R = {r2}")
c3 = 0
f3 = celcius_to_fahrenheit(c3)
print(f"Input C = {c3}. Output F = {f3}")