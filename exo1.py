def nombres(liste):
    i = 0
    while i < len(liste):
        if liste[i] % 2 != 0:
            liste.pop(i)
        else:
            i = i + 1
    print(liste)

nombres([1, 2, 3, 4, 5, 6, 7, 8, 9])