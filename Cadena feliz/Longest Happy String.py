class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        happy = ''
        
        A = [a, 'a']
        B = [b, 'b']
        C = [c, 'c']
        letras = [A, B, C]

        # Ordenar la lista de mayor a menor por el primer elemento de cada sublista
        letras_ordenadas = sorted(letras, key=lambda x: x[0], reverse=True)
        n = 0
        while n < len(letras_ordenadas):
            for i in range(len(letras_ordenadas[n])):
                happy = happy + letras_ordenadas[n][1]
                letras_ordenadas[n][0] -= 1   
            if letras_ordenadas[n][0] == 0:
                n = 0
            else:
                n += 1      





s = Solution()
a = 1
b = 1
c = 7
print(s.longestDiverseString(a, b, c))