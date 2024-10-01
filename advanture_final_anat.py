descriptions = {
        "hometown": """
                    You are in your home town... you have two options: \n
                    """,
        "the forest": """
                    There is a giant bear in the forest. You run away! \n
                    """, 
        "beekeeper": """"
                    You buy a pot of honey from the beekeeper \n
                    """,
        "clearing":"""
                    You chose correctly! \n
                    """  
}

paths = {
     "hometown" : ["beekeeper", "the forest"], 
     "the forest" : ["hometown", "beekeeper"],
     
}

room = "hometown"
honey = False

print("""

      ========================================

Find the Dragon Egg (hint: it's waiting for you at the clearing)

      =========================================

                    Your quest starts!
      
      =========================================
    
""")
      
print("""
      You are in your Homtown the loveliest town in the world!
      """)


while room != "clearing":
    print(f"You are in the {room} and have these possible options")
    print(" ".join(paths[room]))
    target = input("Where do you want to go next? \n")
    if target in paths[room]:
        room = target
        print(descriptions[room])
    
    else: 
         print(""""
               --------------------------------------------------------------
               Oh no! you are going the wrong way! Turn back and try again...
               --------------------------------------------------------------
               """)
       

         
  
print("""
On a hidden clearing you discover the dragon egg.

Your quest has been successful!
      
=========================
      YOU WIN!!!
=========================
""")
      