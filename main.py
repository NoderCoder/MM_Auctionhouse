from os import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap
# Path to your local Excel file
file_path = 'Murder-Mystery-party-Actions/Murder-Mystery-party-planning2.ods'

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
    'Business Travel','Indiana Jones',
]



#seperate list for post murder action items

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


for entry in character_post_murder_action_list:
    print(entry)


# # List of Characters : Each character's information is stored
characterBios = [
    ("Aden Smith", "Security and Spiritual Detail", "Swing from calm to angry rapidly. Talk passionately about spiritual matters, then criticize materialism angrily. Keep people guessing which side they’ll get."),
    ("Bennet Silverman", "VSC CEO", "Exude confidence in every movement. Make people feel special with your words while subtly steering conversations in your favor."),
    ("Brooklyn Weiss", "Banker", "Lean in close and whisper secrets, then laugh loudly. Talk with your hands and act overly familiar with everyone."),
    ("Calvin Mendelson", "Architect", "Speak slowly and deliberately. Smile only when something unpleasant happens to someone else. Be dismissive of emotional outbursts."),
    ("Carlos Rosenberg", "Popstar", "Keep the spotlight on yourself with grand gestures and bold stories. Correct others and make everything about your glamorous life. Laugh loudly at your own jokes."),
    ("Charles Penrose", "Chief of Security", "Move quietly, almost stealthily. Listen more than you speak, but when you do, speak quickly and decisively. Pay close attention to details."),
    ("Chloe Larkin", "Art Appraiser", "Speak sensibly and stay detached from drama. Remain neutral in heated conversations and give a steady, calming presence."),
    ("Dannielle Horowitz", "Survivalist", "Speak plainly without sugarcoating. Look others directly in the eyes and move with a purpose. Ignore trivial matters—focus on practical concerns."),
    ("Dennis Shapiro", "District Judge", "Speak with authority and correct others with a subtle air of superiority. Always look immaculate and adjust your attire often."),
    ("Dimitri Volkov", "Marketing Director", "Criticize everyone’s choices, especially in fashion or design. Raise an eyebrow when unimpressed and remain highly focused on your appearance."),
    ("Elaine Walker", "Auction Manager", "Never raise your voice, even in arguments. Keep your posture straight, and always appear composed. Deflect intrusive questions with a polite smile."),
    ("Fiona Gold", "VSC Intern", "Ask a lot of questions and take notes. Try too hard to fit in with the higher-ups. Work through every break and make sure everyone knows it."),
    ("Gabrial Katz", "Paleontologist", "Act distracted and daydreamy. Speak of grand ideas and theories while ignoring practical matters. Avoid manual labor at all costs."),
    ("Gina Silverman", "Shady Investor", "Focus intensely on discussions about money or profit. Be impatient when others talk about unimportant matters. Nod approvingly at anyone discussing deals or money."),
    ("Greyson Blau", "Bar Manager", "Stand with arms crossed and nod or shake your head curtly. Be direct in conversation and don’t waste time on small talk. Keep an eye on the exits."),
    ("Hugo Pierce", "Cocktail Expert", "Laugh too loudly and dominate the bar. Make cynical jokes and flirt with everyone—until the drinks run out, then get bitter."),
    ("Jack Adler", "Lawyer", "Cross your arms often and mutter under your breath. Roll your eyes at naive statements and give brutally honest opinions, whether asked or not."),
    ("Lisa Emerson", "Influencer", "Speak enthusiastically about the latest gossip. Be overly friendly, touch people’s arms while talking, and take selfies constantly."),
    ("Londyn Schneider", "Innovation Director", "Keep a calm and steady voice. Rarely show emotion, and pause before answering questions to seem deeply contemplative."),
    ("Marcus Mann", "Rancher", "Maintain good manners, but let unsettling comments slip out. Keep eye contact just a second too long and occasionally flash a predatory smile."),
    ("Margo Silverman", "Wealthy Socialite", "Use cutting remarks and deliver backhanded compliments. Keep your chin high, and look down at people—even if you’re shorter."),
    ("Mary Kaplan", "Art Director", "Take sudden risks in conversations—share daring opinions, then backtrack if challenged. Fidget when nervous, and speak too loudly when trying to impress."),
    ("Nina Drake", "Paparazzi", "Ask intrusive questions with an innocent smile. Carry a camera or notepad, and make lots of eye contact. Give people the sense you’re always listening."),
    ("Olivia Winchester", "Auctioneer", "Speak softly but clearly. Make everyone feel heard while carefully avoiding direct answers yourself. Defuse tension with humor and wit."),
    ("Paige Mendelson", "Engineer", "Offer to help others but remain distant. Speak plainly and never overreact. Keep a calm, observant eye on what others are doing."),
    ("Rafael Dupont", "Art Forger", "Use sophisticated language, admire the artwork excessively, and seem a little too knowledgeable about forgeries. Be generous with compliments that feel slightly rehearsed."),
    ("Roger Cohen", "Senior Journalist", "Speak in a low, controlled voice. Interrupt and dominate conversations. Always lead with questions that put others on the spot."),
    ("Roman Silverman", "VSC CFO", "Flatter everyone excessively while subtly competing for attention. Gossip, but get visibly defensive if the topic turns to you."),
    ("Ruby Silverman", "VSC COO", "Speak quickly, always on your way to somewhere more important. Drop hints about future plans and listen carefully for any useful information, but don’t get too attached to anyone."),
    ("Ted Cruz", "Senator", "Speak loudly and interrupt others with grand patriotic statements. Defend your position aggressively and change your opinion if it suits your mood."),
    ("Trenton Silverman", "Old Biz Owner", "Interrupt others when they speak, scoff at 'lesser' people’s ideas, and talk endlessly about your past successes. Turn up your nose at anything you find beneath you."),
    ("Vivan Thorne", "Art Curator", "Speak rapidly and get excited at the slightest hint of scandal. Casually hint at secrets you 'know' without giving them away fully."),
    ("Xavier King", "Accountant", "Speak quickly, stutter when nervous, and dominate the conversation to avoid scrutiny. Brag about small achievements as if they were monumental.")
]


