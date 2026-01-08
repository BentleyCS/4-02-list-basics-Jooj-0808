#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    odd_numbers_string = ""
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            odd_numbers_string += str(i) + " "  # Concatenate the odd number and a space

    print(odd_numbers_string.strip())  # Remove trailing space and print

def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    result_string = ""
    for i in range(n, 0, -1):
        result_string += str(i)
    print(result_string)



def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    import random
    attempt = 0

    while True:
        num = random.randint(1, 10)
        attempt += 1
        print(num)

        if num == 10:
            print("We got it in " + str(attempt))
            break

def reverse(word:str)->str:

    newword = word[::-1]
    print(newword)

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """

    if n % 3 == 0:
        if n % 5 == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    elif n % 5 == 0:
        if n % 3 == 0:
            print("fizzbuzz")
        else:
            print("buzz")
    else:
        print(n)

def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    newn = 0

    while newn != 1:
        if n % 2 == 0:
            newn = n/3+1
            print(newn)
        elif n % 2 != 0:
            newn = n*3+1
            print(newn)




def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """


oddNumbers(5)
backwards(5)
randomRepeating()
reverse("Hello")
fizzBuzzContinuous(15)
collatz(10)