
# CAR GAME ----------------------
user_command = "" #empty string
started = False #checking if car started
while True: #block of code gets executed until break.
    user_command=input("> ").lower()
    if user_command=="start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started")

    elif user_command=="stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped")

    elif user_command=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif user_command=="quit":
        print("Bubye!")
        break
    else:
        print("Sorry I don't understand")




