def asalMi(sayi):
    sayiAsaligi=True 
    for i in range(2,sayi):
        if sayi % i == 0 :
            sayiAsaligi = False

    if sayiAsaligi:
        print(f"{sayi} : bir asal sayıdır")
    else:
        print(f"{sayi} : bir asal sayı değildir")

klavyeGiris = input("sayının asalığı sorgulanması için bir sayi girişi yapınız(çıkış için q ya basınız)")

while klavyeGiris != "q":
    asalMi((int)(klavyeGiris))
    klavyeGiris = input(
        "sayının asalığı sorgulanması için bir sayi girişi yapınız(çıkış için q ya basınız)"
    )
    
