sum_to(6)  # returns 21
sum_to(10) # returns 55

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

sum_to(6)  # returns 21
sum_to(10) # returns 55


def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

# Write a function named occurrences that takes two string arguments as input and 
# counts the number of occurrences of the second string inside the first string.


def occurrences(string, char):
  count = 0
  for c in string:
    if c == char:
      count += 1
  return count

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0


# Write a function named product that takes an arbitrary number of numbers,
#  multiplies them all together, and returns the product. 


def product(*args):
  product = 1
  for num in args:
    product *= num
  return product

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0