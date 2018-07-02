class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏启动激活
        self.game_active = False
        # self.high_score = 0
        with open("highscore.txt","r") as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        '''初始化随游戏进行变化的统计信息'''
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open("highscore.txt","r+", encoding="utf-8") as f:
            if self.high_score > int(f.read()):
                f.write(str(self.high_score))
