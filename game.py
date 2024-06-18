import random 
min_range = int(input("what is you your lowest number range: "))
max_range = int(input("what is your maximum number range: "))
h = random.randrange(min_range,max_range)
num_attempt = 0 
user_num = int(input("what is your game play number?"))
while h != user_num:
    if user_num < h:
        print ("your number is too small! ")
        user_num = int(input("what is your new play number ")) 
        num_attempt += 1
    elif user_num > h:
        print ("your number is  too big ")
        user_num = int(input("what is your new play number "))
        num_attempt += 1
print("corret! your corret answe is {0} the number of attempets are {1}".format(h,num_attempt))

