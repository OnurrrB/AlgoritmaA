import random

def bubble_sort(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


sayi_adedi = int(input("Kaç tane rastgele sayı olsun? "))
sayilar = [random.randint(1, 100) for _ in range(sayi_adedi)]

print("Orijinal liste:", sayilar)

siralı_liste = bubble_sort(sayilar)
print("Sıralı liste:", siralı_liste)
