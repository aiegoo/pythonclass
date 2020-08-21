import random 

class Game:
    comList=list() #컴퓨터가 냈던 가위바위보
    personList=list() #사람이 
    winnerList=list() #승부 저장
    sWinner=["", "컴퓨터승", "사람승", "무승부"]
    sSel=["", "가위", "바위", "보"]

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
        for i in range(0, len(self.comList)):
            c = self.comList[i]
            p = self.personList[i]
            n = self.winnerList[i]   
            cnt[n]= cnt[n]+1  # 각 우승자 숫자 세기   
            print("컴퓨터:" , self.sSel[c], "사람:", self.sSel[p], self.sWinner[n])

        total = cnt[1]+cnt[2]+cnt[3]
        print("전체게임수 : ", total)
        print("컴퓨터 승률 : ", cnt[1]/total)
        print("사람   승률 : ", cnt[2]/total)
        print("무승부 승률 : ", cnt[3]/total)
        
    def gameStart(self):
        #1.컴퓨터가 1~3 중 하나를 생각한다 
        computer = random.randint(1,3)
        #print(computer)
        person =self.myInput()
        n = self.isWinner(computer, person)
        print("컴퓨터:" , self.sSel[computer], "사람:", self.sSel[person], self.sWinner[n])
        self.comList.append(computer)
        self.personList.append(person)
        self.winnerList.append(n)
        

    #가위 1  바위  2   보  3    2는 1을 이기고, 3은 2를 이기고 1은 3을 이긴다 
    def isWinner(self, computer, person):
        #둘이 무승부인 경우는 빼고 나머지만 판단한다 
        if computer == person:
             return 3 #무승부 
  
        #사람이 이긴경우 
        if (person==1 and computer==3) or (person==2 and computer==1) or (person==3 and computer==2):
            return 2 #사람승

        #컴퓨터가 이긴 경우
        if (computer==1 and person==3) or (computer==2 and person==1) or (computer==3 and person==2):
            return 1 #컴퓨터승
        

if __name__ == "__main__":
    game = Game()
    game.start()