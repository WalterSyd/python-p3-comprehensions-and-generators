#!/usr/bin/env python3
num_list = [0, 1, 3, 5, 7, 8, 9]
def return_evens(num_list):
    '''This line creates a new list containing only the even numbers [as per condition spec] from the original num_list.'''
    num_list = [n for n in num_list if n % 2 == 0]
    '''Checking for Empty List'''
    if len(num_list) == 0:
        return []
    else:
        '''Returning List of Evens'''
        return num_list

# save the result in a variable and print
result = return_evens(num_list)
print(result)



sentence_list = ["I like computers", "I require coffee", "Live long and prosper"]
def make_exclamation(sentence_list):
    '''This line creates a new list containing only the sentences with exclamation marks at the end [as per condition spec] from the original sentence_list and adds an exclamation if the sentence did not have one before'''
    sentence_list = [s + "!" for s in sentence_list if s[-1] != "!"]
    '''Checking for Empty List'''
    if len(sentence_list) == 0:
        return []
    else:
        '''Returning List of Sentences with Exclamation Marks'''
        return sentence_list

# save the result in a variable and print
result = make_exclamation(sentence_list)
print(result)