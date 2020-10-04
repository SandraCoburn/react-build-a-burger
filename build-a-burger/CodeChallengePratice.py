def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(12))

def iterative_fibonacci(index):
    first_num = 0
    second_num = 1
    if index == 0:
        return second_num
    if index == 1:
        return second_num
    for i in range(2, index +1):
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
    return third_num


cache ={}
def dynamic_fibonacci(n):
    if n in cache:
        return cache[n]
    else: 
        if n < 2:
            return n
        else:
            cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
            return cache[n]

def factorial(num):
    f = 1
    for i in range(1, num +1):
        f = f * i
    return f

def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_factorial(num -1)

def gerund(string):
    #  st = [s for s in string]
    #  print(st)
    #  ing = ["i", "n", "g"]

     if string[-3:] == "ing":
         return "to " + string[:-3]

print(gerund("building"))

def commafy(lst):
    lst[-1] = "and " + lst[-1] 
    return ", ".join(lst)

print(commafy(["hello", "apple", "list"]))

def how_many(lst):
    if lst[0] == 1:
        return f'there is {str(lst[0])} {lst[-1]}'
    else:
        return f'there are {str(lst[0])} {lst[-1]}s.'

print(how_many([2, "dolls"]))

def abrieviator(string):
    if len(string) < 5:
        return string
    else:
        return string[:4]
print(abrieviator("enigmatic"))

def lookup_states_abr(abreviation):
    ## make a dictionary to hold the states and abbreviations
    states = {
        "CA": "California",
        "NY": "New York"
    }

    return states[abreviation]
print(lookup_states_abr("CA"))