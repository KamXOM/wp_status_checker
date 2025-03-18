from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# WhatsApp Web'e bağlanmak için Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# QR kodunu okutman için bekleyelim
input("Devam etmek için QR kodunu okut ve Enter'a bas...")

# Takip edilecek kişi (Buraya istediğin ismi yaz)
TARGET_NAME = "Annemmm"

def find_chat(name):
    """Belirli bir kişiyle olan sohbeti aç"""
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    search_box.clear()
    search_box.send_keys(name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

def check_typing_status():
    """'Yazıyor...' durumunu kontrol et"""
    try:
        status_element = driver.find_element(By.XPATH, "//span[contains(text(), 'yazıyor')]")
        return True  # Eğer element varsa yazıyor demektir
    except:
        return False  # Bulamazsa yazmıyordur

def log_typing_event(name):
    """Yazıyor olduğu anı log doyasına yaz"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {name} yazıyor...\n"
    with open("typing_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

# Sohbeti aç
find_chat(TARGET_NAME)

print(f"{TARGET_NAME} için yazıyor kontrolü başlatıldı...")
while True:
    if check_typing_status():
        print(f"⚡ {TARGET_NAME} yazıyor!")
        log_typing_event(TARGET_NAME)
    time.sleep(2)  # Çok sık kontrol etmesin, sistemi yormasın