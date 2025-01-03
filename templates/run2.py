import os
import re

def replace_links_in_file(file_path):
    """Replaces all occurrences of links starting with 'https://dennissnellenberg.com' in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace URLs starting with 'https://dennissnellenberg.com'
    updated_content = re.sub(r'https://dennissnellenberg\.com[^\s"\'>]*', '#', content)

    # Write back the modified content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Updated links in: {file_path}")

def update_links_in_directory(directory):
    """Updates links in all HTML files in the given directory."""
    for file in os.listdir(directory):
        if file.endswith('.html'):
            file_path = os.path.join(directory, file)
            replace_links_in_file(file_path)

if __name__ == "__main__":
    # Specify the directory to scan (change this to your target directory)
    target_directory = "D:\\context\\portfolio temp\\Portfolio\\templates"
    print(f"Processing HTML files in directory: {target_directory}")
    update_links_in_directory(target_directory)
    print("Finished updating links.")
