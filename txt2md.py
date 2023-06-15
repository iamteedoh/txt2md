#!/usr/bin/python3

import os
import html2text

def rename_files():
    # get all files in the current directory
    files = os.listdir('.')
    
    # filter only .txt files
    txt_files = [f for f in files if f.endswith('.txt')]

    for file_name in txt_files:
        # remove 'Notes' from the beginning of the file name
        if file_name.startswith('Notes'):
            new_name = file_name.replace('Notes', '', 1)

        # change .txt to .md
        base_name, ext = os.path.splitext(new_name)
        new_name = f'{base_name}.md'
        
        # rename the file
        os.rename(file_name, new_name)
        print(f'Renamed {file_name} to {new_name}')

# Run the function
rename_files()

def html_to_md(input_html_file, output_md_file):
    # Create an html2text.HTML2Text object and override some properties
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False

    # Open the HTML file and read its content
    #with open(input_html_file, 'r', encoding='utf-8') as html_file:
    with open(input_html_file, 'r', encoding='latin-1') as html_file:
        html_content = html_file.read()

    # Convert the HTML to Markdown
    md_content = h.handle(html_content)

    # Write the Markdown to the output file
    #with open(output_md_file, 'w', encoding='utf-8') as md_file:
    with open(output_md_file, 'w', encoding='latin-1') as md_file:
        md_file.write(md_content)

# Specify the directory containing your .md files
directory = ('.')

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # If the file is a .md file
    if filename.endswith('.md'):
        # Create the path to the .md file
        md_file = os.path.join(directory, filename)
        # Convert the .md file (which is formatted as HTML) to proper Markdown
        html_to_md(md_file, md_file)
