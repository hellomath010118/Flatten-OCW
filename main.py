import subprocess

def run_scripts_in_order(script_list):
    """Runs the set of python scripts below in order"""

    for script in script_list:
        subprocess.run(["python", script])

if __name__ == "__main__":
    scripts_to_run = ["1_unzip.py", "2_folder_system_and_deleter.py", "3_classifier_underscore_and_type.py", "4_transcript_name_fixer.py"]
    run_scripts_in_order(scripts_to_run)

