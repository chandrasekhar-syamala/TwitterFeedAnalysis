import matplotlib.pyplot as plt
import pandas as pd
import textwrap
# utilities
import re
import numpy as np
# plotting
import seaborn as sns
from wordcloud import WordCloud
# nltk
from nltk.stem import WordNetLemmatizer
# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

def trending_tweets():
    # Load data from CSV file
    df = pd.read_csv('Data/TrendingTweets.csv')

    # Extract tweet text and counts
    tweets = df.head(5)['tweet'].tolist()
    counts = df.head(5)['retweets_count'].tolist()
    # Set up color palette
    colors = ['#9b59b6', '#3498db', '#95a5a6', '#e74c3c', '#2ecc71']
    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = range(1, len(tweets)+1)

    ax.barh(y_pos, counts, align='center', alpha=0.5, height=0.8, color=colors)
    # Add tweet text to each bar
    for i, count in enumerate(counts):
        # Wrap text into multiple lines
        text = "\n".join(textwrap.wrap(tweets[i], width=50))
        # Adjust font size and vertical alignmentax.text(count+50, i, tweets[i], ha='left', va='bottom', fontsize=8)
        ax.text(0, i+1, text, ha='left', va='center', fontsize=10)

    # Set x-axis label
    ax.set_xlabel('Retweets Count')
    ax.set_ylabel('Rank')
    # Set title
    ax.set_title('Top Trending Tweets', fontsize=16, fontweight='bold')
# Set background color
    ax.set_facecolor('#f5f5f5')
    # Save chart to file
    fig.savefig('/static/trending_tweets.jpg', dpi=300)
    # Show chart
    #plt.show()


def liked_tweets():
    # Load data from CSV file
    df = pd.read_csv('/Data/MostLikedTweets.csv')

    # Extract tweet text and counts
    tweets = df.head(5)['tweet'].tolist()
    counts = df.head(5)['likes_count'].tolist()
    # Set up color palette
    colors = ['#9b59b6', '#3498db', '#95a5a6', '#e74c3c', '#2ecc71']
    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = range(1, len(tweets)+1)

    ax.barh(y_pos, counts, align='center',
            alpha=0.5, height=0.6, color=colors)
    # Add tweet text to each bar
    for i, count in enumerate(counts):
        # Wrap text into multiple lines
        text = "\n".join(textwrap.wrap(tweets[i], width=50))
        # Adjust font size and vertical alignmentax.text(count+50, i, tweets[i], ha='left', va='bottom', fontsize=8)
        ax.text(0, i+1, text, ha='left', va='center', fontsize=10)

    # Set x-axis label
    ax.set_xlabel('Likes Count')
    ax.set_ylabel('Rank')
    # Set title
    ax.set_title('Most Liked Tweets', fontsize=16, fontweight='bold')
    # Set background color
    ax.set_facecolor('#f5f5f5')
    # Save chart to file
    fig.savefig('/static/most_liked_tweets.png', dpi=300)
    # Show chart
    #plt.show()


def top_products():
    # Load data from CSV file
    df = pd.read_csv('/Data/topProds.csv')

    # Extract the product names and their frequency counts
    products = df['Product'].tolist()[:10]
    counts = df['Frequency'].tolist()[:10]

    # Create a pie chart using Matplotlib
    fig, ax = plt.subplots(figsize=(15, 12))
    ax.pie(counts, labels=products, autopct='%1.1f%%', startangle=90)

    # Add title and legend to the chart
    ax.set_title('Apple Product Frequency')
    ax.legend(products, bbox_to_anchor=(1.05, 1), loc='upper left')

    # Save chart to file
    fig.savefig('/static/top_products.png', dpi=300)

    # Display the chart
    #plt.show()

