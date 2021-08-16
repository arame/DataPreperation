
class Hyper:
    #time = "2021_08_01 16_16_57"
    time = "2021_08_08 22_58_57"
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
    input_field_names = ['Country', 'English Tweet', 'sentiment', 'is_facemask', 'is_lockdown']
    output_field_names = ['Country', 'English Tweet', 'sentiment']
 