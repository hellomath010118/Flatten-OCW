import os
from zipfile import ZipFile as open_zip

HASH_SEPERATOR = "##########################"


if __name__ == "__main__":
    print(HASH_SEPERATOR)
    print("UNZIPPING ALL FILES IN CURRENT DIRECTORY.")
    print(HASH_SEPERATOR)

    for filename in os.listdir():
        if filename.endswith(".zip"):
            with open_zip(filename, "r") as current_zip_file:
                current_zip_file.extractall()
