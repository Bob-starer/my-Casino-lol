import random
import time

rewards = ["Nothing", "One more spin", "Win!"]
loss_messages = ["Crikey mate, you blew the whole bloody lot? You're a proper drongo, couldn't pick a winner if it slapped ya in the face!", "You lost", "Try again I guess.. or finally get a job"]

def spin():
    print("spinning the wheel...")
    time.sleep(0.5)
    item_received = random.choice(rewards)
    if item_received == "Win!":
        print("YOU WON!!!! YEAAAAHHAHAHAHHAhA")
    if item_received == "Nothing":
        print(random.choice(loss_messages))
    if item_received == "One more spin":
        spin
for a in range(3):
    print( )
print("########## Welcome to Casino Monte Carlo! ##########")
choice = input("Type SPIN to spin the wheel!: ")
if choice == "SPIN":
    spin()
else:
    print("please type SPIN, not something else")


