![Unreal Engine](https://img.shields.io/badge/unrealengine-%23313131.svg?style=for-the-badge&logo=unrealengine&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# Unreal Engine Asset Renamer
# UE-asset-renamer

This script allows you to rename assets in Unreal Engine based on a search pattern and a replacement string. The script works on all types of assets that can be renamed in the Unreal Editor.

# Requirements

* Unreal Engine 4.26 or later installed
* Python 3.7 or later installed
* PyQt5 module installed

# Installation

Clone this repository or download the ZIP archive and extract its contents.

# Usage

1. Open Unreal Engine
2. Select the assets you want to rename in the Content Browser.
3. Go to **File > Execute Python Script**
4. Locate your Python Script and run it.
5. in the script's UI window, enter the search pattern and the replacement string in the appropriate fields. You can choose to make the search case-sensitive or not by checking the "Case Sensitive" checkbox.
6. Click **"OK"** button to rename the assets.

# Notes

* This script only works on assets that can be renamed in the Unreal Editor. It does not work on other types of files.
* The script will skip assets that do not match the search pattern.
* The script does not prompt you for confirmation before renaming assets. Be sure to double-check your search pattern and replacement string before running the script.
* The script's UI is created using the PyQt5 module. If you are not familiar with PyQt5, you can refer to the PyQt5 documentation for more information.
* In the repository files you can find the files you can find a simple version of this code withouth the PyQt5 UI ```asset renamer.py``` and a UI version with the UE **Utility Widget Tool** ```asset-renamer-widget.py```.
