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

def generate_image_html(image_path, alt_text, width=200):
    """Generate HTML img tag with caption for an image."""
    # URL encode the path but keep slashes
    encoded_path = '/'.join(quote(part, safe='') for part in image_path.split('/'))
    image_name = get_image_name(image_path)
    
    return f'''  <div style="text-align: center; flex: 0 0 auto; width: {width}px;">
    <img src="images/Clients/{encoded_path}" alt="{alt_text}" width="{width}" style="border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); display: block; margin: 0 auto; width: {width}px; height: auto;">
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
    
    # First, clean up any duplicate content that might exist
    # Remove any orphaned divs after the main grid container closes
    content = re.sub(r'(</div>\s*\n)(\s*<div style="text-align: center;">.*?</div>\s*\n)+', r'\1', content, flags=re.DOTALL)
    
    # Update Authorization section - add border and title with flexbox for better GitHub compatibility
    auth_pattern = r'(#### 🔐 Authorization\s*<div[^>]*>).*?(</div>\s*\n(?:####|###|##|#|$))'
    if auth_images:
        auth_replacement = f'''#### 🔐 Authorization
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Authorization Screens</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
{auth_html}
  </div>
</div>
\\2'''
    else:
        auth_replacement = f'''#### 🔐 Authorization
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Authorization Screens</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
    <!-- No images yet - add images to images/Clients/Authorization/ -->
  </div>
</div>
\\2'''
    content = re.sub(auth_pattern, auth_replacement, content, flags=re.DOTALL)
    
    # Update Home section - add border and title with flexbox
    home_pattern = r'(#### 🏠 Home Screen\s*<div[^>]*>).*?(</div>\s*\n(?:####|###|##|#|$))'
    if home_images:
        home_replacement = f'''#### 🏠 Home Screen
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Home Screen</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
{home_html}
  </div>
</div>
\\2'''
    else:
        home_replacement = f'''#### 🏠 Home Screen
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Home Screen</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
    <!-- No images yet - add images to images/Clients/Home/ -->
  </div>
</div>
\\2'''
    content = re.sub(home_pattern, home_replacement, content, flags=re.DOTALL)
    
    # Update Category Buttons section - add border and title with flexbox
    category_pattern = r'(#### 🎯 Category Buttons\s*<div[^>]*>).*?(</div>\s*\n(?:####|###|##|#|$))'
    if category_images:
        category_replacement = f'''#### 🎯 Category Buttons
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Category Buttons & Features</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
{category_html}
  </div>
</div>
\\2'''
    else:
        category_replacement = f'''#### 🎯 Category Buttons
<div style="border: 3px solid #333; border-radius: 8px; padding: 20px; margin: 25px 0; background-color: #f9f9f9;">
  <h4 style="margin-top: 0; margin-bottom: 20px; color: #333; font-size: 20px; font-weight: 700; border-bottom: 2px solid #ddd; padding-bottom: 10px;">Category Buttons & Features</h4>
  <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start; align-items: flex-start;">
    <!-- No images yet - add images to images/Clients/CategoryButtons/ -->
  </div>
</div>
\\2'''
    content = re.sub(category_pattern, category_replacement, content, flags=re.DOTALL)
    
    # Replace all grid/flex layouts with 4-column grid layout (only for image grid divs)
    content = re.sub(
        r'(#### (🔐|🏠|🎯)[^\n]*\n<div style=")display: (flex|grid)[^"]*(">)',
        r'\1display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin: 20px 0;\4',
        content
    )
    
    # Also add responsive breakpoints for smaller screens (optional - can be added via CSS media queries in a style tag if needed)
    
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
