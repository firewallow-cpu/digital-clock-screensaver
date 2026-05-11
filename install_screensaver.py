#!/usr/bin/env python3
"""
Windows Registry Ekran Koruyucusu Kurulum Scripti
Install Screen Saver to Windows Registry
"""

import os
import shutil
import winreg
import sys
from pathlib import Path

def install_screensaver():
    """Screen Saver'ı Windows'a kur"""
    
    # Mevcut dizini al
    current_dir = Path(__file__).parent
    source_scr = current_dir / "digital-clock-screensaver.scr"
    
    # System32 klasörü
    system32_path = Path(os.environ['WINDIR']) / "System32"
    dest_scr = system32_path / "digital-clock-screensaver.scr"
    
    try:
        # .scr dosyasını System32'ye kopyala
        if source_scr.exists():
            print(f"Copying {source_scr} to {dest_scr}")
            shutil.copy2(source_scr, dest_scr)
            print("✓ Screen Saver copied successfully")
        else:
            print(f"Error: {source_scr} not found!")
            print("First run: build_screensaver.bat")
            return False
        
        # Registry'ye ekle
        try:
            reg_path = r"Control Panel\Desktop"
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, "SCRNSAVE.EXE", 0, winreg.REG_SZ, str(dest_scr))
            winreg.CloseKey(registry_key)
            print("✓ Registry updated successfully")
        except Exception as e:
            print(f"Warning: Registry update failed: {e}")
        
        print("\n✓ Screen Saver installed successfully!")
        print("Go to: Settings > Personalization > Lock screen > Screen saver settings")
        print("Select: digital-clock-screensaver")
        
        return True
        
    except Exception as e:
        print(f"Error during installation: {e}")
        return False

if __name__ == "__main__":
    if os.name == 'nt':  # Windows
        install_screensaver()
    else:
        print("Bu script sadece Windows'ta çalışır")
        sys.exit(1)
