def merge_sorted_arrays(arrays):
    result = []
    while arrays:
        min_val = float('inf')
        min_index = -1

        for i, arr in enumerate(arrays):
            if arr and arr[0] < min_val:
                min_val = arr[0]
                min_index = i

        if min_index != -1:
            result.append(min_val)
            arrays[min_index].pop(0)
            if not arrays[min_index]:
                arrays.pop(min_index)

    return result

def main_merge_sorted_arrays():
    k = int(input("Enter the number of sorted arrays (K): "))
    n = int(input("Enter the size of each array (N): "))

    arrays = []
    for i in range(k):
        array_input = list(map(int, input(f"Enter sorted array {i+1} (comma seperated): ").split(",")))
        arrays.append(array_input)

    merged_result = merge_sorted_arrays(arrays)
    print("Merged Result:", merged_result)

if __name__ == "__main__":
    main_merge_sorted_arrays()
