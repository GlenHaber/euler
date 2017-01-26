"""
Large sum

Work out the first ten digits of the sum of the given one-hundred 50-digit numbers
"""

with open('13.input') as f:
    nums = [int(line) for line in f.readlines()]

print(str(sum(nums))[:10])

# Alternate!
nums = [int(str(n)[:11]) for n in nums]
print(str(sum(nums))[:10])