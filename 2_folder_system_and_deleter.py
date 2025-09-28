from config import (os, shutil, TEMPNAME)

HASH_SEPERATOR = "##########################"

if __name__ == "__main__":
    print(HASH_SEPERATOR)
    print("DELETING NON-PDF CONTAINING DIRECTORIES (MIT OCW -- HARD CODED)")
    print(HASH_SEPERATOR)

    # STAGE 1: REMOVE non-.py files
    # STAGE 2: REMOVE non-static resources folders
    
    for filename in os.listdir():
        path = os.path.join(os.getcwd(), filename)
        if os.path.isfile(path) and not filename.endswith(".py") and not filename.endswith(".py.swp"):
            os.remove(path)
        if os.path.isdir(path) and filename != "static_resources" and filename != ".git" and filename != TEMPNAME[:-1]:
            shutil.rmtree(path)

    # STAGE 3: REMOVE useless files

    print(HASH_SEPERATOR)
    print("DELETING UNNECESSARY FILES INSIDE STATIC_RESOURCES.")
    print(HASH_SEPERATOR)

    os.chdir("static_resources")

    for filename in os.listdir():
        if not filename.endswith(".pdf"):
            os.remove(filename)



