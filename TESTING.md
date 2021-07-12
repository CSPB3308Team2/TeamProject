## Project Milestone 3: Testing
#### Team 2 CSPB 3308 Summer 2021
#### Team Members: Jia (Eugene) Ei, William Egesdal, Daniel Shackelford, Dylan Power and Madeline Odom


## Automated Test Cases
#### 1. Setup environment
```
 $ git clone TeamProject # Cloning project repository
 $ cd TeamProject # Enter to project directory
 $ python3 -m venv env # If not created, creating virtualenv named env
 $ source ./env/bin/activate # Activating virtualenv
 (my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies
 (my_venv)$ deactivate # When you want to leave virtual environment
 ```
###### 2. In one terminal, run Flask App 
```
Navigate into the src directory and type:
$ export FLASK_APP=main.py
$ flask run
```
###### 3. In another terminal, run test1.py
```
Navigate into the src directory and type:
$ python3 test1.py
```

###### Expected Output
- Automated test cases will run 7 tests cases to test the rowid, add, delete, and update features as well as the routes of the flask app including routes to the root, about, and home pages. The expected outcome is 7 passing tests.

## User Acceptance Testing Test Cases
## Test Case 1
###### Use case name
 - Verify 10 Todo Items can be added to the list with map information without breaking UI
###### Description
 - Test the Todo Add Functionality and Map Feature for Multiple Inputs
###### Pre-conditions
 - User has the app loaded in a web browser
###### Test steps
 1. Navigate to the "Todos" page (either by clicking "Todos" in the navigation bar or clicking the map icon on the home page).
 2. Enter the Todo Title: Go to Bank. 
 3. Click the gray map button to the left of the "Add" Button.
 4. On the map, click the pin icon for Bank of America Financial Center.
 5. Once the map information populates the form, click the add button.
 6. Repeat steps 2-5, for the following items:
     1. Go to Fedex (Step 2); Click pin for Fedex Office Print & Ship Center (Step 4)
     2. Get Takeout (Step 2); Click pin for All Star Cafe (Step 4)
     3. Continue adding pins for places until 10 items total have been added.
 7. There should be a total of 10 items in the list once completed.
###### Expected result
 - Todo item, map information (Name and Address) in the form is added to the todo list below the form and all todo items added are stored in the list.
 - Every todo list item is in a match carding slot where UI matches including "Not Complete" status, "Update" button and "Delete" button. 
 - The first item should display a foot traffic heat map. 
###### Actual result
 - User sees Todo Title, Place Name, and Place Address.
 - Each item is numbered according to the order it was added. Foot Traffic Heatmap shows for the first item on the list.
 - The number of todos added in that session match the number of todos in the list.  Therefore, 10 items should populate the list below.
###### Status (Pass/Fail)
 - Pass
###### Notes
 - N/A
###### Post-conditions
 - User is able to add multiple todos and place information is retrieved from map and added to the list.
 - The Todo Title, Place Name, Place Address, and Traffic Data are stored in the database.

## Test Case 2
###### Use case name
 - Verify that a todo list item can be updated as completed and item can be deleted.
###### Description
 - Test the completion and deletion feature as well as display of the foot traffic heat map.
###### Pre-conditions
 - User has the app loaded in a web browser and test case 1 has been completed.
###### Test steps
 1. If not completed already, complete the steps in test case 1.
 2. Once to do tasks are added, click the update button of the first todo (Go to Bank).
 3. After the item is updated, click the delete button to remove it from the list.
 4. After pressing delete, scroll back down to where the item was listed and confirm that it has been deleted.
 5. Continue steps 2-4 for the next todo (Go to Fedex).
###### Expected result
 - User should see that the task is marked as completed and then the item is removed from the list with the item information no longer being displayed.
 - The next item on the list (Go to Fedex) should show its foot traffic heat map. 
 - If any item on the list has a heat map and is first on the list, the heat map should be displayed.
###### Actual result
 - Task status is changed from "Not Complete" to "Completed" and the status changed from grey to green for UI confirmation feedback.
 - When the item is deleted, the item no longer appears in the list.
 - If the item has a heat map and is first on the list, the heatmap appears to the user. 
 - A heat map appears for the Bank of America Financial Center, Fedex, and All Star cafe when they are first on the list.
###### Status (Pass/Fail)
 - Pass
###### Notes
 - N/A
###### Post-conditions
 - User is able to mark a todo as completed.
 - The complete boolean set to true in the database.
 - User is able to delete a task and task is removed from the database.
 - If a todo item has a heat map and is first on the list, then it is displayed to the user.


## Test Case 3
###### Use case name
 - Verify that a user can navigate between the pages.
###### Description
 - Test the linkages between each page.
###### Pre-conditions
 - User has the app loaded in a web browser.
###### Test steps
 1. Click the logo, "TODO LOCO" at the center of the navigation bar.
 2. Then, click the map icon available on the page.
 3. Then, click the logo, "TODO LOCO" at the center of the navigation bar again.
 4. Then, click "Todos" in the navigation bar.
 5. Then, click "About" in the navigation bar.
###### Expected result
 - User should be able to go the home page by clicking "TODO LOCO".
 - User should be able to go to the "Todos" page by either clicking map icon on the home page or "Todos" in the navigation bar. 
 - User should be able to go to the "About" page from the navigation bar.
###### Actual result
 - User can navigate between the pages using the navigation and linked map icon.
###### Status (Pass/Fail)
 - Pass
###### Notes
 - N/A
###### Post-conditions
 - User successfully navigates to every available page in the app.


## Test Case 4
###### Use case name
 - Verify todo list maintains information for current session.
###### Description
 - Validate that the todo list information is stored in session.
###### Pre-conditions
 - User has the app loaded in a web browser and has completed test cases 1 and 2.
###### Test steps
 1. If not completed already, complete test case 1 and 2.
 2. Take note of the tasks still present in the list.
 3. Copy the URL and close the browser.
 4. Reopen the browser and navigate to the "Todos" page if it is not currently present.
 5. Verify the todo list items that were listed previously (step 2) are still present.
###### Expected result
 - User should be able to see that all todos that are still listed in the current session.
###### Actual result
 - User can see that the tasks listed are preserved in the current session.
###### Status (Pass/Fail)
 - Pass
###### Notes
 - N/A
###### Post-conditions
 - Todo items are successfully stored in a single session.
