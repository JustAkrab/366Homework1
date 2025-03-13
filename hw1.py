


dictionary_one = {}
dictionary_two = {}
padded_list = []
del_counter = 0
with open('train-Spring2025.txt', 'r', encoding="utf8") as f:
    for line in f:
            # print(line)
            # padding
        sen = "<s> " + line.rstrip() + " </s>"
        spit = sen.split()
        # apply each word to be lowercase
        for i in range(len(spit)):
            # print(i.lower())
            spit[i] = spit[i].lower()
            dictionary_one[spit[i]] = dictionary_one.get(spit[i], 0) + 1
            if i != 0:
                dictionary_two[spit[i] + spit[i-1]] = dictionary_two.get((spit[i] + spit[i-1]), 0) + 1
for i in list(dictionary_one.keys()):
    if dictionary_one.get(i) == 1:
        del dictionary_one[i]
        # print(del_counter)
        del_counter += 1
dictionary_one["<unk>"] = del_counter
# print(dictionary_one)





        # print(spit)

        # Replace all words occurring in the training data once with the token <unk>. Every word
        # in the test data not seen in training should be treated as <unk>



        # print(spit)
        
word = None
unigram_sum = 0
bigram_sum = 0
word_in_sentence = 0
unigram_dictionary = {}
with open('test.txt', 'r') as tf:
    for rine in tf:
        sin = "<s> " + rine.rstrip() + " </s>"
        sprint = sin.split()
        # print(sprint)
        unigram_sum = 0
        for j in range(len(sprint)):
            sprint[j] = sprint[j].lower()
            for m in range(j+1, len(sprint)):
                if sprint[m] == sprint[j]:
                    word_in_sentence += 1
                    # print(word_in_sentence)
            word = sprint[j]
            # print(word)
            if word not in dictionary_one.keys():
                word_in_sentence = 0
                continue
            # print(word)
            # print("uigram Dictionary: ", dictionary_one.get(word))
            # print("word count in sentence: ", word_in_sentence)
            # print("Unigram Prob: ", unigram_sum)
            unigram_sum = (word_in_sentence/dictionary_one.get(word))
            
            # word_in_sentence = 0
            unigram_dictionary[word] = unigram_dictionary.get(word, unigram_sum)
        for string in range(1, len(sprint)):
            print(sprint[string - 1])
        
# print(unigram_dictionary)
        
            


        # print(sprint)




    
    # with open('train-Spring2025.txt', 'r', encoding="utf8") as wf:
    #     for write in 


# bigram logic



#unigram logic




# trigram logic



            
            
    
        
    
