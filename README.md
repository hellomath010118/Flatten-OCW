# Flatten-OCW
Have you been traumatized by the useless folders you find on unzipping the MIT OCW courses? Do you hate those random long starts? Here comes a life-saver!

## Using the project
Download the five python files. Let us assume that you download XYZ.zip from MIT OCW. To process this file, you are advised to make a subfolder, e.g., "OCW_temp" containing the following:
- The project (currently five python files)
- XYZ.zip (preferably a copy)
- NOTE: This is a DESTRUCTIVE operation and the XYZ.zip file will be removed from your device.

Open a command line and execute `py main.py`. All scripts will execute on their own. The output will consist of a directory named static_resources with the following structure:
- static resources
-  - PSets
   -  - Names containing "ps" or "hw"
   - Lectures
   -  - Names containing "lec"
   - Transcripts
   -  - Garbarge-like names, that will be processed using fitz from pymupdf.
   - Slides
   -  - Names containing "slide"
   - Other PDF files
Most of the names that appear in the end are (hopefully) more human readable and logical.
