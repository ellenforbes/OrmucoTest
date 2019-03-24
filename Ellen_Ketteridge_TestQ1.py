#Define global variables
line_test = True
user_input = "Y"
line_master = []

#Set conditions under which the script will continue to run
while line_test == True or user_input == "Y":
#Ask user for inputs and create rules for inputs.
    line_start = int(input('Where will your line start? Enter a number from 0 to 99. '))
    if line_start > 100:
        print("Sorry that line starts off the edge, try a number smaller than 100 next time.")
        pass
    else:
        line_length = int(input('How long will your line be? Enter a number. '))
        line_end = (line_start) + (line_length)
        if line_end > 100:
            print("Sorry that line went off the edge at 100.")
            pass
#Once line has been assessed as having a valid range the test on whether to draw it or not begins.
        else:
            print ("Preparing to draw a line " + str(line_length) + " units long...")
            for i in range(line_start, line_end):
                if i in line_master:
                    line_test = False
                    print ("Sorry that line overlaps, I can't add it.")
                    break
                else:
                    line_test = True
                line_master.append(i)
#Whether the line is drawn or not, the user is asked if they want to continue the program, no will end it.
    user_input = input("Your current line looks like this: " + str(line_master) + ". Shall we draw another? (Y/N) ")
    if user_input == "N":
        print ("Okay, thanks for drawing lines.")
        break
    else:
        pass
