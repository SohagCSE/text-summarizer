import codecs
import re

class rules:
    def __init__(self):
        self.rule_list = []
        self.replace_rule_dict = dict()


    def rule_reader(self):
        file = codecs.open("rules.txt","r","utf8")
        text = file.read()
        text_list = text.split('\n')
        text_list[0] = text_list[0][1:]
        self.rule_list = text_list
        file.close()


    def replace_rules_reader(self):
        file = codecs.open("rules_replace.txt","r","utf8")
        text = file.read()
        text_list = text.split('\n')
        text_list[0] = text_list[0][1:]

        list_1 = []
        list_2 = []
        for t in text_list:
            x,y = re.split('\s*->\s*',t)
            list_1.append(x)
            list_2.append(y)

        self.replace_rule_dict = dict(zip(list_1,list_2))
        file.close()



    def read_rules(self):
        if len(self.rule_list) == 0:
            self.rule_reader()
        return self.rule_list


    def read_replace_rules(self):
        if len(self.replace_rule_dict) == 0:
            self.replace_rules_reader()
        return self.replace_rule_dict
