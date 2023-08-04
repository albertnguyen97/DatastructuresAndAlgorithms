def factorial(n):
    assert 0 <= n and int(n) == n, "Error"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def sumDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumDigits(int(n))


def power(base, exp):
    assert int(exp) == exp, 'must be integer'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp + 1)
    return base * power(base, exp - 1)


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'must be integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def decimalToBinary(a):
    assert int(a) == a, "must be integer"
    if a < 0:
        a = -1 * a
    if a == 0:
        return 0
    else:
        return a % 2 + 10 * decimalToBinary(a/2)


def reverse(strng):
    if len(strng) <= 1:
        return strng
    else:
        return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


def isPalindrome(strng):
    if len(strng) ==0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True


def flatten(arr):
    arrFinal=[]
    for cusItem in arr:
        if type(cusItem) is list:
            arrFinal.extend(flatten(cusItem))
        else:
            arrFinal.append(cusItem)
    return arrFinal


def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum


def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj


def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr