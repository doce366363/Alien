import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """класс для управления русурсами и поведением игры."""

    def __init__(self):
        """Иннициалезирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            self._update_screen()
            self.ship.update()
            self._check_events()

    def _update_screen(self):
        """обновляет изоброжение на экране и отоброжает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """обрабатывает нажатия клавиш"""
        for event in pygame.event.get():
            if event.type == 'QUIT':
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагирует на нажате клавишь"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """реагирует на отжатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    """создание экземпляра и запуск игры"""
    ai = AlienInvasion()
    ai.run_game()