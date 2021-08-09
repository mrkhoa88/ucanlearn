
def nam_nhuan(nam):
    ''' Ham tinh nam nhuan'''
    if nam % 4 == 0:
        if nam % 100 == 0:
            if nam % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def ngay_trong_thang(nam,thang):
    ''' Tra ve so ngay cua thang '''
    if thang > 12 or thang < 1:
        return "Thang khong hop le"
        
    if nam <= 0:
        return "Nam khong hop le"
        
    ngay_cua_thang = [31,28,31,30,31,30,31,31,30,31,30,31]
    if nam_nhuan(nam) and thang == 2:
        return 29
    return ngay_cua_thang[thang - 1]

nhap_nam = int(input("Moi nhap vao nam: "))
nhap_thang = int(input("Moi nhap vao thang: "))

ngay = ngay_trong_thang(nhap_nam,nhap_thang)
print(f"Thang {nhap_thang} nam {nhap_nam} co: {ngay} ngay")

