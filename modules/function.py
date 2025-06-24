FILEPATH = "data/app_data.txt"

# ! read the txt file custom function


def read_txt(filepath=FILEPATH):
    """ This Function helps us to read files from .txt file
    """
    with open(filepath, "r") as file_local:
        app_container_local = file_local.readlines()
    return app_container_local

# $ store in txt file custom function


def write_txt(app_container_loc_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(app_container_loc_arg)


if __name__ == "__main__":
    print("Hello from functions")
