import csv
import streamlit as slt
from random import sample

problem = dict()
marks, ctr = 0, 1

def rdn_question_gen():
    for question in rdn_ques:
        all_options = problem[question]
        rdn_options = sample(all_options, k=len(all_options))
        correct_ans = sample(rdn_options, k=1)
        yield question, rdn_options, correct_ans

if __name__ == "__main__":

    with open('qp.csv') as fo:
        contents = csv.reader(fo)
        for idx, row in enumerate(contents):
            problem[row[1]] = row[2:6]

    problem.pop('Question _Text', None)

    all_ques = problem.keys()
    no_of_q = len(all_ques)
    rdn_ques = sample(all_ques, k=no_of_q)

    pb_set = rdn_question_gen()
    nxt_pb = next(pb_set)
    sel_ans = slt.radio(str(ctr) + '. ' + nxt_pb[0], nxt_pb[1])

    if sel_ans == nxt_pb[2]:
        marks += 10

    ctr += 1
    slt.write(f"Marks: {marks}")

    if ctr >= no_of_q:
        slt.write(f"Thanks for taking the quiz!")
