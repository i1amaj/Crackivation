# Crackivation
#### Video Demo: https://youtu.be/VZa8-Kb75Qo
#### Description:
My final project for CS50x2024, __CRACKIVATION__, is an aesthetic and useful to-do and journaling website that is loaded with features like _a random quote generator, a local date and time displayer_, and much more. It is programmed using frontend __HTML, CSS, and JS__ and backend __Python,Flask, and SQL__.
It consists of five basic components.
```
Register
Login
Todo
Journal
Crackivation
```

##### Screenshots:
<img src="https://github.com/i1amaj/Crackivation/assets/146009506/89e928a8-9fb6-4d0f-9bd9-655d93c03da6" alt="Login" width="1000" height="500"/>
<img src="https://github.com/i1amaj/Crackivation/assets/146009506/fbe8c455-ba21-4164-a5e0-bf7ae2b9c7cc" alt="Todo" width="400" height="200" />
<img src="https://github.com/i1amaj/Crackivation/assets/146009506/5f790a7d-2146-45af-bcbb-6ce254607d46" alt="Journal" width="400" height="200" />
<img src="https://github.com/i1amaj/Crackivation/assets/146009506/f499f36d-320f-4658-9d60-3af952412208" alt="Crackivation" width="400" height="200" />


##### Files and Folders:

###### Flask session:
It is to store the flask session.

###### static:
It contains __styles.css__, which contains the CSS code to make the web application aesthetic and visually appealing.

###### templates:
It contains the HTML files. It contains a total of 5 files.
```
register.html
login.html
todo.html
journal.html
crackivation.html
```
###### app.py:
It contains the flask code to save the data in a SQL database and other Python code.

###### project.db:
It is a SQL database to store data and users.

##### Register:
This allows the user to register for an account. . It also checks whether the username already exists or not and verifies the password. Then it encrypts the passcode into a hash by using werkzeug.security, uses Flask to insert the username and the hash into the SQL database. It also adds a row in the data table with the foreign key of the user ID and initializes the data to an empty string. If the username already exists in the database, it redirects the user and displays the error message 'username taken'. It ensures that each username has a distinct name and a unique ID.

##### Login:
This allows the user to login to an account if it actually exists. It checks whether the SQL table USERS contains that username. If so, it is deciphered from the original passcode and checked to see if it is the correct password or not. If it is the right one, then it creates the session for the user according to the user name and then updatesthe data with respect to the user logged in. Ifnot,t it will redirect the user to the login page with the error message 'Incorrect username and/or password'.

##### Todo:
There is a __TODO__ page after this. It contains several features, such as selectors for mood, water intake, and sleep routine. The main assignment satisfies its objective. A new to-do task can be added to the file, clipped once it is completed, and double-clicked to remove the task. It has a form that is related to a button. . hen the user is registered, it assigns an empty string to the value of todo data, and when it is submitted, it updates the data corresponding to the user session to the innerHTML of the todo_div. It also saves whetheraaertain task is done by changing its text style to liline-throughand it also removes a certain task.

#### Journal:
Next is the journal. On the top, there is a random quote generator that displays a random quote out of an array of quotes using JavaScript. Below is the input field where you type your text. You can also customize the journal using images, providing the image links followed by (_) to display the image on the left side and (-) to display the image on the right side. Also, you can remove the text and images by clicking on them. Then there is a submit button, whic,s in return, submits the form to the route __journal__ in the flask and then updates the existing data or empty string to the innerHTML of the todo division, which contains the tasks. When the user logs in again, the previous data is stored as such, and it can also customize the previously added data.

#### Crackivation:
Last but not least is __Crackivation__. Firstly, on the top, there is a _div_ element that contains the local date and local time displayed in 12-hour format. Below is the main stuff: for each hour (up to the 24-hour mark), there is a select drop-down menu that has various options like play, sleep, study, etc. You will select one option, and then, using JS, it will display the average of your day spent on each of the activities. It also consists of a form associated with a submit button. If the select menu is selected for 5 a.m. for coding, it will remove the above table rows and assign the value of those select menus to the coding value. When the submit button is pressed,if the select menus are available, it will save them in the database, but if all the select menus are selected, it will display the new analysis division and a new 2--hourtemplate. That's it! This was my final project, ___CRACKIVATION___, and here is my amazing journey of CS50 concluds.

This was CS50!
