from django.shortcuts import render
import os

def index(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def works(request):
    return render(request, 'works.html')  


def projects(request, id, name):
    # Path to the CSV file in the static folder
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'Projects_Info.csv')
    
    project_details = None
    
    # Open and read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
        
        # Iterate through the rows to find the project with the matching ID
        for row in reader:
            if int(row['id']) == int(id):  # Ensure both are integers for comparison
                project_details = row
                break

    # Check if project details were found
    if not project_details:
        return render(request, '404.html', {"message": "Project not found"})  # Handle project not found

    # Pass the project details to the context
    context = {
        'project': project_details,
    }
    
    return render(request, 'projects.html', context)