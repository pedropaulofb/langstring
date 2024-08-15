import os


def create_files_from_list(file_with_names, destination_folder):
    with open(file_with_names, "r") as file:
        for line in file:
            filename = line.strip()
            full_path = os.path.join(destination_folder, filename)
            with open(full_path, "w") as new_file:
                print(f"Created file: {full_path}")


# Example usage
source_file = "list_of_filenames.txt"  # Path to your file with names
destination_folder = "./tests/tests_utils/TODO"  # Path to the destination folder

create_files_from_list(source_file, destination_folder)
