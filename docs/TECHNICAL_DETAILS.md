# Technical Details

## Logic Pro Project Structure
Logic Pro `.logicx` files are actually bundles (directories). The core project data is typically stored in a binary Plist within the `ProjectData` folder.

## Extraction Process
The recovery tool scans the binary data for the following magic markers:
- `VOCALOID5`
- `VOCALOID6`

When a marker is found, the tool identifies the start and end of the Base64 encoded payload. 

### Pipeline:
1. **Binary Scan**: Search for version-specific markers.
2. **Base64 Decode**: Convert the extracted string back into binary data.
3. **ZIP Extraction**: The decoded binary is a ZIP archive containing the project data.
4. **File Recovery**: Extract the `.vpr` (Vocaloid Project) files from the ZIP.
