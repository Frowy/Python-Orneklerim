def hesap_makinasi():
    while True:
        try:
            sayi1 = float(input("\033[93mBirinci sayıyı girin: \033[0m"))
            operator = input("\033[93mİşlem operatörünü girin (+, -, *, /): \033[0m")
            sayi2 = float(input("\033[93mİkinci sayıyı girin: \033[0m"))
            
            if operator == "+":
                sonuc = sayi1 + sayi2
            elif operator == "-":
                sonuc = sayi1 - sayi2
            elif operator == "*":
                sonuc = sayi1 * sayi2
            elif operator == "/":
                sonuc = sayi1 / sayi2
            else:
                print("\033[31mGeçersiz operatör girdiniz.\033[0m")
                continue
            
            print("Sonuç:", sonuc)
            
            devam = input("Devam etmek için 'e' tuşuna basın, çıkmak için 'q' tuşuna basın: ")
            if devam.lower() == 'q':
                break
                
        except ValueError:
            print("\033[31mGeçersiz bir değer girdiniz. Tekrar deneyin.\033[0m")

if __name__ == "__main__":
    hesap_makinasi()
