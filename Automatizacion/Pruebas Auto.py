from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost/libreria/Libreria/")
time.sleep(1)
driver.save_screenshot("Results/Historia_1.png")

libros_link = driver.find_element(By.LINK_TEXT, "Libros")
libros_link.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_2.png")

autores_link = driver.find_element(By.LINK_TEXT, "Autores")
autores_link.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_3.png")

about_link = driver.find_element(By.LINK_TEXT, "ABOUT")
about_link.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_4.png")


driver.back
time.sleep(5)
driver.save_screenshot("Results/Historia_5.png")

contacto_link = driver.find_element(By.LINK_TEXT, "Contacto")
contacto_link.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_6.png")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "Form[action='Enviar.php']")))
driver.find_element(By.CSS_SELECTOR, "input[name='asunto']").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[name='asunto']").send_keys("1/1/2024")
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("Ejemplo123@example.com")
driver.find_element(By.CSS_SELECTOR, "input[name='asunto']").send_keys("Jane Doe")
driver.find_element(By.CSS_SELECTOR, "input[name='asunto']").send_keys("Consulta sobre un libro")
driver.find_element(By.CSS_SELECTOR, "textarea[name='comentario']").send_keys("Mensaje de Prueba")
time.sleep(5)
driver.save_screenshot("Results/Historia_7.png")



facebook_button = driver.find_element(By.XPATH, "//button[id='facebook']")
facebook_button.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_9.png")

twitter_button = driver.find_element(By.XPATH, "//button[id='twitter']")
twitter_button.click()
time.sleep(5)
driver.save_screenshot("Results/Historia_10.png")

driver.quit()










