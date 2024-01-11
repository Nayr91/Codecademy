import math

def sieve_of_eratosthenes (limit):
  # handle edge cases
  if (limit <= 1):
    return []

  # create the output list
  output = [True] * (limit+1)

  # mark 0 and 1 as non-prime
  output[0], output[1] = False, False

  # iterate up to the square root of the limit
  for i in range(2, math.floor(math.sqrt(limit))):
    if (output[i] == True):
      j = i ** 2    # initialize j to square of i

      # mark all multiples of i as non-prime
      while j <= limit:
        output[j] = False
        j += i

  # remove non-prime numbers 
  trues = [i for (i,v) in list(enumerate(output)) if v is True]
  return trues
