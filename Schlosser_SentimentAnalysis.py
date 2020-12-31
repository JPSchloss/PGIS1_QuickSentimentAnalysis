# Assignment 4: Sentiment Analysis
# By: Jonathan Schlosser
# Date: 10/22/2019
# The code here works to identify stop words in a text and works to remove them. Within the main function is a create
# stopword dictionary function that works to load a file of stopwords and create a stopword dictionary.



def main():
    # Assigning the file to a variable called filename.
    filename = 'Grimms_Fairy_Tales.txt'
    # filename = 'Frankenstein.txt'

    # Employing a try/except clause to handle a FileNotFoundError.
    try:
        # Opening the file, reading the file, assigning the text to a string variable, and closing the file.
        text_file = open(filename, 'r')
        text_string = text_file.read()
        text_file.close()

        # Splitting the text string into a list of words.
        word_list = text_string.split()

        # Counting the words in the word list.
        word_list_count = len(word_list)

        # Calling a function to create the dictionary and assigning it to a variable.
        stopword_dictionary = create_stopword_dictionary()

        # Creating a for loop to count the words, strip the new line character, identify if the word is a stopword,
        # remove the word if it is, and add to the count in the stopword dictionary.
        for word in word_list:
            word = word.rstrip('\n')
            for key in stopword_dictionary:
                if word == key:
                    word_list.remove(word)
                    stopword_dictionary[key] = (stopword_dictionary[key] + 1)

        # Creating a variable to start the count of total stopwords.
        total_stopwords = 0

        # Getting the values of the stopwords and adding them up.
        for val in stopword_dictionary.values():
            total_stopwords += val

        # Importing the text blob package.
        from textblob import TextBlob

        # Creating a string of the words with any stopwords removed.
        separator = ' '
        text_string_no_stopwords = separator.join(word_list)

        # Creating the textblob and identifying the sentiment values for both the original wordlist and the
        # no-stopwords wordlist.
        original_text_blob = TextBlob(text_string)
        original_sentiment_value = original_text_blob.sentiment.polarity
        no_stopwords_blob = TextBlob(text_string_no_stopwords)
        no_stopwords_sentiment_value = no_stopwords_blob.sentiment.polarity

        # Printing the values found.
        print("Number of words in the text: ", word_list_count)
        print("Number of stopwords in text: ", total_stopwords)
        print("Sentiment polarity with stopwords: ", format(original_sentiment_value, ".3f"))
        print("Sentiment polarity w/o stopwords: ", format(no_stopwords_sentiment_value, ".3f"))
        print("")
        print("Number of stopwords that occur more than 10 times:")
        for key in stopword_dictionary:
            if stopword_dictionary[key] > 10:
                print('\t', key, ' occurs ', stopword_dictionary[key], ' times.')

    except FileNotFoundError:
        print('ERROR: Cannot find the file ', filename, '. Please try again.')

# Defining the create_stopword_dictionary function.
def create_stopword_dictionary():

    # Assigning the stopword list file name.
    filename = 'Smart_Stoplist.txt'

    # Creating a blank dictionary for stopwords.
    stopwords = {}

    # Try/except clause for opening the file.
    try:
        # Opening the file and reading by line.
        stopword_file = open(filename, 'r')
        stopword_string = stopword_file.readline()
        # While loop to create the dictionary with each word as the key and a value of 0.
        while stopword_string != '':
            stopword_string = stopword_string.rstrip('\n')
            stopwords[stopword_string] = 0
            stopword_string = stopword_file.readline()
        # Closing the file.
        stopword_file.close()
    except FileNotFoundError:
        print('ERROR: Cannot find the file ', filename, '. Please try again.')

    # Added a statement to remove the first line of text as it was imported into the dictionary from the file.
    if '#stop word list from SMART (Salton,1971).  Available at http://www.lextek.com/manuals/onix/stopwords2.html' in stopwords:
        del stopwords['#stop word list from SMART (Salton,1971).  Available at http://www.lextek.com/manuals/onix/stopwords2.html']

    # Returning the stopword dictionary.
    return stopwords

# Calling the main function. 
main()
