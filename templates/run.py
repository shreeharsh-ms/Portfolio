import re

def convert_links_to_static(file_path):
    try:
        # Read the content of the file with the correct encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Ensure {% load static %} is at the start of the file
        if not re.search(r"{\%\s*load\s*static\s*%}", content):
            content = "{% load static %}\n" + content

        # Regex patterns to find href, src, and other attributes pointing to static assets
        patterns = [
            (r'(href|src)\s*=\s*[\"\'](css|js)/([a-zA-Z0-9_/.-]+)[\"\']', 
             lambda match: f"{match.group(1)}=\"{{% static '{match.group(2)}/{match.group(3)}' %}}\""),
            (r'(data-[a-zA-Z0-9_-]+)\s*=\s*[\"\']/([a-zA-Z0-9_/.-]+)[\"\']', 
             lambda match: f"{match.group(1)}=\"{{% static '{match.group(2)}' %}}\"")
        ]

        # Apply replacements for each pattern
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"File '{file_path}' has been updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except UnicodeDecodeError as e:
        print(f"Encoding error while reading the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'projects.html'  # Replace with your file path
convert_links_to_static(file_path)
