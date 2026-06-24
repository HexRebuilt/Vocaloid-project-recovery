# Vocaloid-Logic-Recover

A utility to rescue Vocaloid 5 and 6 project data from Logic Pro `.logicx` binary files when the plugin crashes due to OS incompatibility.

## Features
- Automatic `.logicx` path resolution.
- Support for both Vocaloid 5 and 6.
- Direct extraction of embedded Base64 ZIP archives.

## Installation
Requires Python 3.

## Usage
```bash
python vocaloid_recover.py "path/to/project.logicx"
python vocaloid_recover.py "path/to/ProjectData"
```

## How it works
The tool parses the Logic Pro project binary to locate specific markers (`VOCALOID5` or `VOCALOID6`). It then extracts the associated Base64 encoded string, decodes it into a ZIP archive, and extracts the original `.vpr` project files.

## License
MIT License
# Vocaloid-project-recovery
