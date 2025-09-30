import os

def create_gitkeep_in_all_subfolders(root_folders):
    for root in root_folders:
        for dirpath, dirnames, filenames in os.walk(root):
            gitkeep_path = os.path.join(dirpath, '.gitkeep')
            if not os.path.exists(gitkeep_path):
                open(gitkeep_path, 'a').close()

if __name__ == "__main__":
    label_folders = [
        "equipment_labels",
        "people_labels",
        "safety_gear_labels",
        "site_condition_labels",
        "vehicle_labels",
        "violation_labels"
    ]
    create_gitkeep_in_all_subfolders(label_folders)
    print("Added .gitkeep files in all subfolders.")
