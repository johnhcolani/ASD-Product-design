#!/usr/bin/env python3
"""
Script to organize client images into subfolders by feature.
Edit the mappings below to match your images, then run the script.
"""

import os
import shutil
from pathlib import Path

# Define which images belong to which category
# Edit this dictionary with your image mappings
IMAGE_MAPPINGS = {
    'Authorization': [
        # Add image filenames here, e.g.:
        # 'IMG_5049.png',
        # 'IMG_5050.png',
    ],
    'Home': [
        # Add image filenames here
    ],
    'CategoryButtons': [
        # Add image filenames here
    ],
}

def organize_images():
    """Move images to their respective subfolders."""
    base_dir = Path('images/Clients')
    
    if not base_dir.exists():
        print(f"Error: {base_dir} does not exist!")
        return
    
    # Create subfolders if they don't exist
    for folder in IMAGE_MAPPINGS.keys():
        (base_dir / folder).mkdir(exist_ok=True)
    
    moved_count = 0
    not_found = []
    
    # Move images to their folders
    for folder, images in IMAGE_MAPPINGS.items():
        for image_name in images:
            source = base_dir / image_name
            dest = base_dir / folder / image_name
            
            if source.exists():
                shutil.move(str(source), str(dest))
                print(f"✓ Moved {image_name} → {folder}/")
                moved_count += 1
            else:
                not_found.append(image_name)
    
    print(f"\n✓ Organized {moved_count} images")
    
    if not_found:
        print(f"\n⚠ Could not find these images: {', '.join(not_found)}")
        print("Please check the filenames in IMAGE_MAPPINGS")
    
    # List remaining unorganized images
    remaining = [f.name for f in base_dir.iterdir() 
                 if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg']]
    
    if remaining:
        print(f"\n📋 Remaining unorganized images: {len(remaining)}")
        print("   " + ", ".join(remaining[:10]))
        if len(remaining) > 10:
            print(f"   ... and {len(remaining) - 10} more")

if __name__ == '__main__':
    print("=" * 60)
    print("Client Images Organizer")
    print("=" * 60)
    print("\n⚠ Please edit IMAGE_MAPPINGS in this script first!")
    print("   Add image filenames to the appropriate categories.\n")
    
    response = input("Have you edited IMAGE_MAPPINGS? (yes/no): ")
    if response.lower() in ['yes', 'y']:
        organize_images()
    else:
        print("\nPlease edit the IMAGE_MAPPINGS dictionary in this script first.")
        print("Then run the script again.")
