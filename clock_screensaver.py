#!/usr/bin/env python3
"""
Digital Clock Windows Screen Saver
Dijital Saat Windows Ekran Koruyucusu
"""

import sys
import time
from datetime import datetime
import pygame
import ctypes

class DigitalClockScreenSaver:
    def __init__(self):
        # Ekran boyutunu al
        user32 = ctypes.windll.user32
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)
        
        # Pygame başlat
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Digital Clock Screen Saver")
        
        # Renkler
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 100, 255)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        
        # Font ayarları
        self.clock_font = pygame.font.Font(None, 200)
        self.date_font = pygame.font.Font(None, 80)
        self.info_font = pygame.font.Font(None, 50)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.mouse_position = (0, 0)
        self.initial_mouse_position = None
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                current_pos = pygame.mouse.get_pos()
                if self.initial_mouse_position is None:
                    self.initial_mouse_position = current_pos
                else:
                    # Fare hareket ettiyse çık
                    if (abs(current_pos[0] - self.initial_mouse_position[0]) > 5 or 
                        abs(current_pos[1] - self.initial_mouse_position[1]) > 5):
                        self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.running = False
    
    def get_time_string(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def get_date_string(self):
        now = datetime.now()
        # Türkçe gün adları
        days_tr = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        months_tr = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
                     "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
        
        day_name = days_tr[now.weekday()]
        month_name = months_tr[now.month]
        
        return f"{day_name}, {now.day} {month_name} {now.year}"
    
    def draw(self):
        # Arka plan siyah
        self.screen.fill(self.BLACK)
        
        # Saat göster
        time_str = self.get_time_string()
        time_surface = self.clock_font.render(time_str, True, self.GREEN)
        time_rect = time_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 100))
        self.screen.blit(time_surface, time_rect)
        
        # Tarih göster
        date_str = self.get_date_string()
        date_surface = self.date_font.render(date_str, True, self.BLUE)
        date_rect = date_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))
        self.screen.blit(date_surface, date_rect)
        
        # Alt köşeye bilgi
        info_text = "Screen Saver - Digital Clock (Press any key or move mouse to exit)"
        info_surface = self.info_font.render(info_text, True, self.WHITE)
        info_rect = info_surface.get_rect(bottomright=(self.screen_width - 20, self.screen_height - 20))
        self.screen.blit(info_surface, info_rect)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(30)  # 30 FPS
        
        pygame.quit()
        sys.exit()


def main():
    """
    Ana fonksiyon
    Komut satırı parametreleri:
    /s : Screen saver modu
    /p : Preview modu
    /c : Ayarlar
    """
    
    if len(sys.argv) > 1:
        param = sys.argv[1].lower()
        if param == "/s":
            # Screen saver modu
            screensaver = DigitalClockScreenSaver()
            screensaver.run()
        elif param == "/p":
            # Preview modu
            print("Preview Mode - Digital Clock Screen Saver")
            screensaver = DigitalClockScreenSaver()
            screensaver.run()
        elif param == "/c":
            # Ayarlar (şimdilik boş)
            print("Settings not available yet")
            sys.exit(0)
    else:
        # Normal mod
        screensaver = DigitalClockScreenSaver()
        screensaver.run()


if __name__ == "__main__":
    main()
