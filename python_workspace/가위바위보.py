#1.가위 2.바위 3.보 
"""
1. 컴퓨터가 먼저 생각을 한다. 
   랜덤값 하나 추출해서 갖고 있자 
2. 사람 
    1.가위 2.바위 3.보
    1
    컴퓨터 : 바위   사람:가위   컴퓨터승 
"""
import random
class KawibawiboGame:
    comList=[]
    perList=[]
    resultList=[]

    def game(self):
        com = random.randint(1,3)
        person = input("1.가위 2.바위 3.보 ") 
        result = self.isWinner(com, person) 

        self.comList.append(com)
        self.perList.append(person)
        self.resultList.append(result)

    def isWinner(self, com, person):
        winner=1 
        person = int(person)
        if com==1:
            if person==1:
                winner = 0 #무승부
            elif person==2:
                winner = 2 #사람이 
            else:
                winner = 1 #컴퓨터 
        if com==2:
            if person==1:
                winner = 1
            elif person==2:
                winner = 0 #사람이 
            else:
                winner = 2 #컴퓨터 
        if com==3:
            if person==1:
                winner = 2 #무승부
            elif person==2:
                winner = 1 #사람이 
            else:
                winner = 0 #컴퓨터 
        return winner 

    def output(self):
        sResult=["", "가위", "바위", "보"]
        sResult2 = ["무승부", "컴퓨터승", "사람승"]
        #컴퓨터:가위 사람:바위 사람승 
        for i in range(0, len(self.comList)):
            print( sResult[self.comList[i]], 
               sResult[ int( self.perList[i])],
               sResult2[self.resultList[i]])

    def start(self):
        self.game()
        self.output()

game = KawibawiboGame()
game.start()
 
"""
 I like start
 a  - 1
 b  - 0 
 c  - 0 
 ...
 i  - 1
 count=[0,0,0,0,0,0,0,0,...]
 'a'a -> count[0]
 ord('c') - ord('a') ->2
"""
