'''
A user is trying to decide whether to go out tonight.
Write a script which asks her a few yes-no questions and decides for her according to the following scheme: [NO SCHEME]
'''

raining = input("Is it raining? ")
if raining == "yes":
    netflix = input("Is the new episode on Netflix out already? ")
    if netflix == "yes":
        print("Stay home")
    elif netflix == "no":
        umbrella = input("Damn it. Do you have an umbrella? ")
        if umbrella == "yes":
            drinking = input("Do you feel like drinking tonight? ")
            if drinking == "yes":
                print("Go, then!")
            elif drinking == "no":
                sure = input("Yeah, right. You sure? ")
                if sure == "yes":
                    print("What a drag! Stay home.")
                elif sure == "no":
                    print("You gotta go out.")
        elif umbrella == "no":
            sugar = input("Are you made of sugar? ")
            if sugar == "yes":
                print("Being moody? Go to sleep, honey")
            elif sugar == "no":
                print("Dress up and leave")
elif raining == "no":
    reason = input("Do you need another reason? ")
    if reason == "yes":
        print("World sucks. Go out!")
    elif reason == "no":
        print("Are you still here?")