def mention_counts():
    # Set the display options to show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Importing the dataset
    df = pd.read_csv('Data/mentionCounts.csv')
    #df.head()
    N = 10 # top N hashtags
    top_hashtags = df.sort_values(by='Count', ascending=False).head(N)

    plt.figure(figsize=(10, 10))
    plt.barh(top_hashtags['Mentions'], top_hashtags['Count'])
    plt.title(f'Top {N} Mentions',fontsize=20)
    plt.xlabel('Count', fontsize=20)
    plt.ylabel('Mentions', fontsize=20)
    plt.xticks(fontsize=15) # set the font size of the x-axis values
    plt.yticks(fontsize=15) # set the font size of the x-axis values
    #plt.show()
    plt.savefig('static/BarChart_Top10Mentions.png', bbox_inches='tight')
    # Combine all the hashtags into a single string
    mentions_string = ' '.join(df['Mentions'])

    # Generate a word cloud of the all hashtags
    wordcloud = WordCloud(max_words = 1000,width=800, height=800, background_color='black', min_font_size=15,stopwords=None).generate(mentions_string)


    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    # Call plot function on the ax object
    ax.plot()

    # Save the figure
    plt.savefig('static/Mentions_wordcloud.png', bbox_inches='tight')

    # Get the top 10 hashtags by count
    top_n = 10
    top_mentions = df.sort_values(by=['Count'], ascending=False).head(top_n)

    # Create a dataframe of the top N hashtags and their counts
    top_mentions_df = pd.DataFrame({'Mentions': top_mentions['Mentions'], 'Count': top_mentions['Count']})

    # Plot a pie chart of the top N hashtags
    plt.figure(figsize=(9, 9))
    plt.pie(top_mentions_df['Count'], labels=top_mentions_df['Mentions'], autopct='%1.1f%%',startangle=90, textprops={'fontsize': 11}, labeldistance=1.05)
    plt.axis('equal')
    plt.title('Top {} Mentions'.format(top_n),fontsize=20)
    #plt.show()

    plt.savefig('static/Mentions_piechart.png')

def keyword_counts():
    # Set the display options to show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Importing the dataset
    df = pd.read_csv('Data/keywordCounts.csv')
    df = df.iloc[:, :2]
    #df.head()
    df = df.dropna()
    # Download the English stopwords corpus if not already downloaded
    nltk.download('stopwords')

    # Create a set of English stopwords
    en_stopwords = set(nltk.corpus.stopwords.words('english'))

    # Filter only English hashtags from the Hashtag column in the dataframe df
    df_en = df[df['Keywords'].apply(lambda x: all(word.lower() not in en_stopwords for word in x.split()))]
    # Combine all the hashtags into a single string
    keywords_string = ' '.join(df_en['Keywords'])

    # Generate a word cloud of the all hashtags
    wordcloud = WordCloud(max_words = 1000,width=800, height=800, background_color='black', min_font_size=15,stopwords=None).generate(keywords_string)


    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    # Call plot function on the ax object
    ax.plot()

    # Save the figure
    plt.savefig('static/Keywords_wordcloud.png', bbox_inches='tight')

def hashtag_counts():
    # Set the display options to show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Importing the dataset
    df = pd.read_csv('Data/hashtagCounts.csv')
    #df.head()
    N = 10 # top N hashtags
    top_hashtags = df.sort_values(by='Hashtag_Count', ascending=False).head(N)

    plt.figure(figsize=(10, 10))
    plt.barh(top_hashtags['Hashtag'], top_hashtags['Hashtag_Count'])
    plt.title(f'Top {N} Hashtags',fontsize=20)
    plt.xlabel('Count', fontsize=20)
    plt.ylabel('Hashtag', fontsize=20)
    plt.xticks(fontsize=15) # set the font size of the x-axis values
    plt.yticks(fontsize=15) # set the font size of the x-axis values
    #plt.show()
    plt.savefig('/static/BarChart_Top10Hashtags.png', bbox_inches='tight')
    # Combine all the hashtags into a single string
    hashtags_string = ' '.join(df['Hashtag'])

    # Generate a word cloud of the all hashtags
    wordcloud = WordCloud(max_words = 1000,width=800, height=800, background_color='black', min_font_size=10,stopwords=None).generate(hashtags_string)


    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()
    # Call plot function on the ax object
    ax.plot()

    # Save the figure
    plt.savefig('/static/Hashtag_wordcloud.png', bbox_inches='tight')

    # Get the top 10 hashtags by count
    top_n = 10
    top_hashtags = df.sort_values(by=['Hashtag_Count'], ascending=False).head(top_n)

    # Create a dataframe of the top N hashtags and their counts
    top_hashtags_df = pd.DataFrame({'Hashtag': top_hashtags['Hashtag'], 'Count': top_hashtags['Hashtag_Count']})

    # Plot a pie chart of the top N hashtags
    plt.figure(figsize=(9, 9))
    plt.pie(top_hashtags_df['Count'], labels=top_hashtags_df['Hashtag'], autopct='%1.1f%%',startangle=90, textprops={'fontsize': 11}, labeldistance=1.05)
    plt.axis('equal')
    plt.title('Top {} Hashtags'.format(top_n),fontsize=20)
    #plt.show()

    plt.savefig('/static/Hashtag_piechart.png')

trending_tweets()
liked_tweets()
top_products()
#mention_counts()
#keyword_counts()
#hashtag_counts()