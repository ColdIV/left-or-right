# Based on Harkness Rating System
class Rank:
    def __init__(self, id, points = 1200):
        self.id = id
        self.points = points
        self.pointTable = {}
        
        high = 16
        low = 16
        draw = 0
        for i in range(0, 13):
            self.pointTable[i] = {}
            self.pointTable[i][0] = high
            self.pointTable[i][1] = low
            self.pointTable[i][2] = draw
            high -= 1
            low += 1
            draw += 1
    
    # state
    # 1 = win; 0 = lose; 2 = draw
    def vs(self, rank, state, call = True):
        diff = abs(rank.points - self.points)
        
        if call:
            rankState = 0 if state == 1 else 1 if state == 0 else 2
            rank.vs(self, rankState, False)
        
        pointIndex = 0
        if diff > 24 and diff <= 49:
            pointIndex = 1
        elif diff >= 50 and diff <= 74:
            pointIndex = 2
        elif diff >= 75 and diff <= 99:
            pointIndex = 3
        elif diff >= 100 and diff <= 124:
            pointIndex = 4
        elif diff >= 125 and diff <= 149:
            pointIndex = 5
        elif diff >= 150 and diff <= 174:
            pointIndex = 6
        elif diff >= 175 and diff <= 199:
            pointIndex = 7
        elif diff >= 200 and diff <= 224:
            pointIndex = 8
        elif diff >= 225 and diff <= 249:
            pointIndex = 9
        elif diff >= 250 and diff <= 274:
            pointIndex = 10
        elif diff >= 275 and diff <= 299:
            pointIndex = 11
        elif diff >= 300:
            pointIndex = 12
        
        if state == 1:
            self.points += self.pointTable[pointIndex][state]
        elif state == 0:
            self.points -= self.pointTable[pointIndex][state]
        else:
            if self.points > rank.points:
                self.points -= self.pointTable[pointIndex][state]
            elif self.points < rank.points:
                self.points += self.pointTable[pointIndex][state]
                
        return self.points
