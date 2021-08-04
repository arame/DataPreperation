import time, os, shutil, sys

class Helper:
    def printline(text):
        _date_time = time.strftime('%Y/%m/%d %H:%M:%S')
        print(f"{_date_time}   {text}")

    # This helper method is useful to get a list of the folders only and ignore any files
    def list_folders():
        return [x for x in os.listdir() if os.path.isdir(x)]

    def list_country_folders(folder):
        curr_dir = os.getcwd()
        os.chdir(folder)
        Helper.printline(f"Get folders from {os.getcwd()}")
        country_folders = Helper.list_folders()
        if "no_country" in country_folders:
            country_folders.remove("no_country")
        os.chdir(curr_dir)
        return country_folders

    def change_directory(dir):
        if os.path.exists(dir) == False:
            os.mkdir(dir)
        
        os.chdir(dir)
        return os.getcwd()

    def create_directory(dir):
        if os.path.exists(dir) == False:
            os.mkdir(dir)
            return
        
        # Delete all contents of a directory using shutil.rmtree() and  handle exceptions
        try:
            shutil.rmtree(dir)
        except:
            sys.exit('Error while deleting directory')
