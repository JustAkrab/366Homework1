


dictionary_one = {}
padded_list = []
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
        # print(spit)

        # Replace all words occurring in the training data once with the token <unk>. Every word
        # in the test data not seen in training should be treated as <unk>



        # print(spit)
        


with open('test.txt', 'r') as tf:
    for rine in tf:
        sin = "<s> " + rine.rstrip() + " </s>"
        sprint = sin.split()
        # print(sprint)
        for j in range(len(sprint)):
            sprint[j] = sprint[j].lower()
        print(sprint)




    
    # with open('train-Spring2025.txt', 'r', encoding="utf8") as wf:
    #     for write in 


# bigram logic



#unigram logic




# trigram logic



            
            
    
        
    