'''
Nhap vao mot nam bat ky, kiem tra xem nam do co nhuan hay khong
Nhap vao mot thang, kiem tra thang do co bao nhieu ngay.
'''

m = int(input('Nhap vao so thang: '))
if m in (1,3,5,7,8,10,12):
    print('Thang',m,'co 31 ngay')
elif m in (4,6,9,11):
    print('Thang',m,'co 30 ngay')
elif m == 2:
    y = int(input('Moi ban nhap vao nam: '))
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        print('Nam nhuan nen thang 2 co 29 ngay')
    else:
        print('Nam khong nhuan nen thang 2 co 28 ngay')
else:
    print('Thang nhap khong hop le')