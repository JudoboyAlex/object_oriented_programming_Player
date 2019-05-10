class Player:

    def __init__(self, gold_coins, health_points, lives):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return "Coins={}, HP = {}, Lives = {}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives += 1    
    
    def collect_treasure(self):
        if self.gold_coins == 0:
            self.gold_coins +=1
        elif self.gold_coins % 10 == 0:
            self.gold_coins += 1
            return self.level_up()
        else:
            self.gold_coins += 1
    
    def do_battle(self, damage):
        self.health_points = self.health_points - damage
        if self.health_points < 1:
            self.lives= self.lives - 1
            self.health_points = 10
        if self.lives == 0:
            return self.restart()

    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

vegeta = Player(0,0,0)
print(vegeta)
print(vegeta.do_battle(3))
print(vegeta)
print(vegeta.do_battle(7))
print(vegeta)
print(vegeta.do_battle(10))
print(vegeta)
print(vegeta.do_battle(10))
print(vegeta)
print(vegeta.do_battle(10))
print(vegeta)
print(vegeta.do_battle(10))
print(vegeta)

