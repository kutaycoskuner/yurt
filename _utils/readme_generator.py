# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
#                notes
# ----------------------------------------------------------------------------------------
'''
Kutay Coskuner, 2025
This code is licensed under the MIT License. You can use, modify, and distribute it freely.
However, it is provided "as is," without any warranties or guarantees of any kind.
For details, visit: https://opensource.org/licenses/MIT

- description
    This script loops through folders (excluding those starting with `_`) and their
    subfolders, searches for `.json` files whose names start with `metadata`, reads their
    content, and renders it into a `README.md` file in the same directory.

- use case
    This script can be used to generate `README.md` files based on `metadata.json` files
    in a directory structure.

- install
    - pip install python-dotenv (if needed for environment variables)

- sources

- todo
'''

# ----------------------------------------------------------------------------------------
#                libraries
# ----------------------------------------------------------------------------------------
import os
import json

# ----------------------------------------------------------------------------------------
#                variables
# ----------------------------------------------------------------------------------------
ROOT_DIR = os.getcwd()


# ----------------------------------------------------------------------------------------
#                functions
# ----------------------------------------------------------------------------------------
def find_metadata_json_files(root_dir):
    """
    Recursively searches for `.json` files starting with `metadata` in folders that do not start with `_`.

    :param root_dir: The root directory to start searching from.
    :return: A list of paths to the found `.json` files.
    """
    metadata_json_files = []

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories starting with `_`
        dirnames[:] = [d for d in dirnames if not d.startswith('_')]

        # Loop through files in the current directory
        for filename in filenames:
            # Check if the file is a `.json` file and starts with `metadata`
            if filename.endswith('.json') and filename.startswith('metadata'):
                # Construct the full file path and add it to the list
                file_path = os.path.join(dirpath, filename)
                metadata_json_files.append(file_path)

    return metadata_json_files


def render_readme(metadata):
    """
    Renders the content of a `metadata.json` file into a human-readable `README.md` format.

    :param metadata: A dictionary containing the metadata.
    :return: A string containing the rendered `README.md` content.
    """
    readme_content = f"# {metadata.get('name', 'Untitled')}\n\n"
    readme_content += f"**Description:** {metadata.get('description', 'No description provided.')}\n\n"
    readme_content += f"**Version:** {metadata.get('version', 'N/A')}\n\n"
    readme_content += f"**Type:** {metadata.get('type', 'N/A')}\n\n"
    readme_content += f"**Formats:** {', '.join(metadata.get('formats', ['N/A']))}\n\n"
    readme_content += f"**Access Date:** {metadata.get('accessDate', 'N/A')}\n\n"

    # Add screenshot if available
    if metadata.get('screenshot'):
        readme_content += f"![Screenshot]({metadata['screenshot']})\n\n"

    # Add paths if available
    if metadata.get('paths'):
        readme_content += "**Paths:**\n"
        for path in metadata['paths']:
            readme_content += f"- {path}\n"
        readme_content += "\n"

    # Add tags if available
    if metadata.get('tags'):
        readme_content += "**Tags:**\n"
        for tag in metadata['tags']:
            readme_content += f"- {tag}\n"
        readme_content += "\n"

    # Add legal information if available
    if metadata.get('legal'):
        legal = metadata['legal'][0]  # Assuming only one legal block
        readme_content += "**Legal Information:**\n"
        readme_content += f"- **Authors:** {', '.join(legal.get('authors', ['N/A']))}\n"
        readme_content += f"- **Owner:** {legal.get('owner', 'N/A')}\n"
        readme_content += f"- **Source:** {legal.get('source', 'N/A')}\n"
        readme_content += f"- **Publish Date:** {legal.get('publishDate', 'N/A')}\n"
        readme_content += f"- **License:** {legal.get('license', 'N/A')}\n"
        readme_content += f"- **License URLs:** {', '.join(legal.get('licenceURLs', ['N/A']))}\n"
        readme_content += f"- **What:** {legal.get('what', 'N/A')}\n\n"

    # Add modifications if available
    if metadata.get('modifications'):
        readme_content += "**Modifications:**\n"
        for mod in metadata['modifications']:
            readme_content += f"- **Author:** {mod.get('author', 'N/A')}\n"
            readme_content += f"  **Description:** {mod.get('description', 'N/A')}\n"
        readme_content += "\n"

    return readme_content


def create_readme(file_path, content):
    """
    Creates or updates a `README.md` file with the given content.

    :param file_path: The path where the `README.md` file should be created.
    :param content: The content to write to the `README.md` file.
    """
    readme_path = os.path.join(os.path.dirname(file_path), "README.md")
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(content)
    print(f"Created/Updated README.md at: {readme_path}")


# ----------------------------------------------------------------------------------------
#                main
# ----------------------------------------------------------------------------------------
def main():
    metadata_files = find_metadata_json_files(ROOT_DIR)

    # Process each metadata file
    for file_path in metadata_files:
        try:
            # Read the metadata file
            with open(file_path, "r", encoding="utf-8") as file:
                metadata = json.load(file)

            # Render the content into a README.md format
            readme_content = render_readme(metadata)

            # Create or update the README.md file
            create_readme(file_path, readme_content)

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file {file_path}. Skipping.")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}. Skipping.")


# ----------------------------------------------------------------------------------------
#                start
# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
