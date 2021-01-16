'''
	A file contains a set of 30 multiple choice questions with four choices among which one is a correct answer. Write a python program to display and evaluate the answers in such a way that the questions appear in a random order and the choices are also jumbled.
'''

import csv
from random import sample
# import pandas


class Quiz:
    def __init__(self) -> None:
        self.problem = dict()
        self.dip_qp, cpd_ans = [], []
        self.crct_ans, self.marks = 0, 0

    def read_csv(self) -> None:
        """
        Reads from the csv file
        """
        with open('qp.csv') as file:
            rd = csv.reader(file)
            for idx, row in enumerate(rd):
                if idx == 0:  # skip the first row
                    continue
                self.problem[row[1]] = row[2:6]

        # for k, v in self.problem.items():
        #    print(len(v))

    def control(self) -> None:
        """
        Main control of the loop
        """
        all_ques = self.problem.keys()
        self.dip_qp = sample(all_ques, k=len(all_ques))
        for ctr, q_dip in enumerate(self.dip_qp):
            a_ans = self.problem[q_dip]
            self.cpd_ans = sample(a_ans, k=len(a_ans))
            self.crct_ans = sample([1, 2, 3, 4], k=1)
            self.disp_prob(ctr, q_dip)

        print(f"Total Marks: {self.marks}")

    def disp_prob(self, ctr, cur_ques) -> None:
        """
        Displays question as waits for answer
        """
        print(str(ctr+1) + '.', cur_ques)
        print(self.cpd_ans)
        ip = input()
        if ip == self.crct_ans:
            self.marks += 10        # TODO: Need to run unit-tests


if __name__ == "__main__":
    qz = Quiz()
    qz.read_csv()
    qz.control()
