from config import (os, re)
"""
TO DO: Use logging functions instead of printing the message in stdout
"""

def make_if_absent(string: str):
    if not os.path.exists(string):
        os.mkdir(string)
    else:
        print("ALREADY EXISTS, SKIPPING.")

def safe_rename_file(old_filename: str, new_filename: str):
    try:
        os.rename(os.path.join(".", old_filename), os.path.join(new_filename))
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {old_filename}")
    except Exception as e:
        print(f"ERROR RENAMING FILE: {e}")

def relocate_file_into(filename: str, folder: str):
    try:
        os.rename(os.path.join(".", filename), os.path.join(".", folder, filename))
    except FileNotFoundError:
        print(f"FILE NOT FOUND: {filename}")
    except Exception as e:
        print(f"ERROR RENAMING FILE: {e}")


HASH_SEPERATOR = "##########################"

if __name__ == "__main__":

    os.chdir("static_resources")
    
    print(HASH_SEPERATOR)
    print("REMOVING RANDOM HEX NUMERALS.")
    print(HASH_SEPERATOR)

    for filename in os.listdir():
        if "_" in filename:
            underscore_position = filename.index("_")
            new_filename = filename[underscore_position+1:]
            safe_rename_file(filename, new_filename)


    make_if_absent("PSets")
    make_if_absent("Lectures")
    make_if_absent("Transcripts")
    make_if_absent("Slides")

    print(HASH_SEPERATOR)
    print("CLASSIFYING FILES.")
    print(HASH_SEPERATOR)

    lecture_regex = re.compile(r'l[0-9]*\.pdf')  

    for filename in os.listdir():
        if os.path.isfile(filename):
            name = filename.lower()
            if "mit" not in name:
                relocate_file_into(filename, "Transcripts")
            elif "ps" in name or "hw" in name:
                relocate_file_into(filename, "PSets")
            elif "lec" in name or re.match(lecture_regex, name):
                relocate_file_into(filename, "Lectures")
            elif "slide" in name:
                relocate_file_into(filename, "Slides")
       
