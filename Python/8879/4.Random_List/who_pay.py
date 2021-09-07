import random

print("Chao mung ban den voi chuong trinh Ai Se Tra Tien")

name_string = input("Nhap vao danh sach nguoi an, cach nhau boi dau phay: ")
names = name_string.split(", ")

num_item = len(names)
print(names)
luachon = random.randint(0, num_item - 1)
nguoi_se_tra_tien = names[luachon]

print(nguoi_se_tra_tien + " Se tra tien cho bua tiec hom nay!!!!")