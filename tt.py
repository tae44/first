def is_palindrome(n):
    if len(str(n)) > 1:
        return str(n) == str(n)[::-1]

output = filter(is_palindrome,range(1000))
print(list(output))
