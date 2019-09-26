import os
import random
import numpy as np
from neural_network import neural_heuristic, transform 
from board import Board
from intelligence import a_star, manhattan_heuristic, Judge_Whether_Have_A_Solution
import time

def main(epoch):
  epoch = str(epoch)
  game = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
  goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
  game = np.array(game).reshape(4,4)
  game = Board(game)
  random_step = random.randint(25, 35)
  # 打乱25-35步 -> 因为神经网络只训练到了35步, 后面的训练速度太慢了
  game.scramble(random_step)

  if not Judge_Whether_Have_A_Solution(game.board.flatten(), goal):
    return 'fail'
  else:
    print("\n--------------------\nEpoch{}\nRandom Step is {}\n{}\n--------------------\n".format(epoch,random_step, game.board))

  # 进行启发函数等于neural部分
  neural_start = time.time()
  path = a_star(game, neural_heuristic)
  neural_end_time = time.time()
  info = "Neural time {}; total step: {} \n".format(neural_end_time-neural_start, len(path)-1) 
  print(info)
  strs = ''
  for i, board in enumerate(path):
    strs += "Step {}:\n {}\n".format(i, board.board)
  strs += info
  with open('ans/neu_ans'+epoch+'.txt', 'w') as file:
    file.write(strs)

  # 进行启发函数等于曼哈顿部分
  # path = a_star(game, manhattan_heuristic)
  # m_time = time.time()
  # info = "Manhattan time {}; total step: {} \n".format(m_time - neural_end_time, len(path)-1)
  # print(info)
  # strs = ''
  # for i, board in enumerate(path):
    # strs += "Step {}:\n {}\n".format(i, board.board)
  # strs += info
  # with open('man_ans'+epoch+'.txt', 'w') as file:
    # file.write(strs)

for epoch in range(50):
  while main(epoch) == 'fail':
   continue 