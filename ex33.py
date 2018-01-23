numbers = []

def loopfunction(in_num):
    i = 0
    while i < in_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loopfunction(7)

print "The numbers: "

for num in numbers:
    print num 