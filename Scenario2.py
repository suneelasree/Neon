
"""
Scenario 2: Create a Project with Missing Name

Preconditions: User is on the project creation form.
Steps:
Leave the "Name" field empty.
Select a Postgres version.
Choose a region.
Click the "Create Project" button.
Expected Result: System will asign automatic name 

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

postgres_version = "15"
region = "US EAST (Ohio)"


postgres_select = Select(driver.find_element(By.XPATH, '//label[@for="project.pg_version"]'))
postgres_select.select_by_visible_text(postgres_version)

region_select = Select(driver.find_element(By.XPATH, '//label[@for="project.region_id"]'))
region_select.select_by_visible_text(region)

# Click the "Create Project" button
create_button = driver.find_element(By.XPATH, '//button[@data-qa = "project_create_button_form_submit"]')
create_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()="Home"]")))

assert driver.find_element(By.XPATH, '//div[contains(text(), "Connection Details")]'))

# Close the browser
driver.quit()
