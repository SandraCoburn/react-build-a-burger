'''
The factorial of a number is the product of all the integers from 1 to that number.ex:
1*2*3*4*5*6 = 720
'''
#to take input from the user
# n = int(input("give me a number: "))
def fact(n):
    product = 1
    if n < 0:
        print("sorry, factorial numbers does not exist for negative number")
    elif n == 0:
        # print("the factorial of 0 is 1")
       return product
    else:
        for num in range(n):
            product = product * (num+1)
        return product
n = 5
print(fact(n)) #1*2*3*4*5 = 120
print("factorial","=" * 20)

# print the sum of integers in array
def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

items = [1,2,3,4,5,6]
print(sum_list(items))

print("sum of array","=" * 20)


## fibonacci sequeence, find F(n) given n
def nth_fib(n):
    # n is the sum of the two previous numbers
    ## n = 0 , 0 n = 1, 1
    ## n = n-1 + n-2
    #base case
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)

print(nth_fib(8)) # 0,1,1,2,3,5,8,13
print("fibonn recur","=" * 20)

def fibonacci(n):
    if n == 1:
        return 0 # first fibonacci number is 0
    if n == 2:
        return 1 # second fibonacci number is 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9)) # 0,1,1,2,3,5,8,13,21
print("fibbonaci","=" * 20)   
         
'''
Find the first item that occurs an even number of times in an array.
Remember to handle multiple even-occurrence items and return the first one.
Return null if there are no even-occurrence items.
'''
def first_dup(lst):
  dupl = []
  no_dup = -1
  for num in range(len(lst)):

    if lst[num] in dupl:
      return lst[num]
    else:
      dupl.append(lst[num])
  
  return no_dup

arr = [1,2,3,4,5,2,6,7]
print(first_dup(arr))
print("first duplicate in array","=" * 20)

def sum1(n):
  total = 0
  for x in range(n +1): #because zero index you add 1
    #print("iteration: ",x)
    total = total + x
    #print("total: ", total)
  return total

print(sum1(4))
print("sum of integers in number ex: 4 = 1 + 2 + 3 +4","=" * 20)

arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def div_by_three(lst):
  for n in lst:
    if n % 3 == 0:
      print(n)
div_by_three(arr)

print("divide by 3","=" * 20)





