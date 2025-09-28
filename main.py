import subprocess

if __name__ == "__main__":
    scripts_to_run = ["1_unzip.py", "2_folder_system_and_deleter.py", "3_classifier_underscore_and_type.py", "4_transcript_name_fixer.py"]
    for script in scripts_to_run:
        subprocess.run(["python", script])

