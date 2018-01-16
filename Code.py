#========================================================#
def iterate_list(list_name):
    for items in list_name:
        print(items,end=" ")
#========================================================#        
def word_mixer(word_list):
    word_list=poem.split()
    #print("poem as words_list:",word_list)

    length=len(word_list)
    for index in range(length):
        if len(word_list[index])<=5:
            word_list[index]=word_list[index].lower()
        else:
            word_list[index]=word_list[index].upper()
    #print("Before word_mixer: word_list: ",word_list)
    word_list.sort()
    new_words=[]
    while len(word_list)>5:
        new_words.append(word_list.pop(-5))
        #print("after 1st append new_words:",new_words)
        new_words.append(word_list.pop(0))
        #print("after 2nd append new_words:",new_words)
        new_words.append(word_list.pop(-1))
        #print("after 3rd append new_words:",new_words)
        new_words.append("\n")
    new_words.extend(word_list)
    return iterate_list(new_words)
#========================================================#        

poem=input("Enter your poem: ")

word_mixer(word_list)

#twinkle twinkle little star!! , how i wonder what you are?#
#or
#Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?
