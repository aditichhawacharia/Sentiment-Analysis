from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


positive_response = sentiment_analyzer('I love working with Python')
print(positive_response)

negative_response = sentiment_analyzer('I hate working with Pyhton')
print (negative_response)

neutral_response = sentiment_analyzer("I am neutral on Python")
print (neutral_response)
