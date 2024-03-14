def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        raise ValueError("Invalid value of i")

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if i < len(left):
        return ith_order_statistic(left, i)
    elif i < len(left) + len(middle):
        return middle[0]
    else:
        return ith_order_statistic(right, i - len(left) - len(middle))

if __name__ == "__main__":
    arr = [3, 89, 23, 41, 2, 12,36]
    i = 3

    ith_order = ith_order_statistic(arr, i)
    print(f"The {i}th order statistic is: {ith_order}")
