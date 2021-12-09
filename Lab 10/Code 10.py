import operator
from string import punctuation

while True:
    """
    Ask user for the name of file
    """
    filename = input("Enter the name of the file to open ")

    """
    open file using with-as 
    put code that deals with file inside
    try block to handle any exception that might occur such as
    file not found. 
    in case exception occur except block will execute and repeat
    the file loop. 
    """
    try:
        with open(filename) as file:
            """
            Creating an empty dictionary.
            this dict will hold each unique word as key
            and its occurrence as value.
            """
            word_dict = dict()
            """
            Loop through each line in file.
            """
            for line in file:
                """
                loop through each word in line
                """
                for word in line.strip().split(" "):
                    """ Remove punctuation from word
                    using strip() function, by passing
                    punctuation as parameter.
                    punctuation is pre-initialized string and defined in string module
                    of python.
                    """
                    word = word.strip(punctuation)
                    """
                    check if this word has length greater than.
                    if no then do not add this word in
                    word_dict
                    """
                    if len(word) <= 3:
                        continue
                    else:
                        """
                        Check if this word is already added
                        to the word_dict as key or not 
                        if no then add this word as key and 1 as value
                        if already added then increment value by 1.
                        """
                        if word in word_dict.keys():
                            word_dict[word] = word_dict[word] + 1
                        else:
                            word_dict[word] = 1

            """
            Now we have all unique word having length greater than 3
            as key of word_dict and its occurrence of that word as value.
            """
            """
            sort word diction in descending order
            """
            word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))
            """
            print top 10 words that are most used.
            """
            counter = 1
            print("Most frequently used words")
            print("{:>0}{:>15}{:>15}".format('#', 'Word', 'Freq.'))
            print("{:>15}".format("==============================="))
            for key in word_dict:
                if counter > 10:
                    break
                else:
                    frequency = word_dict[key]
                    print("{:>0}{:>15}{:>15}".format(counter, key, frequency))
                    counter += 1

            """ counts all words that occur only once """
            onceCounter = 0
            for key in word_dict:
                if word_dict[key] == 1:
                    onceCounter += 1
            """ get total element in word_dict using len() function this
            will give the total count of unique words"""

            uniqueCounter = len(word_dict)

            """ print total number of words that occur once 
            and total unique words """
            print(f"There are {onceCounter} words that occur only once")
            print(f"There are {uniqueCounter} unique words in the document")

    except:
        print("Could not open file",filename)
        print("Please Try Again\n")
        continue
    else:
        break
