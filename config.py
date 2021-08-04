
class Hyper:
    time = "2021_08_01 16_16_57"
    language = "en"
    HyrdatedTweetLangDir = f"../Summary_Details_files{time}/{language}"
    HyrdatedTweetFile = "tweets.csv"
    HyrdatedTweetLangFile = f"{language}_tweets_prev.csv"
    OutputTweetLangFile = f"{language}_tweets.csv"
    DestDir = f"../Data_{language}_{time}"
    Threshold = 400
    field_names = ['Country', 'English Tweet', 'sentiment']
 