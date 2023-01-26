class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        to_say = []
        for i in range(1,n+1):
            if i%5==0 and i%3==0:
                to_say.append('FizzBuzz')
            elif i%3==0:
                to_say.append('Fizz')
            elif i%5==0:
                to_say.append('Buzz')
            else:
                to_say.append(str(i))
        return to_say