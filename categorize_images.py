#!/usr/bin/env python3
"""
Script to help categorize images by analyzing their content.
This script will attempt to extract text from images to identify which user role they belong to.
"""

import os
from pathlib import Path

# Keywords that might appear in each user role's screenshots
ROLE_KEYWORDS = {
    'Client': ['browse', 'material', 'favorite', 'chat', 'amy', 'contract', 'installation', 'client', 'home'],
    'Sales Representative': ['dashboard', 'client', 'sales', 'analytics', 'inbox', 'performance', 'revenue'],
    'Installer': ['job', 'installer', 'location', 'map', 'photo', 'album', 'availability', 'status'],
    'Scheduler': ['calendar', 'event', 'schedule', 'appointment', 'template', 'google calendar'],
    'Administrator': ['admin', 'user management', 'analytics', 'amy management', 'content', 'advanced']
}

def get_image_files():
    """Get all image files from the images directory."""
    images_dir = Path('images')
    image_extensions = ['.png', '.jpg', '.jpeg']
    images = []
    
    for ext in image_extensions:
        images.extend(images_dir.glob(f'*{ext}'))
        images.extend(images_dir.glob(f'*{ext.upper()}'))
    
    return sorted(images)

def categorize_by_filename(filename):
    """Try to categorize based on filename patterns."""
    filename_lower = filename.lower()
    
    # Check for patterns in filenames
    if 'client' in filename_lower or 'p01' in filename_lower:
        return 'Client'
    elif 'sales' in filename_lower or 'p06' in filename_lower:
        return 'Sales Representative'
    elif 'installer' in filename_lower or 'p07' in filename_lower:
        return 'Installer'
    elif 'scheduler' in filename_lower or 'p08' in filename_lower:
        return 'Scheduler'
    elif 'admin' in filename_lower or 'p09' in filename_lower:
        return 'Administrator'
    
    return None

def main():
    """Main function to categorize images."""
    images = get_image_files()
    
    print("=" * 60)
    print("Image Categorization Helper")
    print("=" * 60)
    print(f"\nFound {len(images)} images to categorize.\n")
    
    # Group by potential categories based on filename
    categorized = {
        'Client': [],
        'Sales Representative': [],
        'Installer': [],
        'Scheduler': [],
        'Administrator': [],
        'Uncategorized': []
    }
    
    for img in images:
        filename = img.name
        category = categorize_by_filename(filename)
        
        if category:
            categorized[category].append(filename)
        else:
            categorized['Uncategorized'].append(filename)
    
    # Print results
    for category, files in categorized.items():
        if files:
            print(f"\n{category}:")
            print("-" * 40)
            for f in files:
                print(f"  - {f}")
    
    print("\n" + "=" * 60)
    print("\nNote: This is a preliminary categorization based on filename patterns.")
    print("Please review the images visually to confirm and refine these categories.")
    print("\nYou can open 'images/viewer.html' in your browser to view all images.")
    print("=" * 60)

if __name__ == '__main__':
    main()
