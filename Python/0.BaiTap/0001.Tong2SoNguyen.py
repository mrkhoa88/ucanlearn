
# Chuong trinh tinh tong 2 so va xu ly ngoai le khi dau vao nhap khong dung kieu du lieu

so1 = input("Moi nhap so thu 1: ")
so2 = input("Moi nhap so thu 2: ")

try:
    so1 = int(so1)
    so2 = int(so2)
    tong = so1 + so2
    print(f"Tong 2 so la: {tong}")
except:
    print("Dinh dang dau vao khong hop le")

print('Tong', 'hai', 'so', 'la:',tong, sep='--')