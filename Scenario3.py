
"""
Scenario 3: Create a Project with No Postgres Version Selected
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Enter a valid project name.
2.	Do not select any Postgres version.
3.	Choose a region.
4.	Click the "Create Project" button.
•	Expected Result: Project will be created with default version

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
region = "US EAST (Ohio)"

name_input = driver.find_element(By.NAME, "project.name")
name_input.send_keys(project_name)


region_select = Select(driver.find_element(By.XPATH, '//label[@for="project.region_id"]'))
region_select.select_by_visible_text(region)

# Click the "Create Project" button
create_button = driver.find_element(By.XPATH, '//button[@data-qa = "project_create_button_form_submit"]')
create_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()="frosty-sound-54330722"]")))

assert driver.find_element(By.XPATH, '//div[contains(text(), "Connection Details")]'))

# Close the browser
driver.quit()
