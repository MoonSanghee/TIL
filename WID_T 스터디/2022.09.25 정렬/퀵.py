def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, 0, right - 1)
    quick_sort(arr, right + 1, end)

n, k = map(int, input().split())
nums = list(map(int, input().split()))
quick_sort(nums, 0, len(nums) - 1)
print(*nums, sep="\n")