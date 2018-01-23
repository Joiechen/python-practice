from sys import exit

def whiteroom(result):
    print "You are in white room that means you already pass through the dark forest."
    print "You will be happy end with the %r" %result
    print "\n Good Luck!"

def back_china():
    print "You have choosen back to china, so there are some good side "

def stay():
    print "You have choosed to stay here, you must know that will hurt your girl friend."

def go_to_canada():
    print "This is the hardest way that you choose to go to canada."

def life_choice():
    g = lambda x:x*2
    print g(3)

    m = lambda x,y,z:(x-y)*z
    print m(4,1,7)

life_choice()     