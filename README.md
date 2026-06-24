# 🎤 Vocaloid Project Recovery
Rescue your Vocaloid 5 & 6 projects from Logic Pro binary traps.

## The Problem
On newer macOS versions, the Vocaloid plugin often triggers a `SIGILL` crash when attempting to load projects, making it impossible to recover project data through the standard interface.

## The Solution
This tool bypasses the plugin entirely by implementing a recovery pipeline:
`Logic Project` $\rightarrow$ `Base64` $\rightarrow$ `ZIP` $\rightarrow$ `.vpr`

## 🚀 Quick Start
### Prerequisites
- Python 3.x

### Usage
Run the script providing the path to your Logic project file or the `ProjectData` folder:
```bash
python vocaloid_recover.py "path/to/project.logicx"
# OR
python vocaloid_recover.py "path/to/ProjectData"
```

## 🛠️ Features
- **V5 & V6 Support**: Compatible with both Vocaloid 5 and 6 project versions.
- **Non-Destructive**: Does not modify the original Logic project.
- **Automatic Path Resolution**: Handles `.logicx` bundles automatically.

## ⚠️ Disclaimer
Always work on a **copy** of your project files to prevent accidental data loss.

## License
MIT License
