from os import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# List of Characters : Each character's information is stored as a tuple, where the first item is the name and the second is the occupation.

# characters = [
#     ("Sabastian Crane", "Professional Card Player", "black"),
#     ("Rafael Dupont", "Art Forger", "grey"),
#     ("Trenton Silverman", "Old Business Owner", "white"),
#     # Add the rest of your characters here...
# ]

characters = [
    ("Ted Cruz","Senator", "patriotic"),
    ("Sabastian Crane", "Professional Card Player", "black"),
    ("Rafael Dupont", "Art Forger", "grey"),
    ("Trenton Silverman", "Old Business Owner", "white"),
    ("Ruby Silverman", "VSC Chief Operating Officer", "grey"),
    ("Roman Silverman", "VSC Chief Financial Officer", "blue"),
    ("Mary Kaplan", "Art Director", "blue"),
    ("Carlos Rosenberg", "Pop Star", "white"),
    ("Nina Drake", "Paparazzi", "white"),
    ("Calvin Mendelson", "Architect", "grey"),
    ("Paige Mendelson", "Engineer", "blue"),
    ("Brooklyn Weiss", "Banker", "red"),
    ("Greyson Blau", "Bar Manager", "white"),
    ("Roger Cohen", "Senior Journalist", "blue"),
    ("Lisa Emerson", "Influencer", "grey"),
    ("Bennet Silverman", "VSC Chief Executive Officer", "black"),
    ("Margo Lane", "Wealthy Socialite", "black"),
    ("Dimitri Volkov", "Marketing Director", "black"),
    ("Gina Zimmerman", "Shady Investor", "blue"),
    ("Londyn Schneider", "Innovation Director", "black"),
    ("Gabrial Katz", "Paleontologist", "black"),
    ("Dannielle Horowitz", "Survivalist", "black"),
    ("Elaine Walker", "Auction Manager", "white"),
    ("Evan Levy", "Company Food Director", "grey"),
    ("Jayden Mizrahi", "Data Scientist", "grey"),
    ("Jack Adler", "Lawyer", "blue"),
    ("Ivy Prescott", "Chemist", "grey"),
    ("Charles Penrose", "Chief of Security", "white"),
    ("Vivan Thorne", "Art Curator", "blue"),
    ("Fiona Gold", "VSC Intern", "blue"),
    ("Olivia Winchester", "Auctioneer", "white"),
    ("Dennis Shapiro", "District Judge", "grey"),
    ("Xavier King", "Accountant", "black"),
    ("Chloe Larkin", "Art Appraiser", "grey"),
    ("Hugo Pierce", "Art Dealer", "blue"),
    ("Aden Smith", "Security & Spiritual Detail", "black"),
    ("Alice Thornton", "Bartender", "white")

]

# Loading the base image and fonts
backgroundImage = Image.open('./Background/MM_invite_12_7_1.jpg')

# Load the custom font (Replace 'path/to/your/font.ttf' with the actual path)
font_path = './font/ABeeZee-Regular.ttf'  # Ensure the font path is correct
font_size = 60
font = ImageFont.truetype(font_path, font_size)
font2= ImageFont.truetype('./font/Benne-Regular.ttf', 48)



# For loop to unpack and print each element in the tuple
for idx, (name, occupation, color) in enumerate(characters):
    # Load a base image (or create a blank image)
    image = backgroundImage.copy()
    draw = ImageDraw.Draw(image)

    # Get the image size and center points
    img_width, img_height = image.size
    x=(img_width/2)-500
    y=(img_width/2)+ 300
    
    # Set up text positions
    name_position = (x, y)  # Coordinates for the name
    occupation_position = (x, y+90)  # Coordinates for the occupation
    dresscode_position = (x, y+155)  # Coordinates for the color (dress code)
    last_line_position = (x,y+220)
    
    # Draw each line of text
    draw.text(name_position, f"Name: {name}", font=font, fill="red")
    draw.text(occupation_position, f"Character: {occupation}", font=font2, fill="red")
    draw.text(dresscode_position, f"Dress code : {color.capitalize()} attire,", font=font2, fill="red")
    draw.text(last_line_position, f"reflecting your character attending an auction", font=font2, fill="red")
    #reflecting your character attending auction
    # Save the modified image with a unique filename
    output_filename = f'./Invites/{name}_{idx + 1}.jpg'
    image.save(output_filename)
    print(f"Saved: {output_filename}")
    print(y)
    #print(f"Name: {name}, Occupation: {occupation}, Favorite Color: {color}")