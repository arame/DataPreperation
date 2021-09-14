import pandas as pd
import os, shutil
from config import Hyper
from helper import Helper

'''
    This program is the fifth in a suite of programs to be executed in this order
    1/ App - gets tweets from Twitter API
    2/ Location - gets the country of the tweet from user location
    3/ Annotate - calculates the sentiment of each tweet
    4/ Wordcload - shows the words most in use in tweets from different countries
    5/ Datapreparation - gets the data in the correct form
    6/ Transformer - builds a transformer model from the tweets
'''
# See https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file
def main():
    move_files_to_destination_folder()
    combine_files()
    select_columns_for_new_file()

def move_files_to_destination_folder():
    #
    #   Create a new data directory where only the countries with enough tweets are selected
    #
    Helper.printline("   Started: Move files to data directory")
    Helper.create_directory(Hyper.DestDir)
    list_dirs = Helper.list_country_folders(Hyper.HyrdatedTweetLangDir)
    i = 0
    no_countries = len(list_dirs)
    Helper.printline(f"Iterate through {no_countries} countries")
    for country in list_dirs:
        i += 1
        country_dir = os.path.join(Hyper.HyrdatedTweetLangDir, country)
        country_file = os.path.join(country_dir, Hyper.HyrdatedTweetFile)
        csv_input = pd.read_csv(country_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        Helper.printline(f"Country {i}/{no_countries}. {country} has {len(csv_input)} entries")
        if country in Hyper.SelectedCountries:
            data_dir = os.path.join(Hyper.DestDir, country)
            Helper.printline(f"Country selected {country} ({len(csv_input)}), copy {country_dir} to {data_dir}")
            shutil.copytree(country_dir, data_dir)
    
    Helper.printline("    Ended: Move files to data directory")

def combine_files():
    #
    # Join all the tweet files for each country into one file for the langauage
    #
    Helper.printline("     ** Started: Combine files for each country per selected language")
    list_dirs = Helper.list_country_folders(Hyper.DestDir)
    big_df = pd.concat( [pd.read_csv(os.path.join(Hyper.DestDir, _dir, Hyper.HyrdatedTweetFile)) for _dir in list_dirs])
    #
    #   Ensure tweets are in lower case
    #
    #big_df["clean_tweet"] = big_df["clean_tweet"].str.lower()
    file = os.path.join(Hyper.DestDir, Hyper.HyrdatedTweetLangFile) 
    big_df.to_csv(file, index=False)
    Helper.printline("     ** Ended: Combine files for each country per selected language")

def select_columns_for_new_file():
    #
    #   Create a new file with only the required columns for sentiment analysis
    #
    Helper.printline("     ** Started: Select required columns for the new file")
    file_in = os.path.join(Hyper.DestDir, Hyper.HyrdatedTweetLangFile)
    file_out = os.path.join(Hyper.DestDir, Hyper.OutputTweetLangFile)
    edit_df = pd.read_csv(file_in, usecols=Hyper.input_field_names)
    edit_df[Hyper.output_field_names].to_csv(file_out, index=False)
    generate_theme_file(edit_df, Hyper.FacemaskTweetLangFile, 'is_facemask==True')
    generate_theme_file(edit_df, Hyper.LockdownTweetLangFile, 'is_lockdown==True')
    if Hyper.is_vaccine_included:
        generate_theme_file(edit_df, Hyper.VaccineTweetLangFile, 'is_vaccine==True')
    
    Helper.printline("     ** Ended: Select required columns for the new file")

def generate_theme_file(edit_df, _file, _query):
    file_out = os.path.join(Hyper.DestDir, _file)
    _df = edit_df.query(_query)
    _df[Hyper.output_field_names].to_csv(file_out, index=False)
    
if __name__ == "__main__":
    main()