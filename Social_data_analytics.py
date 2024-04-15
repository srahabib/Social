#!/usr/bin/env python
# coding: utf-8

# ## Sentiment Forecasting for Cryptocurrency Trends: Predicting Market Sentiment from Social Media Data

# ![image.png](attachment:image.png)

# ## Metadata

# | Column Name | Description |
# :------------|:----------
# |user_name | This variable contains the username of the user who tweeted the content.|
# |    date    | This variable represents the date when the content was posted. |
# | likes    | This variable stores the number of likes that the content received. |
# | retweets | This variable stores the number of retweets that the content received. |
# | content | This variable contains the actual text content of the tweet. |
# | hashtags | This variable contains any hashtags included in the content, if applicable. |

# ## Importing libraries

# In[33]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import re


# ## Import dataset

# In[3]:


df = pd.read_csv("crypto_tweets.csv", index_col=0)
df.head()


# ## EDA and Cleaning

# In[4]:


print('\033[1m' + 'Shape of the data (rows, columns):' + '\033[0m')
print(df.shape)


# In[5]:


for col in df.columns:
    print('\033[1m' + 'Unique values in {} :'.format(col) +
          '\033[0m', len(df[col].unique()))


# ## Function to detect missing values

# In[6]:


def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    table = pd.concat([mis_val, mis_val_percent], axis=1)

    col_names = table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})

    col_names = col_names[col_names.iloc[:, 1] != 0].sort_values('% of Total Values',
                                                                 ascending=False).round(1)

    print("Dataframe has " + str(df.shape[1]) + " columns,"
          "And there exist " + str(col_names.shape[0]) +
          " column with missing value(s)")

    return col_names


summary = missing_values_table(df)
summary


# ## Visualize missing values

# In[7]:


plt.figure(figsize=(10, 5), dpi=100)
sns.heatmap(df.isna(), alpha=0.3)


# ## Detect missing values

# In[8]:


print('\033[1m' + 'Number of duplicate values :' + '\033[0m')
print(df.duplicated().sum())


# ## Function to remove emojies

# In[9]:


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    clean = emoji_pattern.sub(r'', text)  # no emoji
    return clean


# ## Remove hashtag signs emojies and links

# In[10]:


def cleansing(tweet: str):
    # Remove hashtag sign but keep the text
    content = tweet.replace("\n", " ").replace("#", "").replace(
        "_", " ").replace("@", "").replace('&amp;', 'and')
    # Remove emojis
    content = remove_emoji(content)
    # Remove any links
    content = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", content)
    content = re.sub('&lt;/?[a-z]+&gt;', '', content)

    return content.strip()


# ## Save clean data

# In[11]:


df["clean"] = df["content"].apply(cleansing)
tweets = pd.DataFrame(df["clean"])
tweets.columns = ["text"]
tweets.head()


# ## TextBlob

# In[12]:


tweets["polarity"] = tweets["text"].apply(
    lambda t: TextBlob(t).sentiment.polarity)
tweets["subjectivity"] = tweets["text"].apply(
    lambda t: TextBlob(t).sentiment.subjectivity)
tweets.head()


# In[13]:


tweets["polarity"].describe()


# ## Assign sentiment scores

# In[14]:


def get_sentiment(score):
    if score > 0.15:
        return "positive"
    elif score < 0.10:
        return "negative"
    else:
        return "neutral"


# In[15]:


tweets["sentiment"] = tweets["polarity"].apply(get_sentiment)
tweets.head()


# In[17]:


sentiment_counts = tweets["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']


colors = {'positive': '#00CC96', 'negative': '#EF553B', 'neutral': '#636EFA'}

fig = px.bar(sentiment_counts, x='sentiment', y='count', color='sentiment', color_discrete_map=colors,
             labels={'sentiment': 'Sentiment', 'count': 'Count'},
             title='Sentiment Bar Plot')
fig.show()


# In[16]:


fig = px.scatter(tweets, x='polarity', y='subjectivity', title='Polarity vs. Subjectivity Scatter Plot',
                 labels={'polarity': 'Polarity', 'subjectivity': 'Subjectivity'})
fig.show()


# ## Sentiment percentages

# In[18]:


sentiment_counts = tweets["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

# Define custom colors for positive, negative, and neutral sentiments
colors = {'positive': '#00CC96', 'negative': '#EF553B', 'neutral': '#636EFA'}

fig = px.pie(sentiment_counts, values='count', names='sentiment',
             labels={'sentiment': 'Sentiment', 'count': 'Count'},
             title='Sentiment Pie Plot',
             hole=0.3,  # Adjust the size of the hole in the middle of the pie
             color='sentiment', color_discrete_map=colors
             )
# Add percentage labels inside the pie slices
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()


# ## Prepare data for predictive modelling

# In[21]:


df_selected = df[['date', 'likes', 'retweets']]

# Selecting columns from tweets_df
tweets_df_selected = tweets[['text', 'polarity', 'subjectivity', 'sentiment']]

# Concatenating along the columns
data = pd.concat([df_selected, tweets_df_selected], axis=1)
data.head()


# ## SVC

# In[52]:


# Prepare the features and target variable
X = data[['likes', 'retweets', 'polarity', 'subjectivity']]
y = data['sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize Support Vector Machine (SVM) classifier model
model = SVC(kernel='linear', random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# ## Random Forest

# In[39]:


# Prepare the features and target variable
X = data[['likes', 'retweets', 'polarity', 'subjectivity']]
y = data['sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[40]:


print(classification_report(y_test, y_pred))


# In[41]:


cm = confusion_matrix(y_pred, y_test)
print('\033[1m' + 'Confusion Matrix : ' + '\033[0m')
plt.figure(dpi=100)
sns.heatmap(cm/np.sum(cm), annot=True,
            fmt='.2%')
plt.show()


# ## Some predictions for random days

# In[47]:


# Choose some data points from the test set for demonstration
demo_data_with_date = data.loc[X_test.index].sample(n=20, random_state=42)
demo_dates = demo_data_with_date['date']

# Make predictions for the selected data points
demo_predictions = model.predict(X_test)

# Combine the selected data points with their predictions
demo_df = pd.concat([demo_dates.reset_index(drop=True), pd.Series(
    demo_predictions, name='predicted_sentiment')], axis=1)

demo_df.head(20)


# ## Let's examine a day of predictions

# In[49]:


# Define the timestamps
timestamp1 = "2022-10-30 14:38:03+00:00"
timestamp2 = "2022-10-30 07:00:00+00:00"

# Filter the data for the specified timestamps
data_timestamp1 = data[data['date'] == timestamp1]
data_timestamp2 = data[data['date'] == timestamp2]

# Extract features for prediction (excluding 'text')
X_timestamp1 = data_timestamp1.drop(columns=['date', 'sentiment', 'text'])
X_timestamp2 = data_timestamp2.drop(columns=['date', 'sentiment', 'text'])

# Predict sentiment for the timestamps
prediction_timestamp1 = model.predict(X_timestamp1)
prediction_timestamp2 = model.predict(X_timestamp2)

# Print the predicted sentiment for each timestamp
print("Predicted sentiment for", timestamp1, ":", prediction_timestamp1)
print("Predicted sentiment for", timestamp2, ":", prediction_timestamp2)


# ![image.png](attachment:image.png)
