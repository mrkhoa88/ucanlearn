
print("Chao mung ban den voi chuong trinh dat Pizza")
size = input("Ban muon banh size may? S,M, hoac L: ")
them_xucxich = input("Ban co muon them xuc xich khong? y or n: ")
them_phomai = input("Ban co muon them pho mai khong? y or n: ")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if them_xucxich == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if them_phomai == "y":
    bill += 1

print(f"Tong tien phai tra la: {bill}")