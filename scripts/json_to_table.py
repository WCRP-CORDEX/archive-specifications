#!/usr/bin/env python3
"""
Convert global_attributes.json to a markdown table.
"""

import json
from pathlib import Path


def json_to_markdown_table(json_file, output_file):
    """
    Convert the global attributes JSON to a markdown table.
    
    Args:
        json_file: Path to the input JSON file
        output_file: Path to the output markdown file
    """
    # Read the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Start building the markdown table
    lines = []
    
    # Table header
    lines.append("| CORDEX-CMIP6 global attribute | description | examples | corresponding attribute in CORDEX-CMIP5 | form | when required? |")
    lines.append("| ----- | ----- | ----- | :---: | :---: | :---: |")
    
    # Table rows - iterate through the dictionary in order
    for attr_key, attr_data in data.items():
        name = attr_data['name']
        description = attr_data['description']
        examples = attr_data['examples']
        cordex_cmip5 = attr_data['cordex_cmip5_attribute']
        form = attr_data['form']
        when_required = attr_data['when_required']
        
        # Build the row
        row = f"| {name} | {description} | {examples} | {cordex_cmip5} | {form} | {when_required} |"
        lines.append(row)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        f.write('\n')
    
    print(f"Created markdown table: {output_file}")


if __name__ == '__main__':
    json_file = 'global_attributes.json'
    output_file = 'docs/global_attributes.md'
    json_to_markdown_table(json_file, output_file)
