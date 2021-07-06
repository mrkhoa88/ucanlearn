
print("Chuong chia tien bill an uong")

bill = float(input("Tong tien la bao nhieu: "))
tips = float(input("Ban muon tips bao nhieu %: 10, 12, or 15"))
people = int(input("Ban co bao nhieu nguoi: "))

tip_as_percent = tips / 100
total_tip_amount = bill + tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person,2)
print("So tien moi nguoi phai tra la: ",final_amount)