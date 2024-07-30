class ticTacToe:

    def __init__(self) -> None:
        self.data = list()
        self.player = [False, False]

    def test(self):
        print(self.data)

    def initiateGame(self):
        self.data = [0 * i - 1 for i in range(9)]
        self.player[0] = True

    def whosPlaying(self):
        if self.player[0] == True:
            return 0
        else:
            return 1

    def printState(self):
        for i in range(9):
            z = self.data[i]
            if z == -1:
                print("_", end="")
            elif z == 0:
                print("*", end="")
            elif z == 1:
                print("0", end="")

            if i % 3 == 2:
                print("")

    def setOpponent(self):
        if self.player[0] == self.player[1]:
            raise ValueError
        self.player[0] = not self.player[0]
        self.player[1] = not self.player[1]

    def getValidPositions(self):
        item = list()
        for i in range(9):
            if self.data[i] != -1:
                continue
            item.append(i)
        return item

    def checkValdity(self, action):
        if action in self.getValidPositions():
            return True
        return False

    def nextState(self, action):
        if action not in range(9):
            raise ValueError
        plr = self.whosPlaying()
        if self.checkValdity(action):
            self.data[action] = plr

    def checkWin(self):
        plr = self.whosPlaying()
        testing = lambda arr, p, i, j, k: arr[i] == p and arr[j] == p and arr[k] == p

        if (
            testing(self.data, plr, 0, 1, 2)
            or testing(self.data, plr, 3, 4, 5)
            or testing(self.data, plr, 6, 7, 8)
            or testing(self.data, plr, 0, 3, 6)
            or testing(self.data, plr, 1, 4, 7)
            or testing(self.data, plr, 2, 5, 8)
            or testing(self.data, plr, 0, 4, 8)
            or testing(self.data, plr, 2, 4, 6)
        ):
            return plr, True
        else:
            pass


newGame = ticTacToe()
newGame.initiateGame()
gameOn = len(newGame.getValidPositions())

while gameOn:
    print(f"You are now player: {newGame.whosPlaying()}")
    newGame.printState()
    print(f"Valid Positions are {newGame.getValidPositions()}")
    action = int(input("Enter a position:"))
    if not newGame.checkValdity(action):
        print("Not a valid move")
        continue
    newGame.nextState(action)
    if newGame.checkWin():
        print(f"Player {newGame.whosPlaying()} is winner")
        gameOn = 0
        continue
    elif len(newGame.getValidPositions()) == 0:
        print("Draw")

    newGame.setOpponent()
    gameOn -= 1
