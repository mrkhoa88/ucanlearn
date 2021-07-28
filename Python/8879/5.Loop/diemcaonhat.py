
#Tim trong list diem cao nhat nhung khong su dung ham MAX

print("Chuong trinh tinh diem cao nhat")

ds_diem = input("Nhap vao danh sach diem, cach nhau dau khoang cach").split()

for n in range(0, len(ds_diem)):
    ds_diem[n] = int(ds_diem[n])

diem_cao_nhat = 0

for diem in ds_diem:
    if diem > diem_cao_nhat:
        diem_cao_nhat = diem

print(f"Diem cao nhat la: {diem_cao_nhat}")