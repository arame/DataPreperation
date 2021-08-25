
class Hyper:
    #time = "2021_08_01 16_16_57"
    #time = "2021_08_08 22_58_57"
    #time = "2021_08_11 12_02_37"
    #time = "2021_08_12 05_59_32"
    #time = "2021_08_14 10_46_28"
    time = "2021_08_18 10_54_32"
    language = "en"
    HyrdatedTweetLangDir = f"../Summary_Details_files{time}/{language}"
    HyrdatedTweetFile = "tweets.csv"
    HyrdatedTweetLangFile = f"{language}_tweets_prev.csv"
    OutputTweetLangFile = f"{language}_tweets.csv"
    FacemaskTweetLangFile = f"{language}_facemask_tweets.csv"
    LockdownTweetLangFile = f"{language}_lockdown_tweets.csv"
    DestDir = f"../Data_{language}_{time}"
    #Threshold = 400
    SelectedCountries = [ "Australia", "Canada", "China", "France", "Germany", "Ghana", "India",
                         "Ireland", "Italy", "Kenya", "Malaysia", "Netherlands",
                         "New Zealand", "Nigeria", "Pakistan", "Philippines", 
                         "South Africa", "United Kingdom", "United States"]
    input_field_names = ['Country', 'Full Text', 'clean_text', 'sentiment', 'is_facemask', 'is_lockdown']
    output_field_names = ['Country', 'Full Text', 'clean_text', 'sentiment']
 