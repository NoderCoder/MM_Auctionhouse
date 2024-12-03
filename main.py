from os import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Path to your local Excel file
file_path = 'Murder-Mystery-party-Actions/Murder-Mystery-party-planning.ods'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)
# Select columns for the operation
character_name_col = 'Character name'
character_role_col = 'Character role'
post_murder_col = 'Post murder actions'
items_to_find_col = 'Items to find'
storyline_columns = [
    'Love Trianle story line',
    'Auction house Story line',
    'Inheritance and stocks',
    'Underpaid Performance',
    'Vanishing Necklace',
    'Hidden Appraisal',
    'The Secret Affair',
    'Insider Trading Leak',
    'Business Travel'
]

# Function to merge storylines into bullet points
def merge_storylines(row, columns):
    return '\n'.join(f"- {str(row[col]).strip()}" for col in columns if pd.notna(row[col]))

# Add a new column for the merged storylines
df['Merged Storylines'] = df.apply(merge_storylines, columns=storyline_columns, axis=1)

# Create the filtered DataFrame
filtered_df = df[[character_name_col, character_role_col, 'Merged Storylines']]
filtered_df_post_murder = df[[character_name_col, character_role_col, post_murder_col]]
filtered_df_item_find = df[[character_name_col, character_role_col, items_to_find_col]]

# Convert the filtered DataFrame into a list of tuples
character_action_list = list(filtered_df.itertuples(index=False, name=None))
character_post_murder_action_list = list(filtered_df_post_murder.itertuples(index=False, name=None))
character_item_to_find_list = list(filtered_df_item_find.itertuples(index=False, name=None))


# Display the result
print(character_action_list[4])
print(character_post_murder_action_list[4][2])
print(character_item_to_find_list[4][2])

#program to print the files


