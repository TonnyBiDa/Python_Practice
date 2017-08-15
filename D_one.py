# guess word game~
import re
def third_func():
    global input_aim
    global i
    global store_y
    i=0
    store_y=[]
    input_aim = raw_input('Enter the secret word(all in lowcrease):')
    if not re.match('^[a-z]',input_aim):
        print('Error, plz enter again~\n')
        return third_func()
    else:
        print('================================================================\n')
        return first_func(input_aim)
        
def second_func(y,x):
    #print(x)
    #print(y)
    global zz
    global cpy
    global store_y
    global surplus
    list_aim=[]
    if y in x:
        print('Got it!\n')
        #remain_word=x.replace(y,'')
        #print(a)
        store_y.append(y)
        for bb in x:
            list_aim.append(bb)
        #print(store_y)
        #print(list_aim)
        #if i in list_aim and i in store_y:
        if set(store_y)==set(list_aim):
            print('Congratulations. You correctly guessed the word: {}'.format(input_aim))
            again_input=raw_input('Do you want to play one more time? y/n?')
            if again_input=='y':
                print('\n')
                return third_func()
            else:
                return None
        else:
            #compared_two_list=list(set(store_y).intersection(set(list_aim)))
            #print(compared_two_list)
            zz=list(set(list_aim).difference(set(store_y)))
            aa=''.join(list_aim)
            bb=''.join(zz)
            cc='['
            dd=']'
            gg=cc+bb+dd
            surplus=re.sub(gg,'*',aa)
            #print(surplus)
            return first_func(surplus)
    elif i>1:
        print('Sorry!\n')
        return first_func(surplus)
    else:
        print('Sorry!\n')
        return first_func(input_aim)
            

def first_func(x):
    #print(x)
    global i
    global store_y
    global surplus
    for z in x:
        if z=='*':
            #print(1)
            z=x
            break
        else:
            #print(2)
            z=len(x)*'*'
    i+=1    
    #print(aim)
    #print(z)
    print('Word so far:{}'.format(z))
    input_word=raw_input('Take guess number {} :'.format(i))
    if re.match('^[a-z]',input_word):
        if len(input_word)!=1:
            print('plz enter only one letter\n')
            return first_func(input_aim)
        else:
            return second_func(input_word,input_aim)
    else:
        print('plz enter letter~\n')
        return first_func(input_aim)
third_func()

