import pandas as pd

# Path to your local Excel file
file_path = 'Murder-Mystery-party-Actions\Murder-Mystery-party-planning.ods'

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


