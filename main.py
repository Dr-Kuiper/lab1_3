def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def main():
    n = int(input("Enter the length of the array: "))
    arr = [int(input(f"Enter the {i+1} number: ")) for i in range(n)]

    print(f"Initial array: {arr}")
    print(f"Sorted array: {bubble_sort(arr)}")

if __name__ == "__main__":
    main()