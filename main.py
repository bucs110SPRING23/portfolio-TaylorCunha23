import pygame
import pygame_menu

from controller import GameController

pygame.init()
screen = pygame.display.set_mode((800, 800))


class PictionaryGame:
    def __init__(self):

        pygame.display.set_caption("Pictionary Game")

        self.font = pygame.font.Font(None, 30)
        self.game_controller = None

        self.menu = pygame_menu.Menu(
            "Pictionary Game", 800, 800, theme=pygame_menu.themes.THEME_DARK
        )

        self.menu.add.selector(
            "Select Difficulty: ",
            [("Easy", 1), ("Medium", 2), ("Hard", 3)],
            onchange=self.set_difficulty,
        )

        self.menu.add.button("Play", self.start_game)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

    def set_difficulty(self, value):
        GameController.DIFFICULTY = value

    def start_game(self):
        self.game_controller = GameController(self.window, self.font)
        self.game_controller.play_game()

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


self.window.fill((255, 255, 255))
self.menu.update(events)
self.menu.draw(self.window)
pygame.display.flip()
