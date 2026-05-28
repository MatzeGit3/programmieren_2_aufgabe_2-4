import numpy as np
import matplotlib.pyplot as plt 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

    plt.plot(sorted_arr)
    plt.show()