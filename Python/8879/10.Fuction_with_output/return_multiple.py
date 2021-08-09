def hoten(ho,ten):
    if ho == "" or ten == "":
        return f"Ho hoac Ten khong duoc rong"
    else:
        in_ho = ho.title()
        in_ten = ten.title()
        return f"Ho va Ten: {in_ho} {in_ten}"

ho_va_ten = hoten(input("Moi nhap ho: "), input("Moi nhap ten: "))
print(ho_va_ten)