#!/usr/bin/env python3
"""
Script to automatically update README.md with images from organized folders.
This script scans the Clients subfolders and updates the README with the images using table format.
"""

import re
from pathlib import Path
from urllib.parse import quote

def get_images_from_folder(folder_path, include_subfolders=True):
    """Get all image files from a folder and optionally subfolders, sorted by name."""
    if not folder_path.exists():
        return []
    
    images = []
    
    # Get images from the main folder
    for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']:
        images.extend(folder_path.glob(f'*{ext}'))
    
    # Get images from subfolders if requested
    if include_subfolders:
        for subfolder in folder_path.iterdir():
            if subfolder.is_dir():
                for ext in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']:
                    images.extend(subfolder.glob(f'*{ext}'))
    
    # Return relative paths from the Clients folder, removing duplicates
    result = []
    seen = set()
    clients_base = folder_path.parent
    for img in sorted(images):
        rel_path = str(img.relative_to(clients_base)).replace('\\', '/')
        if rel_path not in seen:
            seen.add(rel_path)
            result.append(rel_path)
    
    return result

def get_image_name(image_path):
    """Extract a clean name from the image path."""
    # Get the filename without extension
    filename = Path(image_path).stem
    # Replace hyphens and underscores with spaces, and clean up
    name = filename.replace('-', ' ').replace('_', ' ')
    # Capitalize first letter of each word
    return ' '.join(word.capitalize() for word in name.split())

def generate_image_td(image_path, width=200):
    """Generate HTML table cell (td) with image and caption."""
    # URL encode the path but keep slashes
    encoded_path = '/'.join(quote(part, safe='') for part in image_path.split('/'))
    image_name = get_image_name(image_path)
    
    return f'''      <td style="text-align: center; padding: 10px;">
        <img src="images/Clients/{encoded_path}" alt="{image_name}" width="{width}" style="border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <p style="margin-top: 8px; font-size: 14px; color: #666; font-weight: 500;">{image_name}</p>
      </td>'''

def create_table_rows(images):
    """Create table rows with 4 images per row."""
    if not images:
        return ''
    
    rows = []
    for i in range(0, len(images), 4):
        row_images = images[i:i+4]
        tds = '\n'.join([generate_image_td(img) for img in row_images])
        rows.append(f'    <tr>\n{tds}\n    </tr>')
    return '\n'.join(rows)

def update_readme():
    """Update README.md with images from organized folders."""
    readme_path = Path('README.md')
    clients_base = Path('images/Clients')
    
    if not readme_path.exists():
        print("Error: README.md not found!")
        return
    
    # Read README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get images from each folder (including subfolders)
    welcome_images = get_images_from_folder(clients_base / 'Welcome')
    auth_images = get_images_from_folder(clients_base / 'Authorization')
    home_images = get_images_from_folder(clients_base / 'Home')
    category_images = get_images_from_folder(clients_base / 'CategoryButtons')
    
    # Generate table rows for each section (4 images per row)
    welcome_html = create_table_rows(welcome_images)
    auth_html = create_table_rows(auth_images)
    home_html = create_table_rows(home_images)
    category_html = create_table_rows(category_images)
    
    # Update Welcome section - add before Authorization if it exists
    welcome_pattern = r'(## Welcome Screens\s*<div[^>]*>).*?(</div>\s*\n(?:##|###|####|#|$))'
    if welcome_images:
        welcome_replacement = f'''## Welcome Screens

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
{welcome_html}
  </table>
</div>
\\2'''
        if re.search(welcome_pattern, content, flags=re.DOTALL):
            content = re.sub(welcome_pattern, welcome_replacement, content, flags=re.DOTALL)
        else:
            # Insert Welcome section before Authorization
            auth_match = re.search(r'(### 📸 App Screenshots\s*\n)', content)
            if auth_match:
                insert_pos = auth_match.end()
                welcome_section = f'''### 📸 App Screenshots

## Welcome Screens

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
{welcome_html}
  </table>
</div>

'''
                content = content[:insert_pos] + welcome_section + content[insert_pos:]
    
    # Update Authorization section - use table format
    auth_pattern = r'(## Authorization Screens\s*<div[^>]*>).*?(</div>\s*\n(?:##|###|####|#|$))'
    if auth_images:
        auth_replacement = f'''## Authorization Screens

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
{auth_html}
  </table>
</div>
\\2'''
    else:
        auth_replacement = f'''## Authorization Screens

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
    <!-- No images yet - add images to images/Clients/Authorization/ -->
  </table>
</div>
\\2'''
    content = re.sub(auth_pattern, auth_replacement, content, flags=re.DOTALL)
    
    # Update Home section - use table format
    home_pattern = r'(## Home Screen\s*<div[^>]*>).*?(</div>\s*\n(?:##|###|####|#|$))'
    if home_images:
        home_replacement = f'''## Home Screen

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table style="white-space: nowrap;">
{home_html}
  </table>
</div>
\\2'''
    else:
        home_replacement = f'''## Home Screen

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
    <!-- No images yet - add images to images/Clients/Home/ -->
  </table>
</div>
\\2'''
    content = re.sub(home_pattern, home_replacement, content, flags=re.DOTALL)
    
    # Update Category Buttons section - use table format
    category_pattern = r'(## Category Buttons & Features\s*<div[^>]*>).*?(</div>\s*\n(?:##|###|####|#|$))'
    if category_images:
        category_replacement = f'''## Category Buttons & Features

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table style="white-space: nowrap;">
{category_html}
  </table>
</div>
\\2'''
    else:
        category_replacement = f'''## Category Buttons & Features

<div style="overflow-x: auto; border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <table>
    <!-- No images yet - add images to images/Clients/CategoryButtons/ -->
  </table>
</div>
\\2'''
    content = re.sub(category_pattern, category_replacement, content, flags=re.DOTALL)
    
    # Remove old duplicate headers (#### format)
    content = re.sub(r'#### (🔐|🏠|🎯)[^\n]*\n## ', r'## ', content)
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Print summary
    print("=" * 60)
    print("README Updated Successfully!")
    print("=" * 60)
    print(f"Welcome images: {len(welcome_images)}")
    print(f"Authorization images: {len(auth_images)}")
    print(f"Home Screen images: {len(home_images)}")
    print(f"Category Buttons images: {len(category_images)}")
    print(f"\nTotal images added: {len(welcome_images) + len(auth_images) + len(home_images) + len(category_images)}")

if __name__ == '__main__':
    update_readme()
