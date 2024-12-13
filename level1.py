from pipe import start_pipe, end_pipe, pipes
from wall import Wall, walls

from game_play import GamePlay

class Level1(GamePlay):
    def __init__(self):
        super().__init__()
        
    def initialize(self):
        start_pipe.change_position((6, 6))
        end_pipe.change_position((11,11))

        Wall((8, 6))
        Wall((8, 7))
        Wall((8, 8))
        Wall((8, 9))
        Wall((8, 10))
        Wall((9, 10))

    def update(self):
        for pipe in pipes.values():
            if pipe.update():
                self.cleanup()
                return "game play"
        pass