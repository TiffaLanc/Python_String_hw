# Task 1 Keyword Highlighter: Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

reviews =  ["This product is really good. I'm impressed with its quality.",
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.",
"Poor quality product. Wouldn't recommend it to anyone.",
"The product was average. Nothing extraordinary about it."]
    

keywords = ["good", "bad", "poor", "excellent", "average"]

def replace_cap_keywords(reviews, keywords):
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.swapcase())
            review = review.replace(keyword.capitalize(), keyword.upper())
        print(review)

replace_cap_keywords(reviews, keywords)       
      


# Task 2 Sentinment Tally: Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.


pos_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
neg_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]



def word_tally(reviews, pos_words, neg_words):
  pos = 0
  neg = 0

  for review in reviews:
    words = review.lower().replace('.','').replace(',','').replace('!','').replace('?','').split()
    for word in words:
        if word in pos_words:
            pos += 1
        elif word in neg_words:
            neg += 1
            return pos, neg

pos, neg = word_tally(reviews, pos_words, neg_words)
print(f"Total positive words are: ", pos)
print(f"Total negative words are: ", neg)


         

# Task 3 Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
#Example: "This product is really good. I'm...",


def script(review):
    
    summary = review[:30]
   
    if len(review) > 30:
       
        last_space_index = summary.rfind(' ')
       
        if last_space_index != -1:
            summary = summary[:last_space_index]
      
        summary += "…"
    return summary

for review in reviews:
    summary = script(review)
    print(summary)


  