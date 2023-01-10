import codecs
import re

class doc_read:
    def __init__(self,input_dir):
        file = codecs.open(input_dir,"r","utf8")
        text = file.read()
        sentence_list = re.split('\s*।\s*',text)
        sentence_list[0] = sentence_list[0][1:]

        self.all_sentence = sentence_list
        file.close()
        

    def all_sentense(self):
        return self.all_sentence



class doc_write:
    def __init__(self,sentence_list,output_dir):
        file = codecs.open(output_dir,"w","utf8")

        text = ""
        for sentence in sentence_list:
            text = text + sentence + " । "
            
        print(text)
        file.write(text)
        file.close()
        
