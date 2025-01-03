import csv

# List of all projects
projects = [
    {
        "Project Name": "VivaVista with AI Proctor",
        "Role / Services": "Natural Language Processing (NLP) and Computer Vision",
        "Credits": [
            "Design: Christy Lammerink",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "GPN Nagpur, 2024",
        "Images": ["Image1", "Image2", "Image3", "Image4", "Image5"],
        "Location": "GPN Nagpur",
        "Next Project Name": "Personalized Grocery Recommendation System",
        "Next Project Link": "/projects/2"
    },
    {
        "Project Name": "Personalized Grocery Recommendation System",
        "Role / Services": "Machine Learning-based",
        "Credits": [
            "Design: Tom de Koning",
            "Development: Nagpur Team"
        ],
        "Location & Year": "Nagpur, 2024",
        "Images": ["Image6", "Image7", "Image8", "Image9", "Image10"],
        "Location": "Nagpur",
        "Next Project Name": "DataVIZ",
        "Next Project Link": "/projects/3"
    },
    {
        "Project Name": "DataVIZ",
        "Role / Services": "Data Science & Business Intelligence",
        "Credits": [
            "Photography: Niké Schuurmans",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "Nagpur, 2024",
        "Images": ["Image11", "Image12", "Image13", "Image14", "Image15"],
        "Location": "Nagpur",
        "Next Project Name": "Hashware",
        "Next Project Link": "/projects/4"
    },
    {
        "Project Name": "Hashware",
        "Role / Services": "Cybersecurity & Malware Analysis",
        "Credits": [
            "Design: Christy Lammerink",
            "Development: Nagpur Team"
        ],
        "Location & Year": "Nagpur, 2023",
        "Images": ["Image16", "Image17", "Image18", "Image19", "Image20"],
        "Location": "Nagpur",
        "Next Project Name": "Coding Zen Website",
        "Next Project Link": "/projects/5"
    },
    {
        "Project Name": "Coding Zen Website (Node.js)",
        "Role / Services": "Web Development",
        "Credits": [
            "Design: Tom de Koning",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "GPN Nagpur, 2023",
        "Images": ["Image21", "Image22", "Image23", "Image24", "Image25"],
        "Location": "GPN Nagpur",
        "Next Project Name": "Encryptia Website",
        "Next Project Link": "/projects/6"
    },
    {
        "Project Name": "Encryptia Website (Django)",
        "Role / Services": "Web Development",
        "Credits": [
            "Photography: Niké Schuurmans",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "GPN Nagpur, 2023",
        "Images": ["Image26", "Image27", "Image28", "Image29", "Image30"],
        "Location": "GPN Nagpur",
        "Next Project Name": "Retrieving IP from Payload",
        "Next Project Link": "/projects/7"
    },
    {
        "Project Name": "Retrieving IP from Payload",
        "Role / Services": "Security/Networking",
        "Credits": [
            "Design: Christy Lammerink",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "GPN Nagpur, 2023",
        "Images": ["Image31", "Image32", "Image33", "Image34", "Image35"],
        "Location": "GPN Nagpur",
        "Next Project Name": "Django Reverse Shell - Command Execution",
        "Next Project Link": "/projects/8"
    },
    {
        "Project Name": "Django Reverse Shell - Command Execution",
        "Role / Services": "Security/Networking",
        "Credits": [
            "Design: Tom de Koning",
            "Development: Nagpur Team"
        ],
        "Location & Year": "GPN Nagpur, 2023",
        "Images": ["Image36", "Image37", "Image38", "Image39", "Image40"],
        "Location": "GPN Nagpur",
        "Next Project Name": "Data Analyzing Project",
        "Next Project Link": "/projects/9"
    },
    {
        "Project Name": "Data Analyzing Project",
        "Role / Services": "Data Science/Analytics",
        "Credits": [
            "Photography: Niké Schuurmans",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "Nagpur, 2023",
        "Images": ["Image41", "Image42", "Image43", "Image44", "Image45"],
        "Location": "Nagpur",
        "Next Project Name": "Cisco Packet Tracer Modules",
        "Next Project Link": "/projects/10"
    },
    {
        "Project Name": "Cisco Packet Tracer Modules",
        "Role / Services": "Networking/Simulation",
        "Credits": [
            "Design: Christy Lammerink",
            "Development: GPN Nagpur"
        ],
        "Location & Year": "Nagpur, 2021",
        "Images": ["Image46", "Image47", "Image48", "Image49", "Image50"],
        "Location": "Nagpur",
        "Next Project Name": "None",
        "Next Project Link": "None"
    }
]

# CSV file path
csv_file_path = "Projects_Info.csv"

# Writing to the CSV file
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
    
    # Writing the data for each project
    for project in projects:
        writer.writerow([
            project["Project Name"],
            project["Role / Services"],
            "; ".join(project["Credits"]),  # Joining credits with semicolons
            project["Location & Year"],
            *project["Images"],
            project["Location"],
            project["Next Project Name"],
            project["Next Project Link"]
        ])

print(f"CSV file successfully created at: {csv_file_path}")
