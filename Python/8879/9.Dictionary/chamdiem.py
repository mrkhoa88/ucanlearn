
#tao mot dic diem_sv

diem_sv = {
    "khoa": 81,
    "nga": 78,
    "ngoc": 99,
    "triet": 62,
    "tra": 88

}

#tao mot dic chamdiem
chamdiem = {}

for sv in diem_sv:
    diem = diem_sv[sv]
    if diem > 90:
        chamdiem[sv] = "Xuat sac"
    elif diem > 80:
        chamdiem[sv] = "Gioi"
    elif diem > 70: 
        chamdiem[sv] = "Kha"
    else:
        chamdiem[sv] = "Rot"

print(chamdiem)

