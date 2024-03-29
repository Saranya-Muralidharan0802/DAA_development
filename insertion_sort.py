def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_element


if __name__ == "__main__":
    input_array = [9, 4, 7, 2, 5, 8]
    insertion_sort(input_array)
    for i in range(len(input_array)):
        print(input_array[i])
