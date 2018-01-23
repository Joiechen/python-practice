from sys import argv

script, filename = argv  #these 2 parameters for input

txt = open(filename) #open a file and save it in the txt varable

print "Here's your file %r:" % filename #print the filename which input as the parameter
print txt.read() #print the file content
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") #try to input the file name again

txt_again = open(file_again)
print txt_again.read()  #read the file again
txt_again.close()
