C:\python folder\shakespeare_content_analysis.py
Code:
import string
import matplotlib.pyplot as plt 

#Shakespeare text
text = """
ROMEO.
There is no world without Verona walls,
But purgatory, torture, hell itself.
Hence banished is banishd from the world,
And world is exile is death. Then banished
Is death mistermed. Calling death banished,
Thou cutt'st my head off with a golden axe,
And smile upon the stroke that murders me.
"""

#Converting to lowercase
text = text.lower()

#Removing punctuation
for p in string.punctuation:
    text = text.replace(p, "")

#Tokenization (splitting into words)
words = text.split()

# Sentiment word lists
positive_words = ["love", "joy", "happy", "light", "good", "smile"]
negative_words = ["hate", "sad", "dark", "pain", "anger", "sadness","death"]

positive_count = 0
negative_count = 0

for w in words:
    if w in positive_words:
        positive_count += 1
    elif w in negative_words:
        negative_count += 1

#Decide sentiments
if positive_count > negative_count:
    sentiment = "Positive sentiment"
elif negative_count > positive_count:
    sentiment = "Negative sentiment"
else:
    sentiment = "Neutral sentiment"

#results
print("Text:", text)
print("Positive words:", positive_count)
print("Negative words:", negative_count)
print("Final Sentiment:", sentiment)

# Plot graph
labels = ["Positive", "Negative"]
values = [positive_count, negative_count]

plt.figure()
plt.bar(labels, values)
plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment Type")
plt.ylabel("Count")
plt.show() 
