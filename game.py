

class Game():
    def __init__(self,scorce):
        self.Number_of_Board=0 #局數
        self.frequency=0 #第幾球
        self.sum=0                                                   
        self.rounds=[[0]*10 for i in range(3)]
        self.deposit(scorce)
        self.score()
        print('總分為:'+str(self.sum))
        #self.roll(Int)

        
    def roll(self,Int):                      #存分
        
        self.rounds[self.frequency][self.Number_of_Board] =Int 
        if self.Number_of_Board<9:
            if self.frequency<1:
                self.frequency+=1
            else:
                self.frequency=0
                self.Number_of_Board+=1
        else:
            if self.frequency<2:
                self.frequency+=1
            else:
                self.frequency=0
                self.Number_of_Board=0
                
            
        """if self.Number_of_Board<9:
            
            if self.frequency>1:
                if Int>10:
                    self.frequency+=1
                else:
                    self.Number_of_Board=0
            else:
                self.frequency=0
                self.Number_of_Board+=1

        elif self.Number_of_Board==9:
            if self.frequency>2:
                self.frequency+=1
            else:
                self.frequency=0
                self.Number_of_Board=0"""
        #game.score()
        #print(self.sum)
    def deposit(self,scores):
        for i in range(21):
            
            self.roll(scores[i])


    def score(self):                          #計分
        for i in range(9):
            if self.rounds[0][i]==10:
                Game.strike(self,i)
            elif self.rounds[0][i]+self.rounds[1][i]==10:
                Game.spare(self,i)
            else:
                self.sum=self.sum+self.rounds[0][i]+self.rounds[1][i] 
        for i in range(3):
            self.sum+=self.rounds[i][9]

    def strike(self,i):                       #全倒
        if i<8:
            if self.rounds[0][i+1]==10:
                for j in range(3):
                    self.sum+=self.rounds[0][i+j] 
            else:
                self.sum+=self.rounds[0][i]
                self.sum+=self.rounds[0][i+1]
                self.sum+=self.rounds[1][i+1]
        elif i==9:
            for j in range(3):
                self.sum+=self.rounds[9][j]
        
        else:
            self.sum+=self.rounds[0][i]
            self.sum+=self.rounds[0][i+1]
            self.sum+=self.rounds[1][i+1]
            
    def spare(self,i):                         #半倒
        if i==9:
            for j in range(3):
                self.sum+=self.rounds[9][j]
        else:
            self.sum+=self.rounds[0][i]
            self.sum+=self.rounds[1][i]
            self.sum+=self.rounds[0][i+1]
#scorces=[8,0,0,1,0,1,6,0,0,7,5,1,0,9,0,0,0,4,1,4,0]#47

#scorces=[0,8,9,1,10,0,8,1,6,0,9,0,8,1,4,5,10,0,0,4,1,4,0]#47
scorces=[10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,0,10,10,10]#47

player=Game(scorces)
#round(player,scorce)
print(player.sum)

        
        