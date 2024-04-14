
def FizzBuzz(max_num):
    for x in range(1, max_num + 1):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

FizzBuzz(100)
