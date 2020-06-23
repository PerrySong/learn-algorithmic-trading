"""Assess a betting strategy.  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Atlanta, Georgia 30332  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
All Rights Reserved  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Template code for CS 4646/7646  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
and other users of this template code are advised not to share it with others  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or to make it available on publicly viewable websites including repositories  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
or edited.  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
We do grant permission to share solutions privately with non-students such  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
as potential employers. However, sharing with other current or future  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT honor code violation.  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
-----do not edit anything above this line---  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
Student Name: Pengfei Song (replace with your name)  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT User ID: spfscmz (replace with your User ID)  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
GT ID: spfscmz (replace with your GT ID)  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
"""
from builtins import range

import numpy as np  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
import matplotlib.pyplot as plt
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def author():  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return 'perry'  # replace tb34 with your Georgia Tech username.  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def gtid():  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return 2697139166  # replace with your GT ID number
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def get_spin_result(win_prob):  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    result = False  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    if np.random.random() <= win_prob:  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
        result = True  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    return result  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
def test_code():  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    win_prob = 0.60  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    # add your code here to implement the experiments


def experiment_1():
    res = [0]
    for i in range(10):
        if get_spin_result(0.6):
            res.append(res[-1] + 1)
            print('win!')
        else:
            res.append(res[-1] + -1)
            print('lose!')

    # plt.xlim(0, 300)
    # plt.ylim(-256, 100)
    plt.plot(range(10), res[1:])
    plt.savefig('./martingale.png')


  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
if __name__ == "__main__":  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    test_code()  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    experiment_1()