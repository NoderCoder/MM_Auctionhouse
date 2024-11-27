from os import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import openai


openai.api_key = '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'


# List of Characters : Each character's information is stored as a tuple, where the first item is the name and the second is the occupation.

# characters = [
#     ("Sabastian Crane", "Professional Card Player", "black"),
#     ("Rafael Dupont", "Art Forger", "grey"),
#     ("Trenton Silverman", "Old Business Owner", "white"),
#     # Add the rest of your characters here...
# ]

# characters = [
#     ["Sabastian Crane", "Professional Card Player", "black", ["Evil", "Respectable"]],
#     ["Rafael Dupont", "Art Forger", "grey", ["Open", "Sophisticated"]],
#     ["Trenton Silverman", "Old Business Owner", "white", ["Arrogant", "Snotty"]],
#     ["Ruby Silverman", "VSC COO", "grey", ["Visionary", "Focused"]],
#     ["Roman Silverman", "VSC CFO", "blue", ["Social Butterfly", "Envious"]],
#     ["Mary Kaplan", "Art Director", "blue", ["Risk-taker", "Insecure"]],
#     ["Carlos Rosenberg", "Popstar", "white", ["Pompous", "Arrogant"]],
#     ["Nina Drake", "Paparazzi", "white", ["Bubbly", "Inquisitive"]],
#     ["Calvin Mendelson", "Architect", "grey", ["Calm", "Cruel"]],
#     ["Paige Mendelson", "Engineer", "blue", ["Tolerant", "Devoted"]],
#     ["Brooklyn Weiss", "Banker", "red", ["Loose-lipped", "Rumor Mill"]],
#     ["Greyson Blau", "Bar Manager", "white", ["Tough Guy", "Disciplined"]],
#     ["Roger Cohen", "Senior Journalist", "blue", ["Sinister", "Controlling"]],
#     ["Lisa Emerson", "Influencer", "grey", ["Responsible", "Flashy"]],
#     ["Bennet Silverman", "VSC CEO", "black", ["Resourceful", "Affluent", "Dishonest"]],
#     ["Margo Lane", "Wealthy Socialite", "black", ["Strong", "Snippy"]],
#     ["Dimitri Volkov", "Marketing Director", "black", ["Obsessed", "Judgmental"]],
#     ["Gina Zimmerman", "Shady Investor", "blue", ["Bright", "Greedy"]],
#     ["Londyn Schneider", "Innovation Director", "black", ["Stoic", "Frugal"]],
#     ["Gabriel Katz", "Paleontologist", "black", ["Entitled", "Dreamy"]],
#     ["Dannielle Horowitz", "Survivalist", "black", ["Self-reliant", "Knowledgeable"]],
#     ["Elaine Walker", "Auction Manager", "white", ["Calm", "Poised"]],
#     ["Evan Levy", "Company Food Director", "grey", ["Adaptable", "Ambitious"]],
#     ["Jayden Mizrahi", "Data Scientist", "grey", ["Persistent", "Witty"]],
#     ["Jack Adler", "Lawyer", "blue", ["Grumpy", "Self-motivated"]],
#     ["Charles Penrose", "Chief of Security", "white", ["Clever", "Cunning"]],
#     ["Vivan Thorne", "Art Curator", "blue", ["Gossipy", "Observant"]],
#     ["Fiona Gold", "VSC Intern", "blue", ["Workaholic", "Prideful"]],
#     ["Olivia Winchester", "Auctioneer", "white", ["Charming", "Eloquent", "Affable"]],
#     ["Dennis Shapiro", "District Judge", "grey", ["Refined", "Meticulous"]],
#     ["Xavier King", "Accountant", "black", ["Anxious", "Voluble", "Egotist"]],
#     ["Chloe Larkin", "Art Appraiser", "grey", ["Independent", "Reliable"]],
#     ["Aden Smith", "Security and Spiritual Detail", "black", ["Angry", "Underpaid", "Spiritual"]],
#     ["Ted Cruz", "Senator", "patriotic", ["Belligerent", "Patriotic", "Erratic"]],
#     ["Hugo Pierce", "Cocktails Expert", "blue", ["Self-serving", "Alcoholic"]],
#     ["Ivy Prescott", "Chemist", "grey", ["Materialistic", "Self-motivated"]]
# ]


