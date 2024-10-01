print("""
Find the Dragon Egg
===================

Your quest starts.
""")
      
room = "hometown"
honey = False
rooms = ['hometown', 'the forest', 'beekeeper', 'clearing'] # list rooms that are in my game


print("""
      You are in your Homtown, the loveliest town in the world
      """)

print("""
      Where would you like to go next
      hometown
      the forest
      beekeeper
      """)



while room != "clearing":
    # print(f"You are in {room}")
    target = input("Where would you like to go? ")
    if target in rooms:
          room = target
    else:
          print("Stop! There is no such place.")
          # room = target
    if room == "hometown":
       print("""You are in your hometowm.
            """)
       room = "hometown"
       

    elif room == "the forest":
              print(" You leave the honeypot for the bear and sneak out. You are in the forest")
              honey = True # you can use the honey only once
              room = "the forest"

    elif room == "beekeeper" and not honey:
               print("you buy a pot of honey from the beekeeper")
               honey = True
               room = "beekeeper"
               
    # else:
          # print("you find yourself in a mysterious room. You sense it has a wierd vibe")

print("""
On a hidden clearing you discover the dragon egg.

Your quest has been successful!
""")
      