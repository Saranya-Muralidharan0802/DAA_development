import timeit
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def random_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return random_quicksort(left) + middle + random_quicksort(right)

def best_case(n):
    return list(range(1, n + 1))

def worst_case(n):
    return list(range(n, 0, -1))

def average_case(n):
    return [random.randint(1, 1000) for _ in range(n)]

def benchmark(sort_function, cases, sizes):
    results = {case.__name__: [] for case in cases}

    for size in sizes:
        for case in cases:
            data = case(size)
            stmt = lambda: sort_function(data.copy())
            time = timeit.timeit(stmt, number=1)
            results[case.__name__].append(time)

    return results

def plot_benchmarks(results, sizes):
    for case, times in results.items():
        plt.plot(sizes, times, label=case)

    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 2000, 5000]

    benchmark_results_quicksort = benchmark(quicksort, [best_case, worst_case, average_case], input_sizes)

    plot_benchmarks(benchmark_results_quicksort, input_sizes)
