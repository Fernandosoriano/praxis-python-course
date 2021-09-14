import re
import json

class tree_build:
    def __init__(self,expression):

        if(re.search(r"([0-9]|[+\-*/]|[()])",expression) and re.search(r"([0-9]|\(.+\))[*\-+/]([0-9]|\(.+\))",expression)):
            self.main = expression
        else:
            raise ValueError("expression is not mathematical")
    
    def replace_mat(self,exp:str):
        temp_str= exp
        transp = []
        parn_index = 0
        hyper_num=''
        for index in range(len(temp_str)):
            if(temp_str[index] in "0123456789"):
                hyper_num+=temp_str[index]
                if( index<(len(temp_str)-1) and temp_str[index+1]in"0123456789" ):
                    continue
                else:
                    transp.append({"num":str(hyper_num),"lvl":parn_index})
                    hyper_num=''
            elif(temp_str[index] in "+-/*"):
                transp.append({"op":temp_str[index], "lvl":parn_index})
            elif(temp_str[index] in "("):
                parn_index+=1
                transp.append({"pi":parn_index, "lvl":parn_index})
            elif(temp_str[index] in ")"):
                transp.append({"po":parn_index, "lvl":parn_index})
                parn_index-=1
            else:
                new_str+=temp_str[index]
        return transp

    def build(self):
        temp_string = self.main 
        self.list = self.replace_mat(temp_string)
        deepest = 0
        self.ordenate_list = {}
        for item in self.list:
            if(item['lvl']>deepest):
                deepest=item['lvl']
        advance = deepest
        while advance>-1:
            temp_set = []
            obj = {"lft":None,"op":None,"rgt":None}
            left = False
            op = False
            for item in self.list:
                if item.get('lvl') == advance :
                    if(item.get('num')!=None and not left):
                        left=True
                        obj['lft']=item.get('num')
                        continue
                    if(item.get("op")!=None and not op):
                        op=True
                        obj['op']=item.get("op")
                        continue
                    if item.get('num') and left:
                        left=False
                        op=False
                        obj['rgt']=item.get('num')
                        temp_set.append(obj)
                        obj = {"lft":None,"op":None,"rgt":None}
                        continue
                elif( item.get('lft')!=None ):
                    if not left:
                        left = True 
                        obj['lft'] = item
                        continue
                    elif left:
                        left = False
                        op = False
                        obj['rgt'] = item
                        temp_set.append(obj)
                        obj = {"lft":None,"op":None,"rgt":None}
                        continue
                elif(item.get('pi')!=None or item.get('po')!=None):
                    continue
                else:
                    temp_set.append(item)
                    continue
            self.list = temp_set
            advance-=1
        return self.list
        
    def get_prefix_note(self):
        def recursive(node):
            #### OP
            print('(',node.get("op"),'',end='')
            #### RIGHT
            if(type(node.get("lft"))!=type('')):
                # print("(",end='')
                recursive(node.get("lft"))
            else:
                print(node.get("lft"),'',end='')
            #### LEFT
            if(type(node.get("rgt"))!=type('')):
                recursive(node.get("rgt"))
                print(")",end='')
            else:
                print(node.get("rgt"),")",end='')
        recursive(self.list[0])

    def get_subfix_note(self):
        def recursive(node):
            #### RIGHT
            if(type(node.get("lft"))!=type('')):
                print("(",end='')
                recursive(node.get("lft"))
            else:
                print('(',node.get("lft"),'',end='')
            #### LEFT
            if(type(node.get("rgt"))!=type('')):
                recursive(node.get("rgt"))
                print("",end='')
            else:
                print(node.get("rgt"),"",end='')
            #### OP
            print('',node.get("op"),')',end='')
        recursive(self.list[0])
            
    def get_infix_note(self):
        def recursive(node):
            #### RIGHT
            if(type(node.get("lft"))!=type('')):
                print("(",end='')
                recursive(node.get("lft"))
            else:
                print("(",node.get("lft"),'',end='')
            #### OP
            print(node.get("op"),'',end='')
            #### LEFT
            if(type(node.get("rgt"))!=type('')):
                recursive(node.get("rgt"))
                print(")",end='')
            else:
                print(node.get("rgt"),")",end='')
        recursive(self.list[0])


if __name__ == '__main__':
    input_exp = input("una expresion matemática:- ")
    tree=tree_build(input_exp)
    tree.build()
    opt = input("seleccione el tipo de notacion que prefiere\n\t1 (prefija)\n\t2 (infija)\n\t3 (subfija)\n\n\t:- ")
    print("######## resultado ########")
    if(opt=='1'):
        tree.get_prefix_note()
    if(opt=='2'):
        tree.get_infix_note()
    if(opt=='3'):
        tree.get_subfix_note()
    print(f"\n\n\n\n objeto real sobre el cual se calcula la notación:\n{tree.list}")

print ('no entiendo qué es o que está explicando este señor, pero lo intentaré algún día, para que 
no me quede atrás')