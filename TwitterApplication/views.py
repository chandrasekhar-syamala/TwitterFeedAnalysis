"""
Routes and views for the flask application.
"""

import csv
from datetime import datetime
from flask import render_template
from TwitterApplication import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Team',
        year=datetime.now().year,
        message='Project Team - Principles of Big Data Management'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/influencers')
def influencers():
    """Renders the contact page."""
    with open(r"C:\Users\Chandu\source\repos\TwitterApplication\TwitterApplication\Data\mentionCounts.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        mentionCounts = []
        count = 0
        for row in csv_reader:
            if count == 10:
                break
            mentionCounts.append(row)
            count += 1
    return render_template('influencers.html', mentionCounts=mentionCounts,title='Top Handles')


@app.route('/topics')
def topics():
    """Renders the about page."""
    with open(r"C:\Users\Chandu\source\repos\TwitterApplication\TwitterApplication\Data\topProds.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        topProds = []
        for row in csv_reader:
            topProds.append(row)
    return render_template('topics.html', topProds=topProds,title='Trending Topics')


@app.route('/tweets')
def tweets():
    """Renders the contact page."""
    with open(r"C:\Users\Chandu\source\repos\TwitterApplication\TwitterApplication\Data\TrendingTweets.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        tweets = []
        count = 0
        for row in csv_reader:
            if count == 10:
                break
            tweets.append(row)
            count += 1
    with open(r"C:\Users\Chandu\source\repos\TwitterApplication\TwitterApplication\Data\MostLikedTweets.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        likedtweets = []
        count = 0
        for row in csv_reader:
            if count == 10:
                break
            likedtweets.append(row)
            count += 1    
    return render_template('tweets.html', tweets=tweets[:10], likedtweets=likedtweets[:10],title='Top Tweets')
    

