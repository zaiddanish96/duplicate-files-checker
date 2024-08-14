import os

def main():
    files = os.listdir("YOUR_DIRECTORY_HERE")
    files_by_name = {}
    total_files = 0
    total_duplicated_files = 0

    for filename in files:
        if filename not in files_by_name:
            files_by_name[filename] = []
        files_by_name[filename].append(filename)
        total_files += 1
        if len(files_by_name[filename]) > 1:
            total_duplicated_files += 1

    # Save the output to a readable text file in the specified directory
    with open("YOUR_DIRECTORY/FILENAME", "w") as f:
        for filenames in files_by_name.values():
            if len(filenames) > 1:
                f.write("Duplicated files:\n")
                for filename in filenames:
                    f.write("  " + filename + "\n")

    print("Total number of files:", total_files)
    print("Total number of duplicated files:", total_duplicated_files)

if __name__ == "__main__":
    main()
