class Solution(object):


    def fib(self,n):
        fibArr = [0, 1]

        if n <= 1:
            return n
        else:
            for i in range(2, n + 1):
                fibArr.append(fibArr[-1] + fibArr[-2])

        return fibArr[n]

# Initialize the Solution object with the argument 'n'

n = 3

solutionObj = Solution()

# Call the 'fib()' method of the Solution object
FibiNumber = solutionObj.fib(n)
print(FibiNumber)
