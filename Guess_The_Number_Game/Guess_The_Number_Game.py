import random

count = 0
def is_it_even(num):
    if num%2 == 0:
        return 1
    else:
        return 0

def divisible_by_3(num):
    if num%3 == 0:
        return True
    else:
        return False

def divisible_by_4(num):
    if num%4 == 0:
        return True
    else:
        return False

def divisible_by_7(num):
    if num%7 == 0:
        return True
    else:
        return False


def guess_the_number(count):
    n = int(input("Guess the number: "))

    if n > 100 or n <= 0:
        print("ERROR, Please enter a number only from the range 1 to 100(both 1 and 100 included)")
        guess_the_number(count)

    elif n == x:
        print("Hip Hip Hooray!!!")
        print("Congragulations, You guessed it right, The number is: ", x)
        print("You took {} turns for guessing the right number".format(count+1))
        print("Thanks for Playing, Hope you have enjoyed the game")

    else:
        if count == 0:
            if is_it_even(x) == 1:
                print("HINT1: It is an even number, hence divisible by 2")
            else:
                print("HINT1: It is an odd number, hence not divisible by 2")

            print("Try again, You can do it")
            count += 1
            guess_the_number(count)

        elif count == 1:
            if is_it_even(x) == 1:
                print("HINT1: It is an even number, hence divisible by 2")
            else:
                print("HINT1: It is an odd number, hence not divisible by 2")

            print("Let me give some more hints")

            if divisible_by_3(x):
                print("HINT2: It is divisible by 3")
            elif divisible_by_4(x):
                print("HINT2: It is divisible by 4")
            elif divisible_by_7(x):
                print("HINT2: It is divisible by 7")
            else:
                print("HINT2: It isn't divisible by 3,4 and 7, so it MIGHT be a prime number or a single digit number or a number divisible by 5!!!")

            print("Try again, You can do it")
            count += 1
            guess_the_number(count)

        elif count == 2:
            if is_it_even(x) == 1:
                print("HINT1: It is an even number, hence divisible by 2")
            else:
                print("HINT1: It is an odd number, hence not divisible by 2")

            print("Let me give some more hints")

            if divisible_by_3(x):
                print("HINT2: It is divisible by 3")
            elif divisible_by_4(x):
                print("HINT2: It is divisible by 4")
            elif divisible_by_7(x):
                print("HINT2: It is divisible by 7")
            else:
                print("HINT2: It isn't divisible by 3,4 and 7, so it MIGHT be a prime number or a single digit number or a number divisible by 5!!!")

            print("Let me give some more hints")

            if x < 50 and x <= 25:
                print("HINT3: The number is less than 25, it could also be 25!!!")
            elif x < 50 and x > 25:
                print("HINT3: The number is greater than 25 and less than 50, it could also be 25!!!")

            if x > 50 and x <= 75:
                print("HINT3: The number is less than 75 and greater than 50, it could also be 75!!!")
            elif x > 50 and x > 75:
                print("HINT3: The number is greater than 75, it could also be 75!!!")

            print("Try again, You can do it")
            count += 1
            guess_the_number(count)

        elif count >= 3:
            if is_it_even(x) == 1:
                print("HINT1: It is an even number, hence divisible by 2")
            else:
                print("HINT1: It is an odd number, hence not divisible by 2")

            print("Let me give some more hints")

            if divisible_by_3(x):
                print("HINT2: It is divisible by 3")
            elif divisible_by_4(x):
                print("HINT2: It is divisible by 4")
            elif divisible_by_7(x):
                print("HINT2: It is divisible by 7")
            else:
                print("HINT2: It isn't divisible by 3,4 and 7, so it MIGHT be a prime number or a single digit number or a number divisible by 5!!!")

            print("Let me give some more hints")

            if x < 50 and x <= 25:
                print("HINT3: The number is less than 25, it could also be 25!!!")
                print("Let me give some more hints")
                if x <= 15:
                    print("HINT4: You're so close!!! The number is likely to be single digited or something less than or equal to 15")
                elif x > 15:
                    print("HINT4: You're so close!!! The number is greater than or equal to 15")

            elif x < 50 and x > 25:
                print("HINT3: The number is greater than 25 and less than 50, it could also be 25!!!")
                print("Let me give some more hints")
                if x <= 35:
                    print("HINT4: You're so close!!! The number is less than or equal to 35")
                elif x > 35:
                    print("HINT4: You're so close!!! The number is greater than or equal to 35")

            if x > 50 and x <= 75:
                print("HINT3: The number is less than 75 and greater than 50, it could also be 75!!!")
                print("Let me give some more hints")
                if x <= 65:
                    print("HINT4: You're so close!!! The number is less than or equal to 65")
                elif x > 65:
                    print("HINT4: You're so close!!! The number is greater than or equal to 65")

            elif x > 50 and x > 75:
                print("HINT3: The number is greater than 75, it could also be 75!!!")
                print("Let me give some more hints")
                if x <= 85:
                    print("HINT4: You're so close!!! The number is less than or equal to 85")
                elif x > 85:
                    print("HINT4: You're so close!!! The number is greater than or equal to 85")

            print("Try again, You can do it")
            count += 1
            guess_the_number(count)


if __name__ == "__main__":
     x = random.randint(1, 100)
     #print(x) 

     print("Please note that the number to be guessed is in the range 1 to 100(both 1 and 100 included)")

     if x > 50:
        print("The number is greater than 50, it could also be 50!!!")
    
     elif x <= 50:
        print("The number is less than 50, it could also be 50!!!")

     guess_the_number(count)




