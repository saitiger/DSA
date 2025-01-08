def solve(n):
  res = []
  for i in range(1,n+1):
    if i%15==0:
      res.append('FizzBuzz')
    elif i%5==0:
      res.append('Buzz')
    elif i%3==0:
      res.append('Fizz')
    else:
      res.append(i)
  return res

# Without using Modulo
def solve(n):
    fizz, buzz, fizzbuzz = 0, 0, 0
    result = []
    for i in range(1, n + 1):
        fizz += 1
        buzz += 1
        fizzbuzz += 1

        if fizzbuzz == 15:
            result.append('FizzBuzz')
            fizzbuzz = 0
            fizz = 0  # Resetting both counters because FizzBuzz includes Fizz and Buzz
            buzz = 0
        elif fizz == 3:
            result.append('Fizz')
            fizz = 0
        elif buzz == 5:
            result.append('Buzz')
            buzz = 0
        else:
            result.append(i)
    return result
