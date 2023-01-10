from document_read_write import doc_read,doc_write
from stemming import stem
from tf_idf_score import scoring
from proper_noun import noun_reader
from cluster_3 import cluster_3
import re
import operator


def choose_one_third(score):
    if len(score)<3:
        sz = 1
    else:
        sz = (int)(len(score)/3)
    score = score[:sz]
    return score


all_sentence_list = []
stemmed_sentence_list = []



document = doc_read("input2.txt")
all_sentence_list = document.all_sentence



stm = stem()
for s in all_sentence_list:
    word_list = re.split('\s+',s)
    new_snt = ""
    for w in word_list:
        if new_snt == "":
            new_snt = new_snt + stm.stemmed(w)
        else:
            new_snt = new_snt + " " + stm.stemmed(w)

    stemmed_sentence_list.append(new_snt)



proper_noun = noun_reader()
proper_noun = [x for x in proper_noun if x!='']



snt_scr = scoring(stemmed_sentence_list,proper_noun)
snt_scr.update()
snt_scr_list = snt_scr.sentence_score_list



score = list(zip(all_sentence_list,snt_scr_list))

score = [item for item in score if item[0] != '']   # remove empty sentence


#--- if you want to sort before cluster then comment out below line
#score.sort(key=operator.itemgetter(1),reverse=True)


cluster_obj = cluster_3(score)
list_1,list_2,list_3 = cluster_obj.k_mean_3()


#--- comment out below three line to see output with sorted score
#list_1.sort(key=operator.itemgetter(1),reverse=True)
#list_2.sort(key=operator.itemgetter(1),reverse=True)
#list_3.sort(key=operator.itemgetter(1),reverse=True)


summary = []

print("\n\ncluster - 1:\n")
list_1 = list(zip(*list_1))
print(list_1)
summary += choose_one_third(list_1[0])

print("\n\ncluster - 2:\n")
list_2 = list(zip(*list_2))
print(list_2)
summary += choose_one_third(list_2[0])

print("\n\ncluster - 3:\n")
list_3 = list(zip(*list_3))
print(list_3)
summary += choose_one_third(list_3[0])






print("\n\n\n\n\n summary:\n")
doc_write(summary,"output.txt")


