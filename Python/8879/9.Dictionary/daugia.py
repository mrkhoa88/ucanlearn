
#Nhap ten + gia vao dictionary
#Hoi xem co tiep khong, neu ko thi in ra gia cao nhat, neu co thi nhap tiep
#tim gia cao nhat trong dic


from art import logo

import os
def cls():
    os.system("clear")


print(logo)

#Nhap ten va gia

daugia = {}
daugia_xong = False

def tim_gia_cao_nhat(giatien):
    gia_cao_nhat = 0
    nguoi_thang = ""
    #giatien = {"Khoa": 123, "Nga":456,"Ngoc":789}
    for nguoi in giatien:
        gia_dau = giatien[nguoi]
        if gia_dau > gia_cao_nhat:
            gia_cao_nhat = gia_dau
            nguoi_thang = nguoi
    print(f"Nguoi chien thang la: {nguoi_thang} voi gia tien: {gia_cao_nhat} dong")

        

while not daugia_xong:
    ten = input("Moi nhap ten: ")
    gia = int(input("Moi nhap gia: "))
    daugia[ten] = gia
    tieptuc = input("Co them nguoi nao nua khong? 'C' hoac 'K': ").lower()

    if tieptuc == "k":
        daugia_xong = True
        tim_gia_cao_nhat(daugia)
    elif tieptuc == "c":
        cls()



