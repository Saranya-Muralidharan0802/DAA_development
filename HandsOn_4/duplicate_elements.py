def remove_duplicates(sorted_array):
    if not sorted_array:
        return sorted_array

    i = 0
    for j in range(1, len(sorted_array)):
        if sorted_array[j] != sorted_array[i]:
            i += 1
            sorted_array[i] = sorted_array[j]

    return sorted_array[:i+1]

def main_remove_duplicates():
    array_input = list(map(int, input("Enter a sorted array with duplicates (comma separated): ").split(",")))
    result = remove_duplicates(array_input)
    print("Result:", result)

if __name__ == "__main__":
    main_remove_duplicates()
