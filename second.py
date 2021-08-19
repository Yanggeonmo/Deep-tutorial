class BasketballPlayers:
    def __init__(self, player): #변수
        self.player = player

    def shoot(self):
        print(self.player + 'shoot')

    def goal(self):
        print(self.player + 'goal')

a_basketball_player = BasketballPlayers('curry')

a_basketball_player.shoot()