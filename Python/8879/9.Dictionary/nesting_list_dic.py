
#Vi du 1 nesting binh thuong ta co:

country = {
    "VietNam": "HaNoi",
    "ThaiLan": "Bataza",
    "France" : "Paris",
    "Amarica": "NewYork"
}

#vi du ve nesting list long nhau

du_lich = {
    "VietNam": ["Hanoi","TPHCM","HaLong","DongThap"],
    "America" : ["NewYork","Omaha","Washinton DC"]
}

#Vi du ve nesting dic & dic

du_lich1 = {
    "TPHCM": {"DiaDiem": ["Quan1","ThuDuc","BinhThanh"], "Solandi": 12},
    "DongThap": {"DiaDiem": ["CaoLanh","SaDec","LaiVung"], "Solandi": 26}
}

#Nesting Dictionary in a list

du_lich3 = [
    {"TinhThanh": "TPHCM", 
    "DiaDiem":["Quan1","ThuDuc","BinhThanh"], 
    "Solandi": 16},

    {"TinhThanh": "DongThap", 
    "DiaDiem":["CaoLanh","SaDec","LaiVung"], 
    "Solandi": 44}
    
]

def them_dic(add_tinhthanh,add_diadiem,ad_solandi):
    dl = {}
    dl["TinhThanh"] = add_tinhthanh
    dl["DiaDiem"] = add_diadiem
    dl["Solandi"] = ad_solandi
    du_lich3.append(dl)

them_dic("AnGiang",["LongXuyen","ChauDoc","NuiCam"],89)
print(du_lich3)
