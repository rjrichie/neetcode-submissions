class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        arr1, arr2 = nums1, nums2
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        
        l, r = 0, len(arr1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            arr1L = arr1[i] if i >= 0 else float("-infinity")
            arr1R = arr1[i + 1] if (i + 1) < len(arr1) else float("infinity")
            arr2L = arr2[j] if j >= 0 else float("-infinity")
            arr2R = arr2[j + 1] if (j + 1) < len(arr2) else float("infinity")

            if arr1L <= arr2R and arr2L <= arr1R:
                if total % 2:
                    return min(arr1R, arr2R)
                return (max(arr1L, arr2L) + min(arr1R, arr2R)) / 2
            elif arr1L > arr2R:
                r = i - 1
            else:
                l = i + 1