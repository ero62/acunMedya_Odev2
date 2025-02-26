def topla(sayi1, sayi2):
    print(sayi1 + sayi2)


def bol(sayi1, sayi2):
    if sayi2 == 0 : 
        print("Bölme işlemi için ikinci sayı 0 olamaz!")
    else:
        print(sayi1/sayi2)


def cıkar(sayi1, sayi2):
    print(sayi1 - sayi2)


def carp(sayi1, sayi2):
    print(sayi1 * sayi2)

def hesap_makinasi(sayi1,sayi2,islem):
    if islem == "+" :
        topla(sayi1,sayi2)
    elif islem == "*":
        carp(sayi1, sayi2)
    elif islem == "/":
        bol(sayi1, sayi2)
    elif islem == "-":
        cıkar(sayi1, sayi2)
    else:
        print(f"gecersiz islem turu : {islem}")

hesap_makinasi(5, 3, "+")  # Çıktı: 5 + 3 = 8
hesap_makinasi(10, 2, "/")  # Çıktı: 10 / 2 = 5.0
hesap_makinasi(4, 0, "/")  # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
hesap_makinasi(6, 2, "%")  # Çıktı: Geçersiz işlem türü!
