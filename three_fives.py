# Create threesFives(n) that adds values from 1 and n (inclusive) if that value is not divisible by 3 or 5. Return the final sum.

# For example, threesFives(10) returns 22 as it only returns the sum of 1, 2, 4, 7, and 8. On that example, it skips 3, 6, 9 as those are divisible by 3. It also skips 5, and 10 as it's divisible by 5.

def threeFives(num):
  if num == 1:
    return 1
  if num%5 != 0 and num%3 != 0:
    return num + threeFives(num-1)
  else:
    return 0 + threeFives(num-1)

print(threeFives(7))

# threeFives(10) to return 22
# threeFives(15) to return 60