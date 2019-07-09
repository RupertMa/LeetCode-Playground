class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n=int(n)
        a=range(1,n+1)
        list=[]
        for number in a:
			if number%3==0 and number%5==0: list.append("FizzBuzz")
			elif number%3==0 and number%5!=0: list.append("Fizz")
			elif number%3!=0 and number%5==0: list.append("Buzz")
			else: list.append(str(number))
        return list