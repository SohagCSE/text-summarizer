from sentence_tf import sentence_tf
import math

class scoring:
    def __init__(self,sentence_list,proper_noun):
        self.sentence_list = sentence_list
        self.proper_noun = proper_noun
        self.sentence_tf_list = []
        self.entire_unq_word = set()
        self.all_word_idf_dict = dict()
        self.sentence_score_list = []



    def score_update(self):
        sentence_score = []
        for snt in self.sentence_tf_list:
            snt_score = 0
            for word in snt.words:
                word_score = self.all_word_idf_dict[word]*snt.unq_word_tf_dict[word]
                snt_score = snt_score + word_score
                if word in self.proper_noun:
                    snt_score += 1
                #print(snt_score,"    ",word_score)
            sentence_score.append(snt_score)
        self.sentence_score_list = sentence_score

    


    def idf_update(self):
        all_unq_word_amount = len(self.entire_unq_word)
        all_idf_list = []
        for word in self.entire_unq_word:
            cnt = 0
            for snt in self.sentence_tf_list:
                if word in snt.unq_word:
                    cnt += 1

            all_idf_list.append(math.log(all_unq_word_amount/cnt))

        self.all_word_idf_dict = dict(zip(self.entire_unq_word,all_idf_list))

        self.score_update()





    def update(self):
        sentence_tf_list = []
        words_set = set()
        for line in self.sentence_list:
            snt_tf = sentence_tf(line)
            snt_tf.unq_word_update()
            
            self.entire_unq_word.update(snt_tf.unq_word)

            sentence_tf_list.append(snt_tf)
            
        self.sentence_tf_list = sentence_tf_list

        self.idf_update()
            
        
            

    



    
