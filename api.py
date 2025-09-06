from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

@app.route('/altin', methods=['GET'])
def altin_fiyat():
    try:
        # Selenium ile Chrome başlat
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Tarayıcıyı açmadan çalıştır
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.haremaltin.com")
        
        # Sayfanın yüklenmesi için bekle
        time.sleep(3)  # gerekirse artır
        
        # Has Altın alış fiyatını al
        has_altin_alis = driver.find_element(By.ID, "alis__ALTIN").text.strip()
        # Has Altın satış fiyatını almak istersen örnek:
        # has_altin_satis = driver.find_element(By.ID, "satis__ALTIN").text.strip()
        
        driver.quit()
        
        result = {
            "has_altin_alis": has_altin_alis
            # "has_altin_satis": has_altin_satis
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
