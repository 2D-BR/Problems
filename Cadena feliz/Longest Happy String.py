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
        cont = 0

        while n < len(letras_ordenadas):
            if letras_ordenadas[n][0] > 0 and cont < 2:
                happy += letras_ordenadas[n][1]
                letras_ordenadas[n][0] -= 1  
                cont += 1
            else:
                if letras_ordenadas[n][0] == 0:
                    letras_ordenadas.pop(n)
                    n = 0
                    cont = 0
                else:
                    n += 1
                    cont = 0

        return happy




s = Solution()
a = 1
b = 1
c = 7
print(s.longestDiverseString(a, b, c))