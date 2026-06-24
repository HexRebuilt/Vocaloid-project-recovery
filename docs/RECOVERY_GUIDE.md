# Vocaloid 5 Project Recovery from Logic Pro

## Overview
This guide describes the process of recovering Vocaloid 5 project data when the plugin crashes upon loading in Logic Pro due to OS incompatibility (e.g., SIGILL crashes on macOS).

## Technical Root Cause
Vocaloid 5 stores its project state within the Logic Pro `.logicx` package. Specifically, the data is embedded as a **Base64-encoded ZIP archive** inside a Plist structure within the `ProjectData` binary file.

## Recovery Path
`Logic Project (.logicx)` $\rightarrow$ `ProjectData (Binary)` $\rightarrow$ `Base64 String` $\rightarrow$ `ZIP Archive` $\rightarrow$ `sequence.json` $\rightarrow$ `.vpr Project File`

## Step-by-Step Procedure
1. **Locate Project Data**: Navigate to `[ProjectName].logicx/Alternatives/000/ProjectData`.
2. **Extract Base64**: Search the binary for the `VOCALOID5` identifier and extract the content of the subsequent `<data>` block.
3. **Decode**: Convert the Base64 string into a binary file.
4. **Reconstruct Archive**:
   - Create a folder named `Project`.
   - Place the decoded `sequence.json` inside.
   - Zip the `Project` folder.
   - Rename the resulting archive to `.vpr`.

## Automation
A Python script `vocaloid_recover.py` is provided to automate this extraction.
