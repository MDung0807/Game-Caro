
import copy
import math
from tkinter import Y

class Operator:
    """Move"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def Move (self, s):
        sz = s.N
        x = self.x
        y = self.y

        if x < 0 or x >= sz:
            return None
        if y < 0 or y >= sz:
            return None

        if s.data[x][y] != 0:
            return None

        res = 0
        for i in range(sz):
            for value in s.data[i]:
                if value != 0:
                    res += 1

        sn = s.clone()
        if res % 2 ==0:
            sn.data[x][y] = 1
        elif res % 2 != 0:
            sn.data[x][y] = 2   
        return sn 

class State:
    """initialize state"""
    def __init__(self, data= None, size = None):
        
        self.data = data
        self.N = size

    def clone (self):
        sn = copy.deepcopy(self)
        return sn

def IsNodeEnd(data, size):
    """Check matrix is full
        check win"""
    sz = size
    
    if Win(data, size, 0, 0)[0]:
        return True

    for i in range(sz):
        for value in data[i]:
            if value == 0:
                return False
    return True

def Step (data, sz, flag_win, x, score, change_i, change_j, option=False): # check row, and check col and cal score
    ''' 1 1 1
        0 0 0
        0 0 0
        
        1 1 1
        0 0 0
        0 0 0
        
        1 0 0
        1 0 0
        1 0 0 AND MORE'''

    """check and win. if win with fag_win return True and Score. Score = distance + value parameter
        if not win return False

        PARAMETER: data is matrix
                    sz is size
                    flag_win is quantity to be achieved
                    x is player or AI (player is 1, AI is 2)
                    score  is risk (The lower the score, the higher the risk)
                    chang_i, chang_j: location has just changed
                    option: risk check (if option == True then rick check, if option == False check win)"""
    for i in range (sz):
        for j in range (sz):
            count = 1
            temp_j = j
            if data[i][j] == x:
                while temp_j < j + flag_win - 1 and j + flag_win - 1 < sz:
                    temp_j += 1
                    if data[i][j] == data[i][temp_j]:
                        count += 1
                if count == flag_win:
                    if option: # check if the other end is blocked. if is blocked continue
                        if j> 0 and j + flag_win - 1 < sz - 1:
                            if data[i][j - 1 ]!= 0 and data[i][j - 1 ]!= x and data[i][temp_j + 1] != x and data[i][temp_j +1] != 0:
                                continue
                    return True, int((math.sqrt((i_new - change_i)**2 + (j_new - change_j)**2) + 1) + score)

            count = 1
            temp_i = i
            if data[i][j] == x:
                while temp_i < i + flag_win - 1  and i + flag_win - 1  < sz:
                    temp_i += 1
                    if data[i][j] == data[temp_i][j]:
                        count += 1
                if count == flag_win:
                    if option: # check if the other end is blocked. if is blocked continue
                        if i> 0 and j + flag_win - 1 < sz - 1:
                            if data[i - 1][j ]!= 0 and data[i - 1][j]!= x and data[temp_i + 1][j ]!= 0 and data[temp_i + 1][j]!= x:
                                continue
                    return True, int((math.sqrt((i_new - change_i)**2 + (j_new - change_j)**2) + 1) + score)

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] == x:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i < i + flag_win - 1 and i + flag_win - 1  < sz:
                    temp_j += 1
                    temp_i += 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win:
                    if option: # check if the other end is blocked. if is blocked continue
                        if i> 0 and j > 0 and j + flag_win - 1 < sz - 1 and i + flag_win - 1 < sz - 1:
                            if data[i - 1][j  - 1]!= 0 and data[i - 1][j - 1]!= x and data[temp_i + 1][temp_j + 1]!= 0 and data[temp_i + 1][temp_j + 1]!= x:
                                continue
                    return True, int((math.sqrt((i_new - change_i)**2 + (j_new - change_j)**2) + 1) + score)

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] == x:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i >= 1:
                    temp_j += 1
                    temp_i -= 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win:
                    if option: # check if the other end is blocked. if is blocked continue
                        if i< sz - 1 and j > 0 and temp_j < sz - 1 and temp_i > 0:
                            if data[i + 1][j  -1]!= 0 and data[i + 1][j - 1]!= x and data[temp_i - 1][temp_j + 1]!= 0 and data[temp_i - 1][temp_j + 1]!= x:
                                continue
                    return True, int((math.sqrt((i_new - change_i)**2 + (j_new - change_j)**2) + 1) + score)
    return False, None

def Win (data, size, x, y):
    """if already win returns true"""
    if data == None:
        return False, None
    sz = size

    if sz == 3:
        flag_win = 3
    elif sz != 3:
        flag_win = 5
    
    # Defense
    defense, value = Step(data, sz, flag_win, 1, -1500, x, y)
    """"""
    if defense:
        return defense, value
    # Attack
    attack, value = Step(data, sz, flag_win, 2, -50, x, y)
    if attack:
        return attack, value
    
    return False, None

def Score (s, x, y):
    """Tính điểm"""
    sz = s.N
    flag_win = 4
    data = s.data
    # Defense
    defense, value = Step(data, sz, flag_win, 1, -1000, x, y, True)
    if defense:
        return defense, value
    # Attack
    attack, value = Step(data, sz, flag_win, 2, -400, x, y)
    if attack:
        return attack, value
    
    return False, None

def ran(s, x, y):
    """no risk"""
    return int((math.sqrt((i_new - x)**2 + (j_new - y)**2) + 1) * -100)

def Values (s, i, j):
    flag_win, value_win = Win(s.data, s.N, i, j)
    if flag_win:
        return value_win

    flag_score, value_score = Score(s, i, j)
    if flag_score:
        return value_score
    else:
        return ran(s, i, j)

def AlphaBeta (s, d, a, b, mp, x, y):
    if IsNodeEnd(s.data, s.N) or d == 0:
        return Values(s, x, y)
    sz = s.N
    if mp == True:
        for i in range(sz):
            for j in range(sz):
                child = Operator(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d-1, a, b, False, i, j)
                a = max(a, tmp)
                if b <= a: break
        return a
    else:
        for i in range(sz):
            for j in range(sz):
                child = Operator(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d-1, a, b, True, i, j)
                b = min(b, tmp)
                if  b <= a: break
        return b

def Minimax (s, d, mp):
    """Algorithm AlphaBeta"""
    return AlphaBeta(s, d, -1000, 1000, mp, 0, 0)

def Run (size, data, x, y):

    global i_new, j_new
    i_new = x
    j_new = y

    s = State(data, size= size)
    # AI
    mn = -100000
    minchild = None
    sz = s.N
    
    """choose the best move"""
    for i in range(sz):
        for j in range(sz):
            child = Operator(i, j).Move(s)
            if child == None:
                continue
            tmp = Minimax(child, 1, False)
            if mn < tmp:
                mn = tmp
                minchild = child
    s = minchild

    return s.data