# lists 
# # Display the result
# print(character_action_list[4])
# print(character_post_murder_action_list[4][2])
# print(character_item_to_find_list[4][2])

#combining lists here pre murder only
# Combine lists based on character names ////////////////////////////////////
# Combine lists based on character names
combined_list = []
for bio in characterBios:
    char_name, occupation, personality = bio  # Unpack name, occupation, and personality

    # Find matching entries in the other lists
    actions = next((action[2] for action in character_action_list if action[0] == char_name), "No actions found")
    items = next((item[2] for item in character_item_to_find_list if item[0] == char_name), "No items found")
    
    # Append combined tuple
    combined_list.append((char_name, personality, occupation, actions, items))

# # Print combined list
# for entry in combined_list:
#     print(entry)
print(combined_list[0])

#//////////////////////////////////////////////////////////
# Loading the base image and fonts
backgroundImage = Image.open('./Background/A4 character sheet.jpg')

# Load the custom font (Replace 'path/to/your/font.ttf' with the actual path)
font_path = './font/Pacifico-Regular.ttf'  # Ensure the font path is correct



font_size = 125
font = ImageFont.truetype(font_path, font_size)#titla
font2= ImageFont.truetype('./font/Benne-Regular.ttf', 70) #written text
font3= ImageFont.truetype('./font/ABeeZee-Regular.ttf', 75) # occupation
font4= ImageFont.truetype('./font/Benne-Regular.ttf', 70) #Heading

# 77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

# Setting up image 
img_width, img_height = backgroundImage.size
image = backgroundImage.copy()
draw = ImageDraw.Draw(image)





# Function to wrap text to fit a column width
def wrap_text_to_width(draw, text, font, max_width):
    """Breaks text into lines that fit within max_width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        # Test current line with the new word
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]  # Calculate the text width

        if line_width <= max_width:
            current_line.append(word)
        else:
            # Add current line to lines and start a new line
            lines.append(" ".join(current_line))
            current_line = [word]

    # Add the last line
    if current_line:
        lines.append(" ".join(current_line))

    return lines
# Max column width in pixels
column_width = 2000







# Function to split text by `-` and ensure it fits within the specified column width
def split_text_on_symbol(draw, text, font, max_width, symbol="-"):
    """Splits text into lines based on the specified symbol and wraps to fit within max_width."""
    # Split the text by the symbol
    parts = text.split(symbol)
    lines = []

    for part in parts:
        # Wrap each part to fit within the column width
        part_lines = wrap_text_to_width(draw, part.strip(), font, max_width)
        lines.extend(part_lines)  # Add wrapped lines for each part

    return lines


#Printtttttttttttttttttt
    
# Loop through the combined list
for char_name, personality, occupation, actions, items in combined_list:
    # Use a fresh copy of the background image for each character
    image = backgroundImage.copy()
    draw = ImageDraw.Draw(image)
    
    # Starting position for text
    x, y = 150, 150  # Adjust x and y for starting text position
    line_spacing = 150  # Adjust space between lines
    
    # Write the character's details + occupation
    draw.text((x, y), f"{char_name}", fill="darkred", font=font)
    draw.text((x+1000, y+75), f"{occupation}", fill="black", font=font3)
    y += line_spacing

    draw.text((x, y+120), "Personality:", fill="darkred", font=font3)
    y = y+100
    personality_lines = wrap_text_to_width(draw, personality, font2, column_width)
    for line in personality_lines:
        draw.text((x, y+120), line, fill="black", font=font2)
        y = y+80





        # actions text
    draw.text((x, y+300), "Actions:", fill="darkred", font=font3)
    y =y+100
    actions_lines1 = split_text_on_symbol(draw, actions, font4, column_width)
    for line in actions_lines1:
        draw.text((x, y+300), line, fill="black", font=font2)
        y = y+80

    #actions ot find
    draw.text((x, y+400), f"Auction item that you want: {items}", fill="darkred", font=font2)
    

    
    # Save the output for the current character
    output_filename = f'./ActionCards/{char_name}.jpg'
    image.save(output_filename)
#////////////////////////////////////

