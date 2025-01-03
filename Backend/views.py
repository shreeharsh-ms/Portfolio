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


def projects(request, id, name):
    csv_file_path = 'static/project_info.csv'

    project_data = None
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('id') == str(id):
                    row['Credits'] = row['Credits'].split('; ')  # Convert Credits to a list
                    # Normalize keys for easier template access
                    row['Location'] = row.pop('Location', '')
                    row['Year'] = row['Location & Year'].split(', ')[1] if 'Location & Year' in row else ''
                    project_data = row
                    break
    except FileNotFoundError:
        raise Http404("CSV file not found.")
    except Exception as e:
        raise Http404(f"An error occurred: {e}")

    if not project_data:
        raise Http404("Project not found.")

    context = {
        'project': project_data,
    }
    return render(request, 'projects.html', context)
