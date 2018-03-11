#Import Libraries and create a makeshift loading screen
import os
print("please wait For a few moments")
from textblob import TextBlob

#clear terminal of loading screen
os.system('clear')

#User Input for rating
Rating=raw_input("what is your review:")
#convert to TextBlob String
rating= TextBlob(Rating)
#covert out of 100 to out of 5
User_rating= rating.sentiment.polarity*5
#print out rating
print ("expected User rating:"+str(User_rating)+"/5")
