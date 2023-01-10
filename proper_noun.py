import codecs
import re


def noun_reader():
    file = codecs.open("proper_noun.txt","r","utf8")
    text = file.read()
    text_list = text.split('\r\n')
    text_list[0] = text_list[0][1:] #removing some unwanted garbage on first "word"
    noun_list = text_list
    file.close()
    return noun_list
