import random 

class GameData:
 
    def __init__(self, person=1):
        self.computer=random.randint(1,3)
       
    def setPerson(self, person=1):
        self.person=person
        self.winner=self.isWinner()

    def isWinner(self):
        #둘이 무승부인 경우는 빼고 나머지만 판단한다 
        if self.computer == self.person:
             return 3 #무승부 
  
        #사람이 이긴경우 
        if (self.person==1 and self.computer==3) or (self.person==2 and self.computer==1) \
            or (self.person==3 and self.computer==2):
            return 2 #사람승

        #컴퓨터가 이긴 경우
        if (self.computer==1 and self.person==3) or (self.computer==2 and self.person==1) \
            or (self.computer==3 and self.person==2):
            return 1 #컴퓨터승

class Game:

    sWinner=["", "컴퓨터승", "사람승", "무승부"]
    sSel=["", "가위", "바위", "보"]


    def __init__(self):
        self.gameList = list() 

    def myInput(value):
        #입력된 1~3의 범위를 벗어날 경우를 체크한다 
        value = input("1.가위 2.바위 3.보 ")
        while value!="1" and value!="2" and value !="3":
            value = input("1.가위 2.바위 3.보 ")
        return int(value)

    def start(self):
        while(True):
            print("1.게임시작")
            print("2.게임통계")
            print("3.종료    ")
            sel= input("선택 : ")
            if sel =="1":
                self.gameStart()
            elif sel=="2":
                self.statistics()
            else:
                return
    def statistics(self):
        cnt=[0, 0, 0, 0] 
        for item in self.gameList:
            c = item.computer
            p = item.person
            n = item.winner 
            cnt[n]= cnt[n]+1  # 각 우승자 숫자 세기   
            print("컴퓨터:" , self.sSel[c], "사람:", self.sSel[p], self.sWinner[n])

        total = cnt[1]+cnt[2]+cnt[3]
        print("전체게임수 : ", total)
        print("컴퓨터 승률 : ", cnt[1]/total)
        print("사람   승률 : ", cnt[2]/total)
        print("무승부 승률 : ", cnt[3]/total)
        
    def gameStart(self):
        #1.컴퓨터가 1~3 중 하나를 생각한다 
    
        data = GameData()
        data.setPerson(self.myInput())

       
        print("컴퓨터:" , self.sSel[data.computer], "사람:", self.sSel[data.person], self.sWinner[data.winner])
        self.gameList.append(data)
        

    #가위 1  바위  2   보  3    2는 1을 이기고, 3은 2를 이기고 1은 3을 이긴다 
    
if __name__ == "__main__":
    game = Game()
    game.start()