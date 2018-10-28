import pandas as pd
import re

def generateCleanFile(file_to_clean, output_file):
    df = pd.read_csv(file_to_clean, encoding="latin1")

    #Problem 2: Clean HTML and whitespace
    df['comment_msg'] = df['comment_msg'].apply(lambda x: str(x).lstrip())
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'\r*',"", str(x)))
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'<.*?>',"",str(x)))

    #Problem 1: Clean spam
    df['comment_msg'] = df['comment_msg'].apply(lambda x: x.lower())
    to_drop = ['app', 'free', '%20', 'check out my page', 'www.', 'http://']
    df = df[df.comment_msg.str.contains('|'.join(to_drop)) == False]

    #Problem 3: clean Null values
    df = df[df['comment_msg'] != ""]

    df.to_csv(output_file)

generateCleanFile("dd-comment-profile.csv", "dd-comment-profile-cleaned.csv")
