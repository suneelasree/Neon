
"""
Scenario 1: Create a Project with Valid Information
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Enter a valid project name in the "Name" field.
2.	Select a Postgres version from the available options.
3.	Choose a region from the available options.
4.	Click the "Create Project" button.
•	Expected Result: The project is created successfully, and the user is redirected to the project dashboard.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Start a new instance of the Firefox browser (you can use other browsers as well)
driver = webdriver.Firefox()

# Navigate to the project creation form
driver.get("https://console.neon.tech/app/welcome")

driver.find_element(By.XPATH, "//button[@data-qa="project_create_button"]").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//form[@class="ProjectsNew Form"]')))


# Fill in the project details
project_name = "My New Project"
postgres_version = "15"
region = "US EAST (Ohio)"

name_input = driver.find_element(By.NAME, "project.name")
name_input.send_keys(project_name)

postgres_select = Select(driver.find_element(By.XPATH, '//label[@for="project.pg_version"]'))
postgres_select.select_by_visible_text(postgres_version)

region_select = Select(driver.find_element(By.XPATH, '//label[@for="project.region_id"]'))
region_select.select_by_visible_text(region)

# Click the "Create Project" button
create_button = driver.find_element(By.XPATH, '//button[@data-qa = "project_create_button_form_submit"]')
create_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()="frosty-sound-54330722"]")))

assert driver.find_element(By.XPATH, '//div[contains(text(), "Connection Details")]'))

# Close the browser
driver.quit()
