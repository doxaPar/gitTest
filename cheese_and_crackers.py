def cheese_and_crackers(cheese_count, boxes_of_crackers): # this line defines the function "cheese and crackers"
	print "You have %r cheeses!" % cheese_count # this is part of the function "cheese_and_crackers" and prints the first argument of the defined function
	print "You have %r boxes of crackers!" % boxes_of_crackers # this is the second and uses the second argument of the defined function
	print "That's enough for a party!" # a simple print statement
	print "Get a blanket.\n" # a simple print statement with a carriage return / line feed \n


print "We can just give the functions numbers directly:" # simple text print
cheese_and_crackers(20, 30) # calls the 'cheese_and_crackers function with static arguments.'

print "OR, we can use variables from our script:" # simple text print
amount_of_cheese = 10 # simple variable assignment
amount_of_crackers = 50 # another simple variable assignment

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # calls the function but instead uses variables (defined above) as the rguments to the defined function 'cheese_and_crackers'

print "We can even do math inside too:" # simple print statement
cheese_and_crackers(10 + 20, 5 + 6) # calls the defined function but provides an calculation as the argument

print "And we can combine the two, variables and math:" # simple print statement
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100) # calls the defined function but uses both variables and math to supply the argument

print "Now, let's use input from the user to populate the arguments for the \'cheese_and_crackers\' function."
user_cheeses = raw_input("Please enter the number of cheese: ")
user_crackers = raw_input("Please enter the number of crackers: ")

#int_user_cheeses = int(user_cheeses)
#int_user_crackers = int(user_crackers)

cheese_and_crackers(user_cheeses, user_crackers)