# tempcharacterBios = [
#     ("Marcus Mann", "A rancher who wears his respectability like a well-tailored suit, but there\'s something sinister lurking beneath his polite demeanor."),
#     ("Rafael Dupont", "An art forger with a talent for fakes and a knack for elegant deception. He\'s open, refined, and just dangerous enough to be fascinating."),
#     ("Trenton Silverman", "A business mogul with a nose for money and a scowl for everyone else. His arrogance is matched only by his disdain for 'lesser' folk."),
#     ("Ruby Silverman", "A visionary COO who\'s always three steps ahead. Her laser focus hides a ruthless ambition she keeps just out of sight.")]
characterBios = [
    ("Aden Smith", "Security and Spiritual Detail", "Calm one minute, fiery the next—Aden/'s spirituality is as intense as his temper. You never know if you/'re getting the monk or the brawler."),
    ("Bennet Silverman", "VSC CEO", "A charmer with an agenda, Bennet can weave a tale so convincing you'll wonder if it/'s all true. Those who trust him too easily often regret it."),
    ("Brooklyn Weiss", "Banker", "Nothing stays secret for long around Brooklyn. She/'s the first to know—and the first to tell—when there/'s a story worth spreading."),
    ("Calvin Mendelson", "Architect", "Calm, composed, and terrifyingly calculating, Calvin's smile never quite reaches his eyes. He's the architect of more than just buildings."),
    ("Carlos Rosenberg", "Popstar", "Always the center of attention, Carlos's arrogance is as brash as his fashion choices. When he's around, you/'ll hear him before you see him—just the way he likes it."),
    ("Charles Penrose", "Chief of Security", "Charles has a knack for knowing things he shouldn/'t. His cool demeanor and calculating eyes make you wonder just how much he/'s hiding."),
    ("Chloe Larkin", "Art Appraiser", "Chloe/'s reliability is legendary, but loyalty only goes so far when her interests are at stake. Her gaze is as sharp as her appraisals."),
    ("Dannielle Horowitz", "Survivalist", "Tough, smart, and fiercely independent, Dannielle knows how to handle any situation. She/'s the one you want in a crisis—and the one you dread crossing."),
    ("Dennis Shapiro", "District Judge", "Every decision Dennis makes is a calculated move. His obsession with order and justice leaves little room for compromise or compassion."),
    ("Dimitri Volkov", "Marketing Director", "Dimitri/'s style is impeccable, his smile dazzling, and his critiques scathing. He/'s as obsessed with his image as he is with tearing down others."),
    ("Elaine Walker", "Auction Manager", "Always impeccably composed, Elaine seems immune to chaos. Her polite smile can disarm even the most belligerent guests."),
    ("Evan Levy", "Company Food Director", "Evan's hunger for success matches his appetite for gourmet food. Ambitious and adaptable, he/'s the kind of person who gets what he wants."),
    ("Fiona Gold", "VSC Intern", "Fiona/'s relentless drive has earned her a reputation as a workhorse, but ambition is a double-edged sword, and she/'s wielding it recklessly."),
    ("Gabrial Katz", "Paleontologist", "With his dreamy expression and wandering gaze, Gabrial seems to have his head in the clouds—until he turns those perceptive eyes on you."),
    ("Gina Zimmerman", "Shady Investor", "Greed looks good on Gina, who always finds a way to profit from any situation. Business is a game, and she plays to win—no matter the cost."),
    ("Greyson Blau", "Bar Manager", "With a scowl that could shatter glass and a dedication to his job that borders on obsession, Greyson's a man of principle—if you play by his rules."),
    ("Hugo Pierce", "Cocktail Expert", "Hugo/'s charm is intoxicating, but his loyalty runs only as deep as the bottom of his glass. Keep the drinks coming, and he/'ll stay friendly—stop, and who knows?"),
    ("Ivy Prescott", "Chemist", "Ivy/'s drive is as ruthless as her chemistry experiments. She/'s a master manipulator, always a step ahead and cooking up a plan—or something more dangerous."),
    ("Jack Adler", "Lawyer", "Jack's blunt attitude doesn/'t win him many friends, but he couldn/'t care less. He/'s out for number one, and he/'s not shy about it."),
    ("Jayden Mizrahi", "Data Scientist", "Jayden/'s sharp wit and infectious laugh make her a delight to be around. She/'s always ready with a clever quip or a brilliant solution."),
    ("Lisa Emerson", "Influencer", "Flashy and fabulous, Lisa lives for likes and follows. She/'s responsible when it counts, but drama is her bread and butter."),
    ("Londyn Schneider", "Innovation Director", "Londyn/'s silence speaks louder than words. Every move is calculated, every decision measured. He/'s a man of few words but many thoughts."),
    ("Marcus Mann", "Rancher", "On the surface, Marcus is the perfect rancher—straightforward, dependable, and courteous. But those who look a bit closer see hints of something darker simmering beneath his respectful exterior."),
    ("Margo Lane", "Wealthy Socialite", "Elegant and entitled, Margo/'s quick to throw shade and quicker to defend herself. Cross her, and you/'ll face a cutting remark you won/'t soon forget."),
    ("Mary Kaplan", "Art Director", "Mary/'s bold designs have captivated the art world, but behind her confident front, there's a lingering fear that she/'s one misstep away from losing it all."),
    ("Nina Drake", "Paparazzi", "Nina/'s bubbly laugh can be heard over any crowd, but she/'s rarely there just for fun. If there's gossip to be found, she/'s already taken the picture."),
    ("Olivia Winchester", "Auctioneer", "With her honeyed voice and silver tongue, Olivia could sell sand in the desert. Just don/'t underestimate the mind behind that charming smile."),
    ("Paige Mendelson", "Engineer", "Paige has the patience of a saint and the loyalty of a hound, but even she has limits. When pushed too far, this devoted engineer might just surprise you."),
    ("Rafael Dupont", "Art Forger", "Known for his charm and refined taste, Rafael is a master of illusion. His reputation as an art forger precedes him, yet he carries himself with the grace of an aristocrat, making you wonder what's real and what's not."),
    ("Roger Cohen", "Senior Journalist", "Roger doesn/'t just report the news—he makes it. His influence runs deep, and those who cross him often find their dirty laundry making headlines."),
    ("Roman Silverman", "VSC CFO", "Ever the life of the party, Roman thrives in the social spotlight, but jealousy often gets the better of him. His bright smile may hide more envy than you think."),
    ("Ruby Silverman", "VSC COO", "Ruby's eyes always glint with the anticipation of the future—a future she's already planning. Sharp-witted and shrewd, she/'s not one to be underestimated."),
    ("Ted Cruz", "Senator", "Ted/'s loud opinions and unpredictable behavior make him hard to handle. He's a patriot... if only you could figure out whose side he's on."),
    ("Trenton Silverman", "Old Biz Owner", "Wealth and power have molded Trenton into a man who takes what he wants and shows disdain for anyone he deems beneath him. His sneer speaks louder than any words."),
    ("Vivian Thorne", "Art Curator", "Vivian/'s gossip is as reliable as her taste in art, and she loves nothing more than a scandal—especially if she/'s the one to break it."),
    ("Xavier King", "Accountant", "Nervous and prone to over-explanation, Xavier's loose lips might just sink ships. He/'s the kind of guy who knows something you don/'t—until he spills."),
]



