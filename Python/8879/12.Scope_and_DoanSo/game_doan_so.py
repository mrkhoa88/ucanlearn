
#1. doan mot so nam trong range [1..100]
#2. tao ham kiem tra so ban doan voi day so random, nhan xet > ; < =
#3. tao mot ham lua chon level de hoac kho. neu de co 10 lan doan, neu kho co 5 lan doan.


from random import randint

level_de = 10
level_kho = 5
luotdoan = 0

#Ham nhan xet
def nhanxet(soban,somay,luotdoan):
    """Nhan xet so ban voi so may, tra ve so luot doan - 1"""
    if soban > somay:
        print("So ban > so may")
        return luotdoan - 1
    elif soban < somay:
        print("So ban < so may")
        return luotdoan - 1
    else:
        print("Ban thang roi. So ban = so may")

#ham chon de hoac kho

def luachon():
    level = input("Ban lua chon de hay kho? 'de' / 'kho' ")
    if level == "de":
        return level_de
    else:
        return level_kho


def game():
    print("Chao mung den voi tro choi doan so")
    print("Ban hay doan 1 so trong pham vi 1..100")


    socuamay = randint(1, 100)
    print(f"So may random: {socuamay}")


    luotdoan = luachon()
    

    sobandoan = 0

    while sobandoan != socuamay:
        print(f"Ban co {luotdoan} luot doan cho tro choi")
        sobandoan = int(input("Moi ban doan: "))

        luotdoan = nhanxet(sobandoan, socuamay, luotdoan)
        if luotdoan == 0:
            print("Ban het luot doan, ban thua roi")
            return
        elif sobandoan != socuamay:
            print("Moi doan lai")


game()