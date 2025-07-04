from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import logging
from datetime import datetime
import os
import time
import xml.etree.ElementTree as ET

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
if not os.path.exists("reports"):
    os.makedirs("reports")

log_filename = "reports/orangehrm_login.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

html_report = ["<html><head><title>OrangeHRM Login Report</title></head><body><h2>OrangeHRM Login Test</h2><table border='1'>"]
html_report.append("<tr><th>Step</th><th>Status</th><th>Details</th></tr>")

wb = Workbook()
ws = wb.active
ws.title = "Test Logs"
ws.append(["Timestamp", "Step", "Status", "Details"])

xml_root = ET.Element("TestReport")

def log_step(step, status, details):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{step} - {status} - {details}")
    html_report.append(f"<tr><td>{step}</td><td>{status}</td><td>{details}</td></tr>")
    ws.append([timestamp, step, status, details])
    xml_step = ET.SubElement(xml_root, "Step")
    ET.SubElement(xml_step, "Timestamp").text = timestamp
    ET.SubElement(xml_step, "Name").text = step
    ET.SubElement(xml_step, "Status").text = status
    ET.SubElement(xml_step, "Details").text = details

try:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")

    driver = webdriver.Chrome(options=options)
    log_step("Open Browser", "PASS", "Chrome browser launched")

    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    log_step("Navigate to URL", "PASS", f"Navigated to {url}")

    expected_title = "OrangeHRM"
    assert expected_title in driver.title
    log_step("Check Title", "PASS", f"Page title verified: {driver.title}")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    log_step("Submit Login", "PASS", "Submitted valid credentials")

    dashboard_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Dashboard')]"))
    )
    assert "Dashboard" in dashboard_header.text
    log_step("Login Success", "PASS", f"Dashboard loaded: {dashboard_header.text}")

    screenshot_path = f"screenshots/orangehrm_success_login_{int(time.time())}.png"
    driver.save_screenshot(screenshot_path)
    log_step("Screenshot Saved", "PASS", f"Screenshot saved: {screenshot_path}")

except AssertionError as ae:
    screenshot_path = f"screenshots/orangehrm_assertion_error_{int(time.time())}.png"
    driver.save_screenshot(screenshot_path)
    log_step("Assertion Error", "FAIL", f"{ae}. Screenshot: {screenshot_path}")

except Exception as e:
    screenshot_path = f"screenshots/orangehrm_unexpected_error_{int(time.time())}.png"
    driver.save_screenshot(screenshot_path)
    log_step("Exception", "FAIL", f"{e}. Screenshot: {screenshot_path}")

finally:
    driver.quit()
    log_step("Close Browser", "PASS", "Browser closed")

    html_report.append("</table></body></html>")
    html_path = os.path.abspath("reports/orangehrm_login_report.html")
    with open(html_path, "w") as f:
        f.writelines(html_report)
    log_step("HTML Report", "PASS", f"Saved as {html_path}")

    excel_path = os.path.abspath("reports/orangehrm_login_log.xlsx")
    wb.save(excel_path)
    log_step("Excel Report", "PASS", f"Saved as {excel_path}")

    xml_path = os.path.abspath("reports/orangehrm_login_report.xml")
    xml_tree = ET.ElementTree(xml_root)
    xml_tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    log_step("XML Report", "PASS", f"Saved as {xml_path}")
