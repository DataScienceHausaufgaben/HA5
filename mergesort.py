# Importe
import matplotlib.pyplot as plt

# Methode zum Sortieren einer Liste mit mergesort
def mergeSort(list):
    # Ermittlung der Listenlänge
    length = len(list)

    # Überprüfung ob die Liste sortierbar ist
    if (length <= 1):
        return list
    
    # Mittiges Aufteilen der Liste 
    mid = length // 2
    left = list[:mid]
    right = list[mid:]

    # Rekursiver Aufruf mit den Teillisten
    return merge(mergeSort(left),mergeSort(right))
    
# Sortiert und merged die Teillisten
def merge(left ,right):
    # Definieren der neuen List und Laufvariablen
    merged = []
    l,r = 0,0

    # Sortieren 
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    # Hinzufügen der übrigen Zahlen der Teillisten zur merged-Liste
    while l < len(left):
        merged.append(left[l])
        l += 1

    while r < len(right):
        merged.append(right[r])
        r += 1

    return merged



# Deklarierung der zu sortierenden Liste
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Visualisierung der unsortierten Liste
plt.subplot(2, 1, 1)
plt.bar(range(len(my_list)), my_list)
plt.title('Unsorted List')

# Sortieren
my_list = mergeSort(my_list)

# Visualiserung der sortierten Liste
plt.subplot(2, 1, 2)
plt.bar(range(len(my_list)), my_list)
plt.title('Sorted List')

# Plotten
plt.tight_layout()
plt.show()