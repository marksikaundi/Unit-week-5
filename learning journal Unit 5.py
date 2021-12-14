#Question 1
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
  if letter in 'QO':
    print(letter + 'u' + suffix)
  else:
    print(letter + suffix)

# Output: for the codes

# Jack

# Kack

# Lack

# Mack

# Nack

# Ouack

# Pack

# Quack




# question 2
print('Example 1: Substrings and every i-th character')

string = 'Describe the feature illustrated by each example.'

strA = string[0:9]

strB = string[9::2]

strC = string[10::2]

listD = [x + y for x, y in zip(strB, strC)]

string2 = strA + ''.join(listD)

print(string2)

assert string2 == string

print('')


print('Example 2: Ranges and slice objects')

nums = list(range(1,10))

nums2 = nums[:-1:2] + [nums[-1]] + nums[1::2] + nums[50:100:3]

nums3 = list(range(1,10,2)) + list(range(2,10,2))

print(nums2)

print(nums3)

assert nums2 == nums3

string = 'Describe the feature illustrated by each example.'

string2 = string[:-1:2] + string[-1] + string[1::2] + string[50:100:3]

lstA = [string[i] for i in range(0,len(string),2)]

# lstB = [string[i] for i in range(1,len(string),2)]  # what a mess

# lstB = string[slice(1,len(string),2)]  # string, not a list :)

lstB = list(string)[slice(1,len(string),2)]

lstC = [string[i] for i in range(50,100,3) if i in range(len(string))]

string3 = ''.join(lstA) + ''.join(lstB) + ''.join(lstC)

print(string2)

print(string3)

assert string2 == string3

print('')




print('Example 3: Copying and reversing')

string = 'Describe the feature illustrated by each example.'

string2 = string[:]

try: string2[-1] = '!'

except TypeError as e: print(e)

string3 = string

try: string3[-1] = '!'

except TypeError as e: print(e)

string = ''.join(reversed(string))  # it's slower then slicing

string2 = string2[::-1]

print(string)

print(string2)

print(string3)

assert string2 == string

print('')