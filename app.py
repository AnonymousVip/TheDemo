from selenium import webdriver
from flask import Flask,jsonify
from flask import request
app = Flask(__name__)
@app.route("/")
def home():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

	#driver.implicitly_wait(2)
	driver.get("https://www.swagbucks.com/?gw=1")
	js = 'return document.getElementById("ioBlackBox").value'
	value = driver.execute_script(js)
	driver.quit();
	json = {
	"success": True,
	"token":value
	}
	return jsonify(json);
	
if __name__ == "__main__":
    app.run(debug=True)
