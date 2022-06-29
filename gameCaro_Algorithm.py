
import copy

MIN, MAX = -1000, 1000
values = [2, 0, 0, 5, 6, 7, 8, 9, 10, 11] 

class Operator:
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
    def __init__(self, data= None, size = None):
        
        self.data = data
        self.N = size

    def clone (self):
        sn = copy.deepcopy(self)
        return sn

def IsNodeEnd(s):
    sz = s.N
    data = s.data
    if sz == 3:
        flag_win = 3
    elif sz == 10:
        flag_win = 5
    for i in range (sz):
        for j in range (sz):
            count = 1
            temp_j = j
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1 and j + flag_win - 1 < sz:
                    temp_j += 1
                    if data[i][j] == data[i][temp_j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_i = i
            if data[i][j] != 0:
                while temp_i < i + flag_win - 1  and i + flag_win - 1  < sz:
                    temp_i += 1
                    if data[i][j] == data[temp_i][j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i < i + flag_win - 1 and i + flag_win - 1  < sz:
                    temp_j += 1
                    temp_i += 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i >= 1:
                    temp_j += 1
                    temp_i -= 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win: return True

    for i in range(sz):
        for value in data[i]:
            if value == 0:
                return False
    return True
    
def Win (s):
    if s.data == None:
        return False
    sz = s.N
    data = s.data

    if sz == 3:
        flag_win = 3
    elif sz == 10:
        flag_win = 5

    for i in range (sz):
        for j in range (sz):
            count = 1
            temp_j = j
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1 and j + flag_win - 1 < sz:
                    temp_j += 1
                    if data[i][j] == data[i][temp_j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_i = i
            if data[i][j] != 0:
                while temp_i < i + flag_win - 1  and i + flag_win - 1  < sz:
                    temp_i += 1
                    if data[i][j] == data[temp_i][j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i < i + flag_win - 1 and i + flag_win - 1  < sz:
                    temp_j += 1
                    temp_i += 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win: return True

            count = 1
            temp_j = j
            temp_i = i
            if data[i][j] != 0:
                while temp_j < j + flag_win - 1  and j + flag_win - 1  < sz and temp_i >= 1:
                    temp_j += 1
                    temp_i -= 1
                    if data[i][j] == data[temp_i][temp_j]:
                        count += 1
                if count == flag_win: return True
    return False

def CheckMyTurn (s):
    res = 0
    for i in s.data:
        for value in i:
            if value == 0:
                res+= 1

    if res %2 == 0:
        return True
    return False

def Values (s, nodeIndex):
    if Win(s):
        if CheckMyTurn(s):
            return 16
        return -1
    return values[nodeIndex]

def AlphaBeta (s, d, nodeIndex, a, b, mp):
    if IsNodeEnd(s) or d == 0:
        return Values(s, nodeIndex)
    sz = s.N
    if mp == True:
        best = MIN
        for i in range(sz):
            for j in range(sz):
                child = Operator(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d-1, i, a, b, False)
                best = max(best, tmp)
                a = max(a, best)
                if a>= b: break
        return best
    else:
        best = MAX
        for i in range(sz):
            for j in range(sz):
                child = Operator(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d-1, i, a, b, True)
                best = min(best, tmp)
                b = min(b, best)
                if a>= b: break
        return best

def Minimax (s, d, nodeIndex, mp):
    return AlphaBeta(s, d, nodeIndex, -1000, 1000, mp)

def Run (size, data):

    s = State(data, size= size)
    # AI
    mn = 20
    minchild = None
    sz = s.N
    for i in range(sz):
        for j in range(sz):
            child = Operator(i, j).Move(s)
            if child == None:
                continue
            tmp = Minimax(child, 1, 0, True)
            if mn > tmp:
                mn = tmp
                minchild = child
    s = minchild

    if Win(s):
        # s.Print()
        print('AI win')
        # break
# s.Print()
    if IsNodeEnd(s):
        print ('draw')
        # break
    return s.data
# turn += 1
# if __name__ == '__main__':
#     size = 3
#     data = [[0 for i in range(size)] for i in range(size)]
#     Run(size, data)