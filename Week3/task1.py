def get_sum_digits(num):
    sum = 0
    digits = str(num)
    for i in digits:
        sum += int(i)
    return sum


print(get_sum_digits(123))
print(get_sum_digits(223))
print(get_sum_digits(1337))