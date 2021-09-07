#Password Generator Project
import random
chu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
so = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dacbiet = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Chao mung ban den voi chuowng trinh tao 1 password random")

n_chu = int(input("Ban muon bao nhieu chu: "))
n_so = int(input("Ban muon bao nhieu so: "))
n_dacbiet = int(input("Ban muon bao nhieu ky tu dac biet: "))

password_list = []

for kt_chu in range(1, n_chu+1):
    password_list.append(random.choice(chu))

for kt_so in range(1, n_so+1):
    password_list.append(random.choice(so))

for kt_dacbiet in range(1, n_dacbiet+1):
    password_list.append(random.choice(dacbiet))

random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Mat khau cua ban la: {password}")
