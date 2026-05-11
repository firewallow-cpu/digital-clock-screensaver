@echo off
REM Bu script Python dosyasını .scr dosyasına dönüştürür
REM Gerekli: Python ve PyInstaller kurulu olmalı

REM PyInstaller yüklü değilse yükle
pip install pyinstaller pygame

REM .scr dosyasını oluştur
pyinstaller --onefile --windowed --icon=clock.ico clock_screensaver.py -o dist

REM Çıktıyı .scr uzantısına dönüştür
cd dist
ren clock_screensaver.exe digital-clock-screensaver.scr

echo Screen Saver oluşturuldu: digital-clock-screensaver.scr
echo Windows\System32 klasörüne kopyalayın ve sağ tıklayıp "Install" seçin
pause
