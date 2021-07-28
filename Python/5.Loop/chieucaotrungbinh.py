
print("Chuong trinh tinh chieu cao trung binh")

#Nhap vao mot list chieu cao
#Tinh tong chieu cao trong list
#Dem so item trong list
# chieucao_tb = tong_chieucao / tong_sv -> lam tron 2 chu so.


chieucao_sv = input("Nhap vao danh sach chieu cao, canh nhau khoang trang:").split()

for n in range(0, len(chieucao_sv)):
    chieucao_sv[n] = int(chieucao_sv[n])

tong_chieucao = 0

for chieucao in chieucao_sv:
    tong_chieucao += chieucao

print(f"Tong chieu cao la: {tong_chieucao}")

tong_sv = 0

for sv in chieucao_sv:
    tong_sv += 1
print(f"Tong so sinh vien = {tong_sv}")

chieucao_tb = round((tong_chieucao/tong_sv),2)
print(f"Chieu cao trung binh la: {chieucao_tb}")