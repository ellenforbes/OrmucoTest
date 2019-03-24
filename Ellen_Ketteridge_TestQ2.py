#Import library where calculations are made
import eklibrary

#Ask user to enter inputs
input_one = float(input('Please enter your first input. '))
input_two = float(input('Please enter your second input. '))

#Use function defined in the library to assess user inputs
test_inputs = eklibrary.greaterlesser(input_one, input_two)

#Print results for user
print("Your " + test_inputs)
