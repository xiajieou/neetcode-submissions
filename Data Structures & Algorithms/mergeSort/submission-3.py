# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        

        m = (s + e) // 2  # s + (e-s) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs


    def merge(self, arr, s, m, e):
        L = arr[s:m + 1]
        R = arr[m + 1:e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halfs

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                #stable
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # one of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    