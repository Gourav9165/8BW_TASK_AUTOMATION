import os

def rename(path, prefix):
    try:
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(os.path.join(path, file)):
                new_name = f"{prefix}_{file}"
                os.rename(os.path.join(path, file), os.path.join(path, new_name))
                print(f"\nRenamed: {file} to {new_name} \n")
        print("Renaming of Files Completed Successfully!\n")
    except Exception as e:
        print(f"An error occurred: {e}")


path = input("Enter the Destination Path(Without quotes): ")
prefix = input("Enter prefix: ")

rename(path, prefix)