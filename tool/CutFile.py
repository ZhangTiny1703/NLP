# -*- coding:utf-8 -*-

# 中文分词

import sys
import os

# 设置分句的标志符号
cutlist = "。！？.!?"
punct_pair_str = "《》“”‘’{}（）()【】\"\""
punct_pair_hm = {}

sent_count = 0

# 检查某字符是否分句标志符号的函数；如果是，返回True， 否则返回False
def FindTok(char):
    global cutlist
    if char in cutlist:
        return True
    else:
        return False


def CutSent(cut_str):
    sent_list = []
    sent = []
    punct_pair = []
    for ch in cut_str:
        AddPunct(punct_pair, ch)
        if FindTok(ch):
            sent.append(ch)
            if len(punct_pair) == 0:
                sent_list.append(''.join(sent))
                sent = []
                punct_pair = []
        else:
            sent.append(ch)

    if len(sent) != 0:
        sent_list.append(''.join('%s' %i for i in sent))

    return sent_list


def ConstPunctPair():
    global punct_pair_str, punct_pair_hm

    for index in range(0, len(punct_pair_str), 2):
        punct_pair_hm[punct_pair_str[index + 1]] = punct_pair_str[index]