# List of Characters : Each character's information is stored
characterBios = [
    ("Aden Smith", "Security and Spiritual Detail", "When people become famous, they need both security and spiritual advice, and that's what Aden provides to the pop star Carlos Rosenberg. For a huge fee."),
    ("Bennet Silverman", "VSC CEO", "Bennet is the oldest son of old Grandpa Trenton and is the first person in VSC. A charmer with an agenda, Bennet can weave a tale so convincing you'll wonder if it\'s all true."),
    ("Brooklyn Weiss", "Banker", "You know Brooklyn if you are in the right financial circles. She is the one to go to if you need a loan. She can't afford anything to stay secret around her for too long."),
    ("Calvin Mendelson", "Architect", "A respectable employee of VSC, Calvin's smile never quite reaches his eyes. He's the architect of more than just buildings."),
    ("Carlos Rosenberg", "Popstar", "Carlos is a local celebrity. His arrogance is as brash as his fashion choices. When he's around, you\'ll hear him before you see him—just the way he likes it."),
    ("Charles Penrose", "Chief of Security", "Charles is in charge of maintaining order in the auction house. His cool demeanor and calculating eyes make you wonder just how much he\'s hiding."),
    ("Chloe Larkin", "Art Appraiser", "Chloe is a long-time contractor of the Auction House, and her reliability is legendary. But loyalty only goes so far when her interests are at stake."),
    ("Dannielle Horowitz", "Survivalist", "Tough, smart, and fiercely independent, Dannielle knows how to handle any situation. She likes collecting underpriced ancient items; they give her Indiana Jones vibes."),
    ("Dennis Shapiro", "District Judge", "Judge Shapiro likes to attend auctions, where he looks for rare species of antiques and crooks. His obsession with justice leaves little room for compassion."),
    ("Dimitri Volkov", "Marketing Director", "A big shot in VSC, Dimitri values his position. His style is impeccable, his smile is dazzling, and his critiques are scathing."),
    ("Elaine Walker", "Auction Manager", "Elaine has been running events like this for the Auction House forever. Always impeccably composed, she seems immune to chaos."),
    ("Evan Levy", "Company Food Director", "A rare example of a VSC employee who is valued by everyone. Evan's hunger for success matches his appetite for gourmet food."),
    ("Fiona Gold", "VSC Intern", "Fiona just started as an intern at VSC. Her relentless drive has earned her a reputation as a workhorse, but ambition is a double-edged sword."),
    ("Gabriel Katz", "Paleontologist", "A regular at auctions, Gabriel\'s dreamy expression and wandering gaze suggest he has his head in the clouds — until he turns those perceptive eyes on you."),
    ("Gina Zimmerman", "Shady Investor", "Business is a game, and she plays to win — no matter the cost. Gina thinks she made her main investment by planning to marry Roman Silverman, the CFO."),
    ("Greyson Blau", "Bar Manager", "The Auction House values people like Greyson. He is everywhere and all at once. Greyson is a man of principle — if you play by his rules."),
    ("Hugo Pierce", "Cocktail Expert", "Employed by the Auction House, loved and despised by many. Hugo\'s charm is intoxicating, but his loyalty runs only as deep as the bottom of his glass."),
    ("Ivy Prescott", "Chemist", "Nobody knows why Ivy likes to attend auctions. Her drive is as ruthless as her chemistry experiments."),
    ("Jack Adler", "Lawyer", "You may wonder why the Auction House even needs a lawyer at their events! Jack's blunt attitude doesn\'t win him many friends, but he couldn\'t care less."),
    ("Jayden Mizrahi", "Data Scientist", "Working to increase ad revenues in VSC, Jayden\'s sharp wit and infectious laugh make her a delight to be around."),
    ("Lisa Emerson", "Influencer", "Flashy and fabulous, Lisa lives for likes and follows. Drama is her bread and butter, and an auction is the perfect place to get it."),
    ("Londyn Schneider", "Innovation Director", "Londyn is convinced he drives VSC forward. Every move is calculated, every decision measured. He\'s a man of few words but many thoughts."),
    ("Marcus Mann", "Rancher", "First time seen at an auction, Marcus is the perfect rancher — straightforward, dependable, and courteous, but just on the surface."),
    ("Margo Lane", "Wealthy Socialite", "A respectable auction like this is the place to be for Margo. Elegant and entitled, she is quick to throw shade and quicker to defend herself."),
    ("Mary Kaplan", "Art Director", "Mary is an art director at VSC. Behind her confident front, there's a lingering fear that she\'s one misstep away from losing it all."),
    ("Nina Drake", "Paparazzi", "There are many reasons for a paparazzi to attend an auction. If there's gossip to be found, she\'s already taken the picture."),
    ("Olivia Winchester", "Auctioneer", "Olivia is the one in the Auction House who runs the show. With her honeyed voice and silver tongue, she could sell sand in the desert."),
    ("Paige Mendelson", "Engineer", "An employee of VSC, Paige has the patience of a saint and the loyalty of a hound, but even she has limits."),
    ("Rafael Dupont", "Art Forger", "Why would an art forger attend an auction? Known for his charm and refined taste, Rafael is a master of illusion."),
    ("Roger Cohen", "Senior Journalist", "Roger doesn\'t just report the news—he makes it. His influence runs deep, and those who cross him often find their dirty laundry making headlines."),
    ("Roman Silverman", "VSC CFO", "Roman is a son of old Grandpa Trenton and manages the financial side of VSC. Roman thrives in the social spotlight and is always jealous of his fiancée Gina Zimmerman."),
    ("Ruby Silverman", "VSC COO", "Although the only daughter of Grandpa Trenton, Ruby didn't grow up spoiled. Sharp-witted and shrewd, she\'s not one to be underestimated."),
    ("Ted Cruz", "Senator", "Ted\'s loud opinions and unpredictable behavior make him hard to handle. He's a patriot... if only you could figure out whose side he's on."),
    ("Trenton Silverman", "Old Biz Owner", "Old Grandpa Trenton founded VSC and has been running it for longer than anyone can remember. His sneer speaks louder than any words."),
    ("Vivian Thorne", "Art Curator", "Vivian\'s gossip is as reliable as her taste in art, and she loves nothing more than a scandal—especially if she\'s the one to break it."),
    ("Xavier King", "Accountant", "Xavier thinks he\'s the kind of guy in VSC who gets work done. He always knows something you don\'t — until he spills.")
]




