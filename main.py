from os import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import openai


openai.api_key = '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'


# Function to generate image from a text prompt
prompt = "An astronaut lounging in a tropical resort in space, pixel art"
model = "dall-e-3"


def main() -> None:
    # Generate an image based on the prompt
    response = openai.images.generate(prompt=prompt, model=model)

    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()

# List of Characters : Each character's information is stored as a tuple, where the first item is the name and the second is the occupation.

# characters = [
#     ("Sabastian Crane", "Professional Card Player", "black"),
#     ("Rafael Dupont", "Art Forger", "grey"),
#     ("Trenton Silverman", "Old Business Owner", "white"),
#     # Add the rest of your characters here...
# ]

characters = [
    ["Sabastian Crane", "Professional Card Player", "black", ["Evil", "Respectable"]],
    ["Rafael Dupont", "Art Forger", "grey", ["Open", "Sophisticated"]],
    ["Trenton Silverman", "Old Business Owner", "white", ["Arrogant", "Snotty"]],
    ["Ruby Silverman", "VSC COO", "grey", ["Visionary", "Focused"]],
    ["Roman Silverman", "VSC CFO", "blue", ["Social Butterfly", "Envious"]],
    ["Mary Kaplan", "Art Director", "blue", ["Risk-taker", "Insecure"]],
    ["Carlos Rosenberg", "Popstar", "white", ["Pompous", "Arrogant"]],
    ["Nina Drake", "Paparazzi", "white", ["Bubbly", "Inquisitive"]],
    ["Calvin Mendelson", "Architect", "grey", ["Calm", "Cruel"]],
    ["Paige Mendelson", "Engineer", "blue", ["Tolerant", "Devoted"]],
    ["Brooklyn Weiss", "Banker", "red", ["Loose-lipped", "Rumor Mill"]],
    ["Greyson Blau", "Bar Manager", "white", ["Tough Guy", "Disciplined"]],
    ["Roger Cohen", "Senior Journalist", "blue", ["Sinister", "Controlling"]],
    ["Lisa Emerson", "Influencer", "grey", ["Responsible", "Flashy"]],
    ["Bennet Silverman", "VSC CEO", "black", ["Resourceful", "Affluent", "Dishonest"]],
    ["Margo Lane", "Wealthy Socialite", "black", ["Strong", "Snippy"]],
    ["Dimitri Volkov", "Marketing Director", "black", ["Obsessed", "Judgmental"]],
    ["Gina Zimmerman", "Shady Investor", "blue", ["Bright", "Greedy"]],
    ["Londyn Schneider", "Innovation Director", "black", ["Stoic", "Frugal"]],
    ["Gabriel Katz", "Paleontologist", "black", ["Entitled", "Dreamy"]],
    ["Dannielle Horowitz", "Survivalist", "black", ["Self-reliant", "Knowledgeable"]],
    ["Elaine Walker", "Auction Manager", "white", ["Calm", "Poised"]],
    ["Evan Levy", "Company Food Director", "grey", ["Adaptable", "Ambitious"]],
    ["Jayden Mizrahi", "Data Scientist", "grey", ["Persistent", "Witty"]],
    ["Jack Adler", "Lawyer", "blue", ["Grumpy", "Self-motivated"]],
    ["Charles Penrose", "Chief of Security", "white", ["Clever", "Cunning"]],
    ["Vivan Thorne", "Art Curator", "blue", ["Gossipy", "Observant"]],
    ["Fiona Gold", "VSC Intern", "blue", ["Workaholic", "Prideful"]],
    ["Olivia Winchester", "Auctioneer", "white", ["Charming", "Eloquent", "Affable"]],
    ["Dennis Shapiro", "District Judge", "grey", ["Refined", "Meticulous"]],
    ["Xavier King", "Accountant", "black", ["Anxious", "Voluble", "Egotist"]],
    ["Chloe Larkin", "Art Appraiser", "grey", ["Independent", "Reliable"]],
    ["Aden Smith", "Security and Spiritual Detail", "black", ["Angry", "Underpaid", "Spiritual"]],
    ["Ted Cruz", "Senator", "patriotic", ["Belligerent", "Patriotic", "Erratic"]],
    ["Hugo Pierce", "Cocktails Expert", "blue", ["Self-serving", "Alcoholic"]],
    ["Ivy Prescott", "Chemist", "grey", ["Materialistic", "Self-motivated"]]
]




















# For printing
# Loading the base image and fonts
backgroundImage = Image.open('./Background/MM_invite_12_7_1.jpg')

# Load the custom font (Replace 'path/to/your/font.ttf' with the actual path)
font_path = './font/ABeeZee-Regular.ttf'  # Ensure the font path is correct
font_size = 60
font = ImageFont.truetype(font_path, font_size)
font2= ImageFont.truetype('./font/Benne-Regular.ttf', 48)


# loop to unpack and print each element in the List
for idx, (name, occupation, color, traits) in enumerate(characters):
    # Load a base image (or create a blank image)
    image = backgroundImage.copy()
    draw = ImageDraw.Draw(image)

    # Get the image size and center points
    img_width, img_height = image.size
    x = (img_width / 2) - 500
    y = (img_width / 2) + 300

    # Set up text positions
    name_position = (x, y)  # Coordinates for the name
    occupation_position = (x, y + 90)  # Coordinates for the occupation
    dresscode_position = (x, y + 155)  # Coordinates for the color (dress code)
    last_line_position = (x, y + 220)

    # Draw each line of text
    draw.text(name_position, f"Name: {name}", font=font, fill="red")
    draw.text(occupation_position, f"Character: {occupation}", font=font2, fill="red")
    draw.text(dresscode_position, f"Dress code: {color.capitalize()} attire", font=font2, fill="red")
    draw.text(last_line_position, "reflecting your character attending an auction", font=font2, fill="red")

    # Save the modified image with a unique filename
    output_filename = f'./Invites/{name}_{idx + 1}.jpg'
    image.save(output_filename)
    print(f"Saved: {output_filename}")
    #print(f"Name: {name}, Occupation: {occupation}, Favorite Color: {color}")