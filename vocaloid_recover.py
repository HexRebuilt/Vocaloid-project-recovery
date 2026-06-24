#!/usr/bin/env python3
import sys
import base64
import os

def recover_vocaloid_project(input_path):
    # Path Handling
    project_data_path = input_path
    if os.path.isdir(input_path) and input_path.endswith('.logicx'):
        project_data_path = os.path.join(input_path, 'Alternatives', '000', 'ProjectData')
        print(f"Detected .logicx directory. Searching for ProjectData at: {project_data_path}")
    
    if not os.path.exists(project_data_path):
        print(f"Error: ProjectData file not found at {project_data_path}")
        return

    try:
        with open(project_data_path, 'rb') as f:
            content = f.read()

        # Vocaloid 5 & 6 Support
        markers = {
            b'VOCALOID6': 'v6',
            b'VOCALOID5': 'v5'
        }
        
        version_found = None
        marker_pos = -1
        
        for marker, version in markers.items():
            pos = content.find(marker)
            if pos != -1:
                version_found = version
                marker_pos = pos
                break
        
        if not version_found:
            print(f"Error: Could not find VOCALOID5 or VOCALOID6 marker in {project_data_path}")
            return

        print(f"Detected Vocaloid {version_found.upper()[1:]} project... Extracting...")

        # Robust Extraction
        start_tag = b'<data>'
        end_tag = b'</data>'
        
        start_pos = content.find(start_tag, marker_pos)
        if start_pos == -1:
            print(f"Error: Could not find <data> tag after marker in {project_data_path}")
            return
        
        start_pos += len(start_tag)
        end_pos = content.find(end_tag, start_pos)
        if end_pos == -1:
            print(f"Error: Could not find </data> tag after <data> tag in {project_data_path}")
            return

        # Extract the Base64 string
        base64_data = content[start_pos:end_pos]

        # Decode Base64
        try:
            decoded_data = base64.b64decode(base64_data)
        except Exception as e:
            print(f"Error: Failed to decode Base64 data: {e}")
            return

        # Save as .vpr file with version-specific name
        output_filename = f"recovered_{version_found}.vpr"
        output_path = os.path.join(os.path.dirname(project_data_path) if os.path.dirname(project_data_path) else ".", output_filename)
        
        with open(output_path, 'wb') as f:
            f.write(decoded_data)
        
        print(f"Successfully recovered project to: {output_path}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Vocaloid Project Recovery Tool")
        print("Usage: ./vocaloid_recover.py <path>")
        print("\nArguments:")
        print("  <path>    Path to a ProjectData file or a .logicx project directory")
        sys.exit(1)
    
    recover_vocaloid_project(sys.argv[1])
