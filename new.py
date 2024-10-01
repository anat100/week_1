descriptions = {
    "hometown": """You are in your hometown.
            A small trading spot at the desert border.
            People are busy bartering goods and sharing stories.
            The scent of spices fills the air as camels pass by.
            The warm sun embraces you, and memories flood your mind.""",
    "desert": """You find yourself in a vast desert.
            Endless dunes stretch as far as the eye can see.
            The scorching sun beats down upon the golden sand.
            The heat shimmers in the distance, playing tricks on your eyes.
            You can hear the distant howl of a coyote, a testament to the harshness of this environment.""",
    "forest": """You are standing in the heart of a lush forest.
            Tall trees loom overhead, their canopies forming a natural roof.
            Sunlight filters through the leaves, creating dappled patterns on the ground.
            The air is crisp and filled with the earthy scent of moss and vegetation.
            You can hear the soft rustling of leaves and the melodic chirping of birds in the distance.""",
    "bee sanctuary": """You are at a bee sanctuary.
            Wooden beehives are arranged in neat rows.
            The air is filled with the gentle buzzing of bees at work.
            Sunflowers and lavender bloom nearby, providing a sweet fragrance.""",
    "clearing": """You have stumbled upon a peaceful clearing.
            The sun shines brightly overhead, illuminating the open space.
            Soft grass cushions your feet, inviting you to rest.
            The sound of a babbling brook can be heard nearby, adding to the tranquility.
            Colorful wildflowers bloom in abundance, painting the clearing with a vibrant palette.""" 
}

paths = {
    "hometown": ["bee sanctuary", "forest"],
    "forest": ["hometown", "desert"],
    "bee sanctuary": ["hometown", "clearing"],
    "desert": ["forest", "clearing"],
    "clearing": ["bee sanctuary", "desert"]
}

room = 'hometown'

print("""
Find the Magic Medal
===================

Your quest starts.
""")

while room != "clearing":
    print(f"You are in the {room} and have two possible options")
    print(", ".join(paths[room]))
    target = input("Where would you like to go? ")
    if target in paths[room]:
        room = target
        print(descriptions[room])
    else:
        print("Stop! There is no such place.")


print("""
On a hidden clearing you discover the Magic Medal.

Your quest has been successful!
""")
