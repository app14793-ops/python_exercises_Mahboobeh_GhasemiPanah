def count_letter_with_for(word,letter):
    count=0
    for i in word:
        if i==letter:
            count+=1
    return count        


def count_letter_without_for(word,letter):
    count=word.count("a")
    
    return count 

word=input("enter word: ")
letter=input("enter letter: ")
print(count_letter_without_for(word, letter))
print(count_letter_with_for(word, letter))


