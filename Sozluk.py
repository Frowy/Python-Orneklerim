# Sözlük verisi oluşturup dolduralım.
sozluk = {
    'elma': 'meyve',
    'araba': 'taşıt',
    'kitap': 'nesne', 
    'baba' : 'insan',
    # Yeni kelime örneği: 'yeni kelime': 'anlamı'
}

while True:
    # Kullanıcıdan bir kelime girmesini istedik
    kelime = input("Bir kelime girin (çıkmak için 'q' tuşuna basın): ")

    if kelime == 'q':
        break  # Kullanıcı 'q' tuşuna basarsa döngüden çık

    # Sözlükte kelimenin olup olmadığınıda kontro eledeceğiz
    if kelime in sozluk:
        print(f"'{kelime}' sözlükte bulunuyor ve anlamı: {sozluk[kelime]}")
    else:
        print(f"'{kelime}' sözlükte bulunmuyor.")