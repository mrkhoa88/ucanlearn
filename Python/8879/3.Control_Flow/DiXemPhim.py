
print("Chao mung ban den voi chuong trinh mua ve xem phim")

chieucao = float(input("Moi ban nhap chieu cao: "))
bill = 0
if chieucao >= 120:
    print("Ban duoc di xem phim!")
    tuoi = int(input("Moi nhap so tuoi: "))
    if tuoi < 12:
        bill = 5
        print("Gia ve $5.")
    elif tuoi <= 18:
        bill = 7
        print("Gia ve $7.")
    elif tuoi >= 45 and tuoi <= 55:
        print("Mien phi gia ve.")
    else:
        bill = 12
        print("Gia ve $12.")
    chuphinh = input("Ban co muon chup hinh khong? Y/N: ")
    if chuphinh == "Y":
        bill += 3
    print(f"Tong tien phai tra la: {bill}")
else:
    print("Sorry, ban khong duoc xem phim cua nguoi lon!")

