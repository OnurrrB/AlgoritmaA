# 1. Bubble Sort
def bubble_sort(dizi):
    n = len(dizi)
    for i in range(n):
        for j in range(0, n-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]

# 2. Insertion Sort
def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i - 1
        while j >= 0 and key < dizi[j]:
            dizi[j + 1] = dizi[j]
            j -= 1
        dizi[j + 1] = key

# 3. Max Subarray Sum (Kadane Algoritması)
def max_subarray_sum(dizi):
    max_so_far = dizi[0]
    max_ending_here = dizi[0]
    for i in range(1, len(dizi)):
        max_ending_here = max(dizi[i], max_ending_here + dizi[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# 4. Fast Exponentiation (Power Algoritması)
def power(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # Eğer üs tekse
            result *= base
        base *= base  # Temeli kareliyoruz
        exp //= 2  # Üssü ikiye böldük
    return result

# 5. Max Alt Dizi Toplamı (Önceki algoritmada da olduğu gibi)
# Bu algoritma, Kadane algoritmasını kullanarak aynı işlevi görmektedir.
def max_alt_dizi_toplam(dizi):
    max_so_far = dizi[0]
    max_ending_here = dizi[0]

    for i in range(1, len(dizi)):
        max_ending_here = max(dizi[i], max_ending_here + dizi[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Örnek kullanımlar
if __name__ == "__main__":
    # Bubble Sort
    dizi_bubble = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(dizi_bubble)
    print("Bubble Sort ile sıralı dizi:", dizi_bubble)

    # Insertion Sort
    dizi_insertion = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(dizi_insertion)
    print("Insertion Sort ile sıralı dizi:", dizi_insertion)

    # Max Subarray Sum
    dizi_max_sub = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Max subarray sum:", max_subarray_sum(dizi_max_sub))

    # Fast Exponentiation
    taban = 2
    üs = 10
    print(f"{taban} üssü {üs}:", power(taban, üs))

    # Max Alt Dizi Toplam
    dizi_max_alt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Max alt dizi toplamı:", max_alt_dizi_toplam(dizi_max_alt))
