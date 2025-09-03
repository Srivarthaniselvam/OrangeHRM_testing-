## OrangeHRM Login Automation Test 

This project automates the login functionality of the **[OrangeHRM Open Source Demo Site](https://opensource-demo.orangehrmlive.com/)** using Selenium WebDriver in Python. The script performs a full test cycle including logging, reporting, and screenshot capture.
##  Project Description

- Automates login process using valid credentials.
- Verifies page title and successful login using the dashboard check.
- Captures screenshot after successful login or on failure.
- Logs detailed results in:
  -  HTML report
  -  Excel file
  -  XML file
  - `.log` text log file

## Project Summary
Automates OrangeHRM login using Selenium in Python.

Validates title, credentials, and dashboard access.

Generates reports: HTML, Excel, XML, and logs.

Captures screenshots for both success and failure.

 ## Test Plan Points
Objective: Test valid login functionality.

Inputs: Username = Admin, Password = admin123.

Expected Output: Dashboard should load after login.

Test Environment: Python 3, Selenium, Chrome.

Reports Generated:

HTML

Excel

XML

Log file

Screenshots

Exit Criteria: Dashboard header must be visible.

## Testing Types Used
 - Type	Purpose / Where Used
 - Functional Testing	Check login process with valid data
 - UI Testing	Ensure fields and buttons are interactable
 - Assertion Testing	Validate title and dashboard text
 - Regression Testing	Can be reused after updates
 - Error Handling Test	Handles exceptions and captures screenshots

## Why Components Are Used
Selenium: Automates browser tasks.

WebDriverWait: Ensures elements are loaded.

logging: Logs steps in .log file.

openpyxl: Creates Excel report.

ElementTree: Creates structured XML report.

Screenshots: Provide evidence of test results.

HTML Report: Human-readable test summary.

## Use Cases
QA/Testing portfolios.

Interview/Internship projects.

Real-world functional testing practice.

CI/CD pipelines (Jenkins, GitHub Actions).

Bug tracking and reporting in teams.
