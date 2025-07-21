



def list_neighbors(node):
    dirs=[[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]
    result=[]
    for dir in dirs:
        neighbor=([node[0]+dir[0], node[1]+dir[1]])
        if neighbor in all_nodes:
            result.append(neighbor)
    return result


all_nodes=[]
for x in range(5):
    for y in range(6):
        all_nodes.append([x,y])

letters=['E','K','Ö','H','S','U','R','P','Ä','T','Ä','U','O','K','M','I','I','K','R','O','E','R','H','K','T','T','E','T','O','I']

def print_board(letters):
    for y in range(6):
        for x in range(5):
            print(letters[y*5+x])
        print('\n')

def load_dictionary():
    file=open("dictionary.txt")
    return file

def filter_dict(word, sub_dictionary)
    #return all words continuing from currently checked letter chain, if none found ..., if one found, if multiple found
    for letter in word:
        found=0
        for i in sub_dictionary: 
            if i[0:len(word)] != word:    
                sub_dictionary.remove(i)
    return sub_dictionary

def check_node(node, sub_dict)
    

def chain(root)
    neighbors=list_neighbors(root)
    sub_dict=filter_dict(root, dictionary)
    for i in neighbors:
        word=root.append(i)
        sub_dict=filter_dict(word,sub_dict)
        if not sub_dict:
            continue
        elif len(sub_dict)==1:
            result.append(word)
            continue
        for j in i:
            word=word.append(j)


        

def traverse(root)
    for root in all_nodes:

    


test=[]
print(all_nodes)
for i in all_nodes:
    for k in i:
        all_nodes[k]=0
print(len(all_nodes))
print(all_nodes)
print_board(letters)