# For printing
# Loading the base image and fonts
backgroundImage = Image.open('./Background/Character list long jpeg copy.jpg')

# Load the custom font (Replace 'path/to/your/font.ttf' with the actual path)
font_path = './font/Pacifico-Regular.ttf'  # Ensure the font path is correct



font_size = 46
font = ImageFont.truetype(font_path, font_size)
font2= ImageFont.truetype('./font/Benne-Regular.ttf', 38)
font3= ImageFont.truetype('./font/ABeeZee-Regular.ttf', 40)

# 77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777







# 77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

# Setting up image 
img_width, img_height = backgroundImage.size
# loop to unpack and print each element in the List
for idx, (name, occupation, bio) in enumerate(characterBios):
    # Load a base image (or create a blank image)
    image = backgroundImage.copy()
    draw = ImageDraw.Draw(image)

# Settings for text placement
column_size = 100
x, y = column_size, 150  # Starting position for the first column
x2, y2 = 1300, 620  # Starting position for the second column
line_spacing = 5  # Space between lines for names
bio_line_spacing = 5  # Space between lines for bios
wrap_width = 60  # Number of characters per line before wrapping

# Helper function for text wrapping
def wrap_text(text, wrap_width):
    """Wraps text to fit within a certain width."""
    words = text.split(" ")
    wrapped_lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= wrap_width:
            current_line += (word + " ")
        else:
            wrapped_lines.append(current_line.strip())
            current_line = word + " "
    wrapped_lines.append(current_line.strip())
    return wrapped_lines

# Split the characters between the two columns
half_index = len(characterBios) // 2
first_column_bios = characterBios[:half_index+2]
second_column_bios = characterBios[half_index:]
second_column_bios = second_column_bios[2:]
# del second_column_bios[1]




# Write the first column
for name,occupation, bio in first_column_bios:
    # Draw the name
    draw.text((x, y), name, font=font, fill="darkred")
    name_text_height = font.getbbox(name)[3]  # The height of the name text
    
# Ops adding the job
    draw.text((x+450, y+20),"("+ occupation + ")", font=font3, fill="darkorange")
    
    
    y += name_text_height + line_spacing  # Move down for bio


    # Wrap and draw the bio
    wrapped_bio = wrap_text(bio, wrap_width)
    for line in wrapped_bio:
        draw.text((x, y), line, font=font2, fill="black")
        bio_text_height = font2.getbbox(line)[3]  # The height of each line in the bio
        y += bio_text_height + bio_line_spacing  # Move down for the next bio line

    # Add extra space after each character bio
    y += line_spacing * 3

# Write the second column
for name, occupation, bio in second_column_bios:
    # Draw the name
    draw.text((x2, y2), name + ":", font=font, fill="darkred")
    name_text_height = font.getbbox(name)[3]  # The height of the name text

    draw.text((x2+450, y2+20),"("+ occupation + ")", font=font3, fill="darkorange")

    y2 += name_text_height + line_spacing  # Move down for bio

    # Wrap and draw the bio
    wrapped_bio = wrap_text(bio, wrap_width)
    for line in wrapped_bio:
        draw.text((x2, y2), line, font=font2, fill="black")
        bio_text_height = font2.getbbox(line)[3]  # The height of each line in the bio
        y2 += bio_text_height + bio_line_spacing  # Move down for the next bio line

    # Add extra space after each character bio
    y2 += line_spacing * 3

# Save the result
output_filename = './character_bios_two_columns.jpg'
image.save(output_filename)
print(f"Saved: {output_filename}")