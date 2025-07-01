



def neighbors(node):
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

def check_word(chain)
    #return all words continuing from currently checked letter chain, if none found ..., if one found, if multiple found
    words=[]
    
    for i in dictionary:
        if i[len(chain)]==word:
            words.append(i)

    return words
def score_board(words):


test=[]
print(all_nodes)
for i in all_nodes:
    for k in i:
        all_nodes[k]=0
print(len(all_nodes))
print(all_nodes)
print_board(letters)
