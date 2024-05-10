class Solution(object):


    def fib(self,n):
        a, b =0,1

        if n <= 1:
            return n
        else:
            for i in range(2, n + 1):
                a,b = b, a+b

        return b

# Initialize the Solution object with the argument 'n'

n = 3

solutionObj = Solution()

# Call the 'fib()' method of the Solution object
FibiNumber = solutionObj.fib(n)
print(FibiNumber)
