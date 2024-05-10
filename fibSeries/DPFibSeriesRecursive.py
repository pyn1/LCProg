class Solution(object):


    def fib(self,n):

        if n <= 1:
            return n
        else:
           return self.fib(n-1) + self.fib(n-2)


# Initialize the Solution object with the argument 'n'

n = 3

solutionObj = Solution()

# Call the 'fib()' method of the Solution object
FibiNumber = solutionObj.fib(n)
print(FibiNumber)
