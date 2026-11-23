def addition(*args):
    total = 0
    for num in args:
        total += num
    return total

addition(1, 2, 3, 4, 5) 
addition(10, 20)
addition(5, 10, 15, 20, 25, 30)