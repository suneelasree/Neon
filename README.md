# Neon
Automation Assignment

Scenario 1: Create a Project with Valid Information
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Enter a valid project name in the "Name" field.
2.	Select a Postgres version from the available options.
3.	Choose a region from the available options.
4.	Click the "Create Project" button.
•	Expected Result: The project is created successfully, and the user is redirected to the project dashboard.

Scenario 2: Create a Project with Missing Name
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Leave the "Name" field empty.
2.	Select a Postgres version.
3.	Choose a region.
4.	Click the "Create Project" button.
•	Expected Result: An error message appears, indicating that the project name is required.


Scenario 3: Create a Project with No Postgres Version Selected
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Enter a valid project name.
2.	Do not select any Postgres version.
3.	Choose a region.
4.	Click the "Create Project" button.
•	Expected Result: Project will be created with default version

Scenario 4: Create a Project with No Region Selected
•	Preconditions: User is on the project creation form.
•	Steps:
1.	Enter a valid project name.
2.	Select a Postgres version.
3.	Do not choose any region.
4.	Click the "Create Project" button.
•	Expected Result: Project will be created with default Region

Scenario 5: Create a Project with Special Characters in Name

Preconditions: User is on the project creation form.
Steps:
Enter a project name that contains special characters (e.g., !@#$%^&*()_+) in the "Name" field.
Select a Postgres version from the available options.
Choose a region from the available options.
Click the "Create Project" button.
Expected Result: The project is created successfully without any issues, and the user is
redirected to the project dashboard. This scenario tests the ability of the system to handle project names with special characters.
