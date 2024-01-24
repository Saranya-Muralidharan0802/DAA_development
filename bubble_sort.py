def bubble_sort(arr):
    arr_size = len(arr)
    swap_flag = False
    for i in range(arr_size - 1):
        for j in range(0, arr_size - i - 1):
            if arr[j] > arr[j + 1]:
                swap_flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap_flag:
            break


if __name__ == "__main__":
    input_array = [34,11,98,55,4,63]
    bubble_sort(input_array)
    for i in range(len(input_array)):
        print(input_array[i])
