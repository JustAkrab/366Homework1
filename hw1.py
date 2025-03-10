


# dictionary_one = {}
padded_list = []
with open('train-Spring2025.txt', 'r', encoding="utf8") as f:
    for line in f:
            # print(line)
        sen = "<s> " + line.rstrip() + " </s>"
        spit = sen.split()
        for i in range(len(spit)):
            # print(i.lower())
            spit[i] = spit[i].lower()
        print(spit)

        # print(spit)
        


with open('test.txt', 'r') as tf:
    for rine in tf:
        sin = "<s> " + line.rstrip() + " </s>"
        sprint = sin.split()
        print(sprint)



    
    # with open('train-Spring2025.txt', 'r', encoding="utf8") as wf:
    #     for write in 

            
            
    
        
    