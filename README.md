# Twitter Feed Analysis using Spark with Hadoop
An academic project as a part of course, "Principles of Big Data Management", to develop a system to store, process, analyse, and visualize Twitter’s data using Apache Spark

Phase -1 : Hadoop & Spark's Map Reduce Word Count of URLs and HashTags from the tweets collected through Twitter API using TWARC.


## Documentation
#### [Setting UP Hadoop](https://www.quickprogrammingtips.com/big-data/how-to-install-hadoop-on-mac-os-x-el-capitan.html)
#### [Setting UP Spark]( http://genomegeek.blogspot.com/2014/11/how-to-install-apache-spark-on-mac-os-x.html)
#### [Configuring TWARC](https://scholarslab.github.io/learn-twarc/)

#### Tweet Collection & Extraction of Urls, HashTags
    1. Python Script is written to do the tweet collection through API and then extraction of urls & hashtags.
    2. It seeks users choice of keyword(s) to search for the corresponding tweets and storing it into a json file.
    3. Twarc command 'search' is used to collect the respective tweets with a timeout of 15 Minutes(i.e., the collection
        of tweets is suspended if the search command is not done by 15 minutes).
    4. The tweets collected will be stored in a json file 'tweets_keywords'.
    5. Urls and HashTags are extracted from 'tweets_keywords' into a text file 'twitter_out.txt'.
        i.  While reading Tweets, empty tweets are ignored and the tweets with at least one url or one hashtag is extracted/ 
        ii. There are several kinds of urls exist in the url entity of tweet. The main url is being extracted into text file 
            ignoring remaining kind of urls.
        iii. Similarly, all the hashtags of tweets are extracted into the output text file. 



## Deployment(Step by Step Execution)

    1. Extracting urls & hashtags from the collected tweets for given user keyword(s)

```bash
    python twitter_extraction.py
```
    2. Moving extracted text file 'twitter_out' from local folder to hdfs folder.
```bash
    $HADOOP_HOME/bin/hdfs dfs -put '/local/path/twitter_out.txt' /your_hdfs_folder 
```
    3. Running Hadoop MapReduce WordCount on 'twitter_out.txt' present in 'your_hdfs_folder' and place the generated output under 'output'
```bash
    $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /your_hdfs_folder/twitter_out.txt /your_hdfs_folder/output
```
    4. The generated output can be found in the hdfs folder named 'output'.
    5. Running Spark MapReduce WordCount on twitter_extraction and extracting the wordcount output into Spark_Output file which will be stored in local folder.
```bash
    $SPARK_HOME/bin/spark-submit run-example JavaWordCount /your_hdfs_folder/twitter_out.txt | grep -v info >> Spark_Output.txt
```

## Authors

- [@Chandrasekhar-Syamala](https://github.com/chandrasekhar-syamala)



