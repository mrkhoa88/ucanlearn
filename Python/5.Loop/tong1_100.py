
#Tinh tong tu 1-100
#Tinh tong cac so chan tu 1-100
print("Chuong trinh tinh tong tu 1--100")

tong = 0

for i in range(0,101):
    tong +=i
print(f"Tong tu 1-100 = {tong}")

tongchan = 0

for j in range(0,101,2):
    tongchan += j
print(f"Tong chan = {tongchan}")