
cannang = float(input("Ban nang bao nhieu: "))
chieucao = float(input("Ban cao bao nhieu: "))
bmi = round(cannang / (chieucao**2),2)


if bmi < 16:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Gay do III.")
elif bmi < 18.5:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Gay do II.")
elif bmi < 25:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Thua can.")
elif bmi < 30:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Beo phi do 1.")
elif bmi < 35:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Beo phi do 2.")
else:
    print(f"Chi so bmi cua ban la: {bmi}. Ban bi Beo phi do 3.")