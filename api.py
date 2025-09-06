from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

# Ana sayfa route
@app.route('/', methods=['GET'])
def home():
    return "API çalışıyor. Has Altın fiyatı için /altin endpoint'ini kullanın."

# Has Altın fiyat endpoint
@app.route('/altin', methods=['GET'])
def altin_fiyat():
    try:
        # Headless Chrome ayarları (Render gibi Linux ortamları için)
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

        # Harem Altın ana sayfasına git
        driver.get("https://www.haremaltin.com")
        time.sleep(3)  # Sayfanın yüklenmesini bekle

        # Has Altın fiyatını çek
        has_altin = driver.find_element("id", "alis__ALTIN").text
        driver.quit()

        return jsonify({"has_altin_alis": has_altin})

    except Exception as e:
        return jsonify({"error": str(e)})

# Flask uygulamasını Render için çalıştır
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
