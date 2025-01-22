import random

# Expanded word pools
word_pools = {
    "adjective": [
        "dark", "bright", "silent", "eerie", "funny", "brave", "mysterious", "beautiful", "serene", "haunting",
        "golden", "ancient", "ethereal", "melancholy", "vivid", "wild", "turbulent", "tranquil", "fiery", "glimmering"
    ],
    "noun": [
        "forest", "moon", "treasure", "shadow", "dream", "laugh", "kiss", "adventure", "mountain", "ocean",
        "river", "flame", "soul", "storm", "whisper", "path", "castle", "glow", "void", "horizon", "mist", "blade"
    ],
    "verb": [
        "whispered", "screamed", "laughed", "cried", "shone", "wandered", "bloomed", "roared", "danced", "echoed",
        "embraced", "lingered", "drifted", "rose", "fell", "glided", "sang", "rushed", "vanished", "soared", "thundered"
    ]
}

# Themes and templates
poem_templates = {
    "horror": [
        "In the {adjective} shadows, the {noun} {verb}.",
        "A {adjective} chill grips the {noun},",
        "The {noun} {verb} as night takes its {noun}.",
        "Fear {verb} through the {adjective} {noun}."
    ],
    "comedy": [
        "A {adjective} {noun} tripped on a {noun},",
        "It {verb} and {verb}, quite the {adjective} sight!",
        "With a {noun} in hand and a {adjective} grin,",
        "It left everyone {verb} till the end of the {noun}."
    ],
    "romance": [
        "Beneath the {adjective} {noun}, our love did {verb}.",
        "Your {adjective} {noun} shone brighter than the {noun}.",
        "With each {noun}, our hearts {verb} as one.",
        "Forever in this {adjective} {noun}, I will {verb} you."
    ],
    "adventure": [
        "Over the {adjective} {noun}, we {verb} with might,",
        "Seeking the {noun} in the {adjective} night.",
        "Our {noun} {verb} through the {adjective} lands,",
        "A {noun} of glory lay within our hands."
    ]
}

# Generate a random line using placeholders
def generate_line(template):
    return template.format(
        adjective=random.choice(word_pools["adjective"]),
        noun=random.choice(word_pools["noun"]),
        verb=random.choice(word_pools["verb"])
    )

# Generate a poem based on a theme and length
def generate_poem(theme, length=4):
    if theme not in poem_templates:
        return "Sorry, that theme is not available."
    templates = poem_templates[theme]
    poem = [generate_line(random.choice(templates)) for _ in range(length)]
    return "\n".join(poem)

# Main program
def main():
    print("Welcome to the Poem Generator!")
    print("Available themes: horror, comedy, romance, adventure")
    theme = input("Choose a theme: ").strip().lower()
    try:
        length = int(input("Enter the number of lines for your poem (e.g., 4, 6, 8): "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Setting poem length to 4 lines.")
        length = 4

    # Generate the poem
    print("\nHere is your poem:\n")
    poem = generate_poem(theme, length)
    print(poem)

    # Save option
    save_option = input("\nWould you like to save this poem to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        filename = f"{theme}_poem.txt"
        with open(filename, "w") as file:
            file.write(poem)
        print(f"Poem saved as '{filename}'!")

if __name__ == "__main__":
    main()
