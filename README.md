# `Household Item Finder`

This is a tool for people who lose things in their home and end up buying a copy of the item they "lost," even though the item was actually sitting somewhere in a drawer. This application will help people keep and track inventory of everything they have in their home and where it is so as to not buy copies and promote money spending efficiency. 

# `FOR REGULAR USAGE:`

## Simple Instruction
**Windows:**
- Download the installer [here]()
- Run the installer
- It will give you an "Unknown Publisher" warning, simply click "more info" > "run anyway"
  
**MAC:**
- Download the zip folder [here]()
- Double-click to uncompress the folder, and go into the uncompressed folder
- Bypass the "Unidentified Developer" Warning
- Right-click or control-click the "editor_gui" unix executable file and hit open, then confirm open.
- It should install Homebrew if you don't have it on your system.

## Examples/Tutorial
- [Tutorial](example)

# `FOR DEVELOPER USAGE:`

Clone the repository with --recurse-submodules so PySimpleGUI's older version will be included:

`git clone --recurse-submodules https://github.com/Noah-Grimaldi/Household-Item-Finder.git`

Run editor_gui.py, which programmatically references the other files.

## Dependencies
- Windows Instruction: [Download Python 3.10](https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe).
- MAC Instruction: Install [Homebrew](https://brew.sh/), then if you already have python 3.10 downloaded, uninstall it.
  
  First do `brew install python-tk@3.10`
  
  Then do `brew install python@3.10`

**After** you've activated the venv on your specified platform, run the command: `pip install -r requirements.txt`

## Platform Support 
Windows/MacOS

