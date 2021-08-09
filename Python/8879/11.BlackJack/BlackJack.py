
# https://replit.com/@appbrewery/blackjack-final
#1. Viet mot ham chia bai gom bo bai, la bai va tra ve la bai
#2. Chia 2 la bai cua ban + cua may
#3. Viet ham tinh tong cac la bai trong list (cua ban + cua may)
    #+ neu la 2 la bai co tong = 21 return 0
    #+ neu 11 va tong > 21 thi remove 11, append lai 1
    #+ return bai
#Su dung while
#4. Neu diem cua ban = 0 va diem cua may = 0 va diem cua ban >21 ->ket thuc = True
    #in ra bai cua ban, tong diem
    #in ra la bai dau tien cua may
    # else: hoi xem co tiep tuc khong?
        #Neu y append them 1 la bai vao bai cua ban
        #else: ket thuc =  True
        #in ra bai + diem cua ban va cua may

#5. While diem cua may != 0 hoac diem cua may < 17 thi phai append them cho may

#6. Viet ham so sanh diem cua ban + diem cua may
    #=0 -> BlackJack, >21, hoa, >, <

#7. Gom tat ca vao mot ham choi_bai
#8. While co muon choi bai khong == 'y'

import random
import math
from art import logo
import os
def cls():
    os.system("clear")



def chia_bai():
    '''Chia bai tren ban'''
    bo_bai = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    bai = random.choice(bo_bai)
    return bai

def tinh_tong_the_bai(tong_bai):
    if sum(tong_bai) == 21 and len(tong_bai) == 2:
        return 0
    
    if 11 in tong_bai and sum(tong_bai) > 21:
        tong_bai.remove(11)
        tong_bai.append(1)    
    return sum(tong_bai)

def so_sanh(diem_ban,diem_may):
    if diem_ban > 21 and diem_may > 21:
        return "Ban thua vi vuot qua 21"
        
    if diem_ban == diem_may:
        return "Bai hoa"
    elif diem_ban == 0:
        return "Ban thang BlackJack"
    elif diem_may == 0:
        return "May thang BlackJack"
    elif diem_ban > 21:
        return "Vuot qua 21, Ban thua"
    elif diem_may > 21:
        return "vuot qua 21, May thua"
    elif diem_ban > diem_may:
        return "Diem ban > diem may. Ban Thang"
    else:
        return "Diem ban < diem may. Ban Thua"


def choi_bai():
    print(logo)
    bai_cua_ban = []
    bai_cua_may = []
    ket_thuc = False

    for _ in range(2):
        bai_cua_ban.append(chia_bai())
        bai_cua_may.append(chia_bai())


    while not ket_thuc:
        diem_cua_ban = tinh_tong_the_bai(bai_cua_ban)
        diem_cua_may = tinh_tong_the_bai(bai_cua_may)

        print(f"Bai cua ban la: {bai_cua_ban}, tong la: {diem_cua_ban}")
        print(f"Bai cua may co la dau: {bai_cua_may[0]}")

        if diem_cua_ban == 0 and diem_cua_may == 0 and diem_cua_ban > 21:
            ket_thuc = True
        else:
            hoi = input("Ban co muon chia bai tiep khong? 'y' tiep tuc hoac 'n' ket thuc: ")
            if hoi == "y":
                bai_cua_ban.append(chia_bai())
            else:         
                ket_thuc = True

    while diem_cua_may != 0 or diem_cua_may < 17:
        bai_cua_may.append(chia_bai())
        diem_cua_may = tinh_tong_the_bai(bai_cua_may)

    print(f"Bai cua ban la: {bai_cua_ban}, Tong diem: {diem_cua_ban}")
    print(f"Bai cua may la: {bai_cua_may}, Tong diem: {diem_cua_may}")
    print(so_sanh(diem_cua_ban,diem_cua_may))

while input("Co muon choi BlackJack khong? 'y' or 'n': ") == "y":
    cls()
    choi_bai()
