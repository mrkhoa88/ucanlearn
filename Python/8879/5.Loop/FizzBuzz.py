#Cho danh sach so tu 1-100
#Neu so chia het cho 3 thi in ra Fizz
#Neu so chia het cho 5 thi in ra Buzz
#Neu so chia het cho 3 & 5 thi in ra FizzBuzz

print("Chao mung den voi chuong trinh FizzBuzz")

for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)