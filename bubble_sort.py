def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        already_sorted=True
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                already_sorted=False
        if already_sorted:
            break
    return arr

if __name__ == "__main__":
    k=bubble_sort([2,5,3,4,7,9,0])
    print(k)