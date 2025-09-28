from config import (os, shutil, open_zip, TEMPNAME)

HASH_SEPERATOR = "##########################"


if __name__ == "__main__":
    print(HASH_SEPERATOR)
    print("UNZIPPING ALL FILES IN CURRENT DIRECTORY.")
    print(HASH_SEPERATOR)

    os.makedirs(TEMPNAME, exist_ok=True)

    for filename in os.listdir():
        if filename.endswith(".zip"):
            with open_zip(filename, "r") as current_zip_file:
                shutil.move(filename, os.path.join(TEMPNAME, os.path.basename(filename)))
                current_zip_file.extractall()
