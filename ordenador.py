from random import sample


def partition(arr, low, high):
    i = low - 1                  # index of smaller element
    pivot = arr[high]            # pivot

    for j in range(low, high):
        # if current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1            # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test the algorithm

# lista = [10, 7, 8, 9, 1, 5]
lista = list(sample(range(0, 100), 30))         # Gera uma lista aleatória de 0 a 100 com 30 elementos
print(lista)
print('#' * 117)
n = len(lista)
quickSort(lista, 0, n - 1)      # Ordena a lista
print(lista)
