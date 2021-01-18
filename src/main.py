import csv
import streamlit as slt
from random import sample


class Quiz:
    def __init__(self) -> None:
        self.problem = dict()
        self.dip_qp, self.cpd_ans = [], []
        self.crct_ans, self.sel_ans, self.marks = [], [], 0

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

    def control(self) -> None:
        """
        Main control of the loop
        """
        all_ques = self.problem.keys()
        self.dip_qp = sample(all_ques, k=len(all_ques))
        for ctr, q_dip in enumerate(self.dip_qp):
            a_ans = self.problem[q_dip]
            self.cpd_ans = sample(a_ans, k=len(a_ans))
            self.crct_ans.append(sample(a_ans, k=1))
            self.sel_ans.append(slt.radio(str(ctr + 1) + '. ' + q_dip, (*self.cpd_ans,)))
        
        if slt.button("Submit"):
            for idx, _ in enumerate(self.dip_qp):
                if self.crct_ans[idx] == self.sel_ans[idx]:
                    self.marks += 10
            slt.write(self.marks)

        print(f"Total Marks: {self.marks}")


if __name__ == "__main__":
    qz = Quiz()
    qz.read_csv()
    qz.control()