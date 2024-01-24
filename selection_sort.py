def selection_sort(arr):
    for i in range(len(arr)):
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
        arr[i], arr[min_element] = arr[min_element], arr[i]


if __name__ == "__main__":
    input_array = [47, 12, 6, 79, 93, 64]
    selection_sort(input_array)
    for i in range(len(input_array)):
        print(input_array[i])
