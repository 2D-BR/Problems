class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rango = len(arr)
        rank = [1] * rango

        for i in range(rango):
            for j in range(rango):
                n = 0
                repetido = 0
                if arr[i] > arr[j]:
                    while n <= j:
                        if arr[n] == arr[j]:
                            repetido += 1
                        n += 1
                    if repetido < 2:
                        rank[i] += 1
            
        return rank

s = Solution()
array = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(s.arrayRankTransform(array))
"""
Entrada: arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]

Salida: [5, 3, 4, 2, 8, 6, 7, 1, 3]
"""