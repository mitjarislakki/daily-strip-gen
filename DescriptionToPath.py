import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('computerVision.csv')

def get_image_path(description):
   
    # Search for the row that matches the given description
    row = df[df['texts'] == description]
    
    # Check if a matching row was found
    if not row.empty:
        # Return the image path from the matching row
        return row['img'].values[0]
    else:
        # If no match found, return None
        return None

# Example usage:
description = "Beautiful landscape"
image_path = get_image_path(description)

if image_path:
    print(f"The image path for '{description}' is: {image_path}")
else:
    print(f"No image path found for '{description}'")
