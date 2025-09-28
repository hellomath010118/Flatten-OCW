from config import (os, shutil, pymupdf, TEMPNAME)

def weak_find_topic(text: str):
    """
    Extracts first line of text and removes invalid symbols
    that cannot be present in filename.
    """
    newline_index = text.find('\n')
    if newline_index != -1:
        text = text[:newline_index]
   
    # Remove invalid characters for filenames
    invalid_chars = r'<>:"/\|?*'
    for ch in invalid_chars:
        text = text.replace(ch, '')
    
    return text

def find_topic(text: str) -> str:
    """
    Extract the topic from the given text.
    Returns a sanitized string suitable as a filename.
    """
    newline_index = text.find('\n')
    if newline_index != -1:
        text = text[:newline_index]
    # Remove non-alphanumeric characters at the start of the text
    
    flag = -1
    i = 0
    for char in text:
        if not (char.isalnum() or char.isspace() or char == "-" or char == "," or char == "."):
            flag = i
        i += 1
    text = text[flag+1:].strip()

    if not text:
        raise ValueError("Extracted topic is empty")
    # Remove invalid characters for filenames
    invalid_chars = r'<>:"/\|?*'
    for ch in invalid_chars:
        text = text.replace(ch, '')
    
    result = ""
    l = len(text)
    for i in range(l-1):
        result += text[i]
        if text[i].isdigit() and not text[i+1].isdigit() and text[i+1] != ".":
            result += "."
    result += text[l-1]
#    if text[l-1].isdigit():
#        result += "."

    return result



def try_renaming_in(directory, bad_filename, first_page_of_file):
    
    file_path = os.path.join(directory, bad_filename)

    new_filename = find_topic(first_page_of_file) + ".pdf"
    new_path = os.path.join(directory, new_filename)
    
    if os.path.exists(new_path):
        print(f"File already exists: {new_filename}, resorting to PLAN B.")

        new_filename = weak_find_topic(first_page_of_file) + ".pdf"
        new_path = os.path.join(directory, new_filename)

        if os.path.exists(new_path):
            print(f"Embarrassing COMPLETE FAILURE for {bad_filename}.")
        else:
            os.rename(file_path, new_path)
            print(f"Renamed '{bad_filename}' to '{new_filename}'") 
    else:
        os.rename(file_path, new_path)
        print(f"Renamed '{bad_filename}' to '{new_filename}'")

def process_pdfs(directory: str):
    """
    Processes PDF files in the given directory.
    Renames them based on their content.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):  # Process only PDFs
            try:
                file_path = os.path.join(directory, filename)
                print(f"Processing: {filename}")
                current_pdf = pymupdf.open(file_path)
                
                try:
                    first_page = current_pdf[0].get_text('text', flags=2)
                finally:
                    current_pdf.close()  # Ensure the file is closed

                try_renaming_in(directory, filename, first_page)

            except ValueError as e:
                print(f"Skipping {filename}: {e}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

HASH_SEPERATOR = "##########################"

# Call the function for the current directory
if __name__ == "__main__":

    os.chdir("static_resources")
    os.chdir("Transcripts")

    print(HASH_SEPERATOR)
    print("TRYING TO FIX NAMES IN DIRECTORY.")
    print(HASH_SEPERATOR)
    
    process_pdfs(os.getcwd())
    
    os.chdir("../..")
    final_folder_name = ""
    for file in os.listdir(os.path.join(os.getcwd(), TEMPNAME[:-1])):
        if file.endswith(".zip"):
            final_folder_name = os.path.splitext(file)[0]
            shutil.move(
                os.path.join(TEMPNAME, file),
                os.path.join(os.getcwd(), file)
            )

    if not os.listdir(TEMPNAME):
        shutil.rmtree(TEMPNAME)
    else:
        print(f"[!] Unexpected files found in temporary directory: {os.listdir(TEMPNAME)}")

    os.rename("static_resources", final_folder_name)
