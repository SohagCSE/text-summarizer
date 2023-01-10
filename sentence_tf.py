class sentence_tf:
    def __init__(self,sentence):
        self.sentence = sentence
        self.words = sentence.split()
        self.words_cnt = len(self.words)
        self.unq_word = set(self.words)
        self.unq_word_cnt = []
        self.unq_word_tf = []
        self.unq_word_tf_dict = dict()
        

    

    def unq_word_update(self):
        unq_cnt = []
        each_tf = []
        for word in self.unq_word:
            cnt = self.words.count(word)
            unq_cnt.append(cnt)
            tf = cnt/self.words_cnt
            each_tf.append(tf)

        self.unq_word_cnt = list(zip(self.unq_word,unq_cnt))
        self.unq_word_tf = list(zip(self.unq_word,each_tf))
        self.unq_word_tf_dict = dict(self.unq_word_tf)

