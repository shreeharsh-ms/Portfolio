from django.shortcuts import render
import os
import csv
from django.conf import settings
from django.http import Http404


def index(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def works(request):
    return render(request, 'works.html')  


import csv
import os
from django.conf import settings
from django.shortcuts import render
from django.http import Http404

def projects(request, id, name):
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'Projects_Info.csv')

    # Check if the file exists
    if not os.path.exists(csv_file_path):
        raise Http404("CSV file not found.")

    # Read the CSV file and find the project
    project_data = {}
    next_project_data = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row.get('id', -1)) == id:
                project_data = row
                next_project_id = row.get('Next Project ID', None)
                break

    # Raise 404 if no matching project found
    if not project_data:
        raise Http404("Project not found.")

    # If there's a next project, find its details
    if next_project_id:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row.get('id', -1)) == int(next_project_id):
                    next_project_data = row
                    break

    # Prepare project context data
    project_context = {
        'id': project_data.get('id', 'N/A'),
        'name': project_data.get('Project Name', 'Untitled Project'),
        'role_services': project_data.get('Role / Services', 'N/A'),
        'credits': project_data.get('Credits', '').split('; '),
        'location_and_year': project_data.get('Location & Year', 'N/A'),
        'images': [
            project_data.get('Image1', ''),
            project_data.get('Image2', ''),
            project_data.get('Image3', ''),
            project_data.get('Image4', ''),
            project_data.get('Image5', ''),
        ],
        'location': project_data.get('Location', 'N/A'),
        'year': project_data.get('Location & Year', 'N/A').split(', ')[-1],
        'next_project_name': next_project_data.get('Project Name', 'None'),
        'next_project_link': f"/projects/{next_project_data.get('id', '')}/{next_project_data.get('Project Name', '').replace(' ', '-').replace('/', '-')}" if next_project_data else '#',
        
        # New fields for detailed project info
        'project_overview': project_data.get('Project Overview', 'No overview available.'),
        'technologies_features': project_data.get('Technologies & Features', 'No technologies available.'),
        'impact_future_directions': project_data.get('Impact & Future Directions', 'No impact details available.'),
        
        # New field for next project image
        'next_project_image1': next_project_data.get('Next Project Image1', '')
    }

    # Pass the isolated data to the template
    return render(request, 'projects.html', {'project': project_context})
