import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def print_iterations(iterations):
    print("Iterations:")
    for i in range(len(iterations)):
        print(f"Iteration {i+1}: {iterations[i]}")

def print_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

def print_before_and_after(arr, sorted_arr):
    print("Before sorting:", arr)
    print("After sorting:", sorted_arr)

def analyze_algorithm():
    worst_case = [99, 97, 95, 90, 90, 89, 88, 85, 84, 81, 79, 77, 74, 71, 68, 64, 63, 62, 60, 59, 55, 54, 53, 50, 49, 48, 46, 44, 43, 43, 41, 40, 40, 39, 39, 36, 36, 33, 33, 32, 32, 31, 31, 26, 25, 24, 23, 22, 21, 21, 21, 20, 19, 19, 18, 17, 15, 15, 10, 9, 9, 8, 7, 7, 6, 5, 3, 3, 3, 2, 1, 1, 1]
    best_case = [1, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7, 8, 9, 9, 10, 15, 15, 17, 18, 19, 19, 20, 21, 21, 21, 22, 23, 24, 25, 26, 31, 31, 32, 32, 33, 33, 36, 36, 39, 39, 40, 40, 41, 43, 43, 44, 46, 48, 49, 50, 53, 54, 55, 59, 60, 62, 63, 64, 68, 71, 74, 77, 79, 81, 84, 85, 88, 89, 90, 90, 95, 97, 99]
    average_case = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Worst Case Analysis:")
    start_time = time.time()
    bubble_sort(worst_case)
    print_iterations(worst_case[:5] + worst_case[-5:])
    print_execution_time(start_time)
    print_before_and_after(worst_case, worst_case)

    print("\nBest Case Analysis:")
    start_time = time.time()
    bubble_sort(best_case)
    print_iterations(best_case[:5] + best_case[-5:])
    print_execution_time(start_time)
    print_before_and_after(best_case, best_case)

    print("\nAverage Case Analysis:")
    start_time = time.time()
    bubble_sort(average_case)
    print_iterations(average_case[:5] + average_case[-5:])
    print_execution_time(start_time)
    print_before_and_after(average_case, average_case)

# Main program
arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

print("Pilihan pengurutan:")
print("1. Bubble Sort")
print("2. Insertion Sort")

choice = input("Masukkan pilihan Anda (1/2): ")

if choice == '1':
    print("\nBubble Sort")
    sorted_arr = arr.copy()
    start_time = time.time()
    bubble_sort(sorted_arr)
    print_iterations(sorted_arr[:5] + sorted_arr[-5:])
    print_execution_time(start_time)
    print_before_and_after(arr, sorted_arr)
    analyze_algorithm()
elif choice == '2':
    print("\nInsertion Sort")
    sorted_arr = arr.copy()
    start_time = time.time()
    insertion_sort(sorted_arr)
    print_iterations(sorted_arr[:5] + sorted_arr[-5:])
    print_execution_time(start_time)
    print_before_and_after(arr, sorted_arr)
    analyze_algorithm()
else:
    print("Pilihan tidak valid.")