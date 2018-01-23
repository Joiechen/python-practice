print "Hello World!"
print "I'd like to say this is python 2.7"
# -*- coding:utf-8 -*-

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

x = "There are %d types of people." % 10  #数字用d表示，百分号引用后面的值
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not) #string使用s表示，百分号引用，小括号里面用逗号分割两个变量引用

print x
print y

print "I said: %r." % x #r是对于复杂类型的引用
print "I also said:'%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  #百分号可以连接打印两个不同类型的输出

w = "This is the left side of ..."
e = "a string with a right side."

print w + e #加号可以连接显示字符串
