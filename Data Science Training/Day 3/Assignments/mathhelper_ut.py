print('''This is Utkarsh\'s Mathhelper Module in Python /''')
def give_fibo(n):
    fibo = [0,1]
    for n in range(n-2):
        last_num = fibo[-1]
        second_last_num = fibo[-2]
        next_num = last_num + second_last_num
        fibo.append(next_num)
    return fibo

def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return 'Not a Prime Number'
            break
    else: 
        return 'Prime number'



def sum_of_n_natural_numbers(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


