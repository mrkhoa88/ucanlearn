#1. import art.py - hien thi logo

#2. import data - lay du lieu cho tro choi
## khai bao 2 tai khoan random A, B. Neu A giong B thi random B lai
## tao ham format thong tin trong data

#3. so sanh A: ten, nghe, diachi
## voi B: ten, nghe, diachi
## in ra: Ai co nhieu luot theo doi hon ? Type 'A' or 'B'

#4. kiem tra sai: xin loi, ban sai roi, diemso = 0
## Kiemtra dung, random tiep tuc, diemso ++1

#5. Lam cho tro choi lap lai. 
#6. Lam cho B tro thanh A de choi tiep
#7. Xoa man hinh de khong bi cuon dai xuong


from art import logo, vs
from data import data
import random
import os
def cls():
    os.system("clear")

#tao ham format du lieu

def fortmat_data(account):
    """Lay du lieu trong data game va tra ve dinh dang ten, nghe, diachi """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr} from {account_country}")
#in logo

def check_answer(guess, a_follower, b_follower):
    """Doan, so sanh so luot theo doi cua A vs B"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
#random data

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"So sanh A: {fortmat_data(account_a)}.")
    print(vs)
    print(f"voi B: {fortmat_data(account_b)}.")

    #Doan va so sanh A,b

    guess = input("Ai co nhieu luoc theo doi hon? Type 'A' or 'B': ").lower()

    #Lay so luot theo doi
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    cls()
    if is_correct:
        score += 1
        print(f"Ban dung roi. Diem hien tai cua ban la: {score}")
    else:
        game_continue = False
        print(f"Ban doan sai roi. Diem so cuoi cung la: {score}")