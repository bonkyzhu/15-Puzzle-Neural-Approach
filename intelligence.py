import numpy as np
from board import Board
from utils import Node, PriorityQueue
import time

def a_star(board, heuristic):
    """
    A*算法主题

    :param board: 要解决的游戏
    :param heuristic: 选择的启发函数
    :return: 返回的解的路径
    """

    frontier = PriorityQueue()
    node = Node(board)
    frontier.add(node, heuristic(node.data) + len(node.path()) - 1)

    explored = []

    while frontier.has_next():
        node = frontier.pop()

        if node.data.is_solved():
            return node.path()

        for move in node.data.legal_moves():
            child = Node(node.data.forecast(move), node)
            if (not frontier.has(child)) and (child.data not in explored):
                frontier.add(child, heuristic(child.data) + len(child.path()) - 1)
            elif frontier.has(child):
                child_value = heuristic(child.data) + len(child.path()) - 1
                if child_value < frontier.get_value(child):
                    frontier.remove(child)
                    frontier.add(child, child_value)

        explored.append(node.data)

    return None


def manhattan_heuristic(board):
    state = board.get_board()
    indices = np.array([np.argwhere(state == i)[0] for i in range(1,16)])
    correct_indices = np.array([[i, j] for i in range(4) for j in range(4)])[:-1]

    return np.abs(indices - correct_indices).sum()

def Judge_Whether_Have_A_Solution(game, goal):
  '''
  通过判断奇偶性
  '''
  # 存储奇偶性的值
  game_parity = 0
  goal_parity = 0

  for i in range(16):
    if game[i] != 0: 
      game_parity += len([j for j in range(i) if game[i]>game[j] and game[j]!=0])
    if goal[i] != 0:
      goal_parity += len([j for j in range(i) if goal[i]>goal[j] and goal[j]!=0])
    
  game_parity += np.argwhere(game == 0)[0]
  # game_parity += game.index(0)
  goal_parity += goal.index(0)

  if game_parity % 2 == goal_parity % 2:
    return True
  else:
    return False

