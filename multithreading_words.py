import concurrent.features 
import time 
import re 

def num_of_words(sentence):
    '''Find number of words in a sentence'''
    num_of_words = len(sentence.split())
    print("\nNumber of words in the sentence : {}".format(num_of_words))
    time.sleep(1)

def num_of_characters(sentence):
    '''Find number of characters in a sentence'''
    num_of_characters = len(sentence)
    print("\nNumber of characters in the sentence : {}".format(num_of_characters))
    time.sleep(1)

def num_of_vowels(sentence):
    '''Find the number of vowels in the sentence'''
    regexPattern = re.compile('[aeiouAEIOU')
    #Finding the defined regex pattern in the sentence
    listOfMatches = regexPattern.findall(sentence)
    print("\nNumber of vowels in the sentence : {}".format(len(listOfMatches)))
    time.sleep(1)

if __name__=="__main__":
    sentence = "Multithreading is an important feature for any programming language."
    #Start counter to keep track of time
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        futures = []
        #assign tasks for threads 
        futures.append(executor.submit(num_of_words, (sentence)))
        futures.append(executor.submit(num_of_characters, (sentence)))
        futures.append(executor.submit(num_of_vowels, (sentence)))
        #wait until all threads are complete
    #end counter 
    finish = time.perf_counter()
    #Log the total time taken 
    print("\nFinished in {} second(s)".format(round(finish-start, 2)))
    
