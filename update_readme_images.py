#!/usr/bin/env python3
"""
Script to automatically update README.md with images from organized folders.
This script scans the Clients subfolders and updates the README with the images.
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

def generate_image_html(image_path, alt_text, width=300):
    """Generate HTML img tag with caption for an image."""
    # URL encode the path but keep slashes
    encoded_path = '/'.join(quote(part, safe='') for part in image_path.split('/'))
    image_name = get_image_name(image_path)
    
    return f'''  <div style="text-align: center;">
    <img src="images/Clients/{encoded_path}" alt="{alt_text}" width="{width}" style="border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <p style="margin-top: 8px; font-size: 14px; color: #666; font-weight: 500;">{image_name}</p>
  </div>'''

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
    auth_images = get_images_from_folder(clients_base / 'Authorization')
    home_images = get_images_from_folder(clients_base / 'Home')
    category_images = get_images_from_folder(clients_base / 'CategoryButtons')
    
    # Generate HTML for each section
    auth_html = '\n'.join([generate_image_html(img, 'Client - Authorization') for img in auth_images])
    home_html = '\n'.join([generate_image_html(img, 'Client - Home Screen') for img in home_images])
    category_html = '\n'.join([generate_image_html(img, 'Client - Category Buttons') for img in category_images])
    
    # Update Authorization section - match everything between the div tags
    auth_pattern = r'(#### 🔐 Authorization\s*<div[^>]*>)(.*?)(</div>)'
    if auth_images:
        auth_replacement = f'\\1\n{auth_html}\n\\3'
    else:
        auth_replacement = f'\\1\n  <!-- No images yet - add images to images/Clients/Authorization/ -->\n\\3'
    content = re.sub(auth_pattern, auth_replacement, content, flags=re.DOTALL)
    
    # Update Home section
    home_pattern = r'(#### 🏠 Home Screen\s*<div[^>]*>)(.*?)(</div>)'
    if home_images:
        home_replacement = f'\\1\n{home_html}\n\\3'
    else:
        home_replacement = f'\\1\n  <!-- No images yet - add images to images/Clients/Home/ -->\n\\3'
    content = re.sub(home_pattern, home_replacement, content, flags=re.DOTALL)
    
    # Update Category Buttons section
    category_pattern = r'(#### 🎯 Category Buttons\s*<div[^>]*>)(.*?)(</div>)'
    if category_images:
        category_replacement = f'\\1\n{category_html}\n\\3'
    else:
        category_replacement = f'\\1\n  <!-- No images yet - add images to images/Clients/CategoryButtons/ -->\n\\3'
    content = re.sub(category_pattern, category_replacement, content, flags=re.DOTALL)
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Print summary
    print("=" * 60)
    print("README Updated Successfully!")
    print("=" * 60)
    print(f"Authorization images: {len(auth_images)}")
    print(f"Home Screen images: {len(home_images)}")
    print(f"Category Buttons images: {len(category_images)}")
    print(f"\nTotal images added: {len(auth_images) + len(home_images) + len(category_images)}")

if __name__ == '__main__':
    update_readme()
