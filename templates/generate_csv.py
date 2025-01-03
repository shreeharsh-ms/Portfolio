import csv

# Data to be written to the CSV file
data = {
    "Project Name": "The Damai",
    "Role / Services": "Design & Development",
    "Credits": [
        "Design: Christy Lammerink",
        "Design: Tom de Koning",
        "Photography: Niké Schuurmans"
    ],
    "Location & Year": "Bali, Indonesia © 2024",
    "Images": ["Image1", "Image2", "Image3", "Image4", "Image5"],
    "Location": "Bali, Indonesia",
    "Next Project Name": "Next Project Name",
    "Next Project Link": "Next Project Link"
}

# Writing to a CSV file
csv_file_path = "The_Damai_Project_Info.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow([
        "Project Name", 
        "Role / Services", 
        "Credits", 
        "Location & Year", 
        "Image1", "Image2", "Image3", "Image4", "Image5", 
        "Location", 
        "Next Project Name", 
        "Next Project Link"
    ])
    # Writing the data
    writer.writerow([
        data["Project Name"], 
        data["Role / Services"], 
        "; ".join(data["Credits"]),  # Joining credits with semicolons
        data["Location & Year"], 
        *data["Images"], 
        data["Location"], 
        data["Next Project Name"], 
        data["Next Project Link"]
    ])

csv_file_path
