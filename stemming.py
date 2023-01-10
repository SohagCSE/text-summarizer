from rules import rules
import re

def remove_suffix(s,r):
    s = s[::-1]
    r = r[::-1]
    res = ""
    for i in range(0,len(s)):
        if i<len(r):
            if r[i] == '.':
                res = res + s[i]
        else:
            res = res + s[i]
    return res[::-1]



def add_suffix(s,r):
    s = s[::-1]
    r = r[::-1]
    res = ""
    for i in range(0,len(s)):
        if i<len(r):
            if r[i] == '.':
                res = res + s[i]
            else:
                res = res + r[i]
                res = res + s[i]
        else:
            res = res + s[i]
    return res[::-1]





class stem:
    def __init__(self):
        self.rule = rules()
        self.rule_list = self.rule.read_rules()
        self.rule_replace = self.rule.read_replace_rules()


    def stemmed(self,w):
        for r in self.rule_list:
            ptrn = re.compile(".*"+r+"$")
            #print(ptrn)
            if ptrn.match(w):
                if "." not in r:
                    w = w[:len(w)-len(r)]
                    #print(r," -----",w)
                    if r in self.rule_replace:
                        w = add_suffix(w,r)
                        #print(r," -----",w)
                    break
                else:
                    w = remove_suffix(w,r)
                    if r in self.rule_replace:
                        w = add_suffix(w,self.rule_replace[r])
                        #print(r," -----",w)
                    break

        return w




