def addition(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(addition(10, 20))
print(addition(10, 20, 30))
print(addition(24, 76, 320, 970, 50))