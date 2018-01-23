#UTF-8
def fib(to = 10):
    curr = 0
    next = 1
    count = 0
    while count < to:
        yield curr
        curr = next
        next = curr +next
        count += 1


if __name__ == '__main__':
    for x in fib(20):
        print (x + 1)