# characterBios = [
#     ("Aden Smith", "A spiritual security guard with a temper. His anger flares as quickly as his zen calm—a dangerous mix."),
#     ("Bennet Silverman", "The resourceful CEO of VSC, who\'s as dishonest as he is charming. He can talk his way out of anything... and often does."),
#     ("Brooklyn Weiss", "A banker who knows everyone's business and isn\'t shy about sharing. Loose lips are her forte—especially when there\'s a juicy rumor involved."),
#     ("Calvin Mendelson", "A calm, collected architect who hides a cruel streak behind his serene smile. He\'s all about precision—until it\'s time to get his hands dirty."),
#     ("Carlos Rosenberg", "A popstar who loves the spotlight almost as much as he loves himself. His arrogance is the only thing louder than his music."),
#     ("Charles Penrose", "A cunning Chief of Security with a clever streak. He\'s the guy who knows just enough to make you nervous."),
#     ("Chloe Larkin", "An art appraiser with a strong sense of independence. She\'s reliable, until the highest bidder comes along."),
#     ("Dannielle Horowitz", "A self-reliant survivalist who\'s as knowledgeable as she is blunt. She\'s prepared for any challenge... or confrontation."),
#     ("Dennis Shapiro", "A meticulous District Judge who judges everyone by his own refined standards. He\'s all polish, with a hint of ruthlessness."),
#     ("Dimitri Volkov", "A judgmental Marketing Director obsessed with his image. He\'ll critique your outfit while planning your downfall."),
#     ("Elaine Walker", "A poised Auction Manager who remains unruffled under pressure. Her calm demeanor is her greatest weapon."),
#     ("Evan Levy", "A food director who\'s adaptable, ambitious, and always hungry—for success and a good meal."),
#     ("Fiona Gold", "A prideful VSC intern with a workaholic streak. Her ambition might just be her downfall if she\'s not careful."),
#     ("Gabrial Katz", "A dreamy paleontologist who\'s just a bit too entitled for comfort. Always digging—whether it\'s fossils or for attention."),
#     ("Gina Zimmerman", "A bright investor with a greedy edge, who doesn\'t mind playing dirty to get ahead. It\'s all business—until it\'s personal."),
#     ("Greyson Blau", "A disciplined bar manager with a tough exterior. He\'s the kind of guy you want on your side... unless you\'re on his bad side."),
#     ("Hugo Pierce", "A cocktail expert with a self-serving streak. He\'s great company until the bottles run dry—and then things get dicey."),
#     ("Jack Adler", "A grumpy lawyer who\'s out for himself. His self-motivation is matched only by his disdain for everyone else\'s."),
#     ("Jayden Mizrahi", "A witty Data Scientist who loves nothing more than a challenge. Quick with a joke and quicker with a solution."),
#     ("Lisa Emerson", "A flashy influencer who\'s all about the next big thing. Responsible, but with a taste for drama—she\'s hard to ignore."),
#     ("Londyn Schneider", "A frugal Innovation Director who\'s stoic to the point of silence. He keeps his cards close, but there\'s no mistaking his sharp gaze."),
#     ("Marcus Mann", "A rancher who wears his respectability like a well-tailored suit, but there\'s something sinister lurking beneath his polite demeanor."),
#     ("Margo Lane", "A wealthy socialite whose sharp tongue is as formidable as her bank account. She\'s strong-willed, snippy, and always ready for a fight."),
#     ("Mary Kaplan", "An Art Director who takes risks with both her designs and her decisions. Beneath the bravado, though, lies a shaky sense of self."),
#     ("Nina Drake", "A bubbly paparazzi with a knack for finding scandal. Her curiosity has a way of uncovering secrets best left hidden."),
#     ("Olivia Winchester", "A charming auctioneer whose eloquence can soothe or slice. She has a way of getting what she wants—without anyone noticing."),
#     ("Paige Mendelson", "An engineer devoted to the ones she loves, tolerant to a fault. There\'s little that shakes Paige\'s loyalty, though everyone has their limits."),
#     ("Rafael Dupont", "An art forger with a talent for fakes and a knack for elegant deception. He\'s open, refined, and just dangerous enough to be fascinating."),
#     ("Roger Cohen", "A senior journalist who controls the headlines—and, some say, the people in them. His sinister charisma draws secrets out like moths to a flame."),
#     ("Roman Silverman", "A social butterfly and envy-ridden CFO, Roman thrives in a crowd—just don\'t turn your back on him."),
#     ("Ruby Silverman", "A visionary COO who\'s always three steps ahead. Her laser focus hides a ruthless ambition she keeps just out of sight."),
#     ("Ted Cruz", "A belligerent senator with a knack for making enemies. His erratic behavior makes him unpredictable at best."),
#     ("Trenton Silverman", "A business mogul with a nose for money and a scowl for everyone else. His arrogance is matched only by his disdain for 'lesser' folk."),
#     ("Vivan Thorne", "A gossipy Art Curator with a keen eye and a sharper tongue. She loves digging up dirt—and doesn\'t care who gets soiled."),
#     ("Xavier King", "A voluble accountant with a fragile ego and an anxious streak. He\'ll talk your ear off—and maybe let something slip."),
# ]



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