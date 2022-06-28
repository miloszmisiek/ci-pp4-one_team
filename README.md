

# OneTeam
  ## **Contents**
  - [Important Notes](#important-notes)
  - [Tools](#tools)
  - [Credits](#credits)
  - [Acknowledgments](#acknowledgments)


## About
[OneTeam app](#) is a ship's crew task manager. The goal of the app is to help ship's staff to manage their tasks, schedule jobs and keep track of necessary activities onboard vessels. It is aim to increase productivity along workers.

Live site can be found [here](#).

## User Experience Design
### Strategy
This app is design to server ship's staff. The app is meant to intuitive and of simple design. It is achived by use of simple interface with tonned colors.

### Target Audience
OneTeam is developed for ship's members.
- Master: ship's master is meant to be admin of the app and have full control over the workflow. He has access to admin panel where he has overall responsibility over people and tasks.
- Senior Officer: the head of Deck Department, second in command of the vessel, he has rights to schedule jobs for crew with certain limitations.
- Junior Officer: under direct command of Senior Officer. They can manege their tasks to keep track of their Division of Labour.
- Bosun: the most senior among ratings (regular workers). He can use the app to have an overview of what is planned to do and brief ordinary seamen of what mangament has planned to do.

### User Stories

**Master Goals**
| Issue ID    | User Story |
|-------------|-------------|
|[#3](https://github.com/miloszmisiek/ci-pp4-one_team/issues/3)|As a Master I can approve priority 1 tasks so that I have control over high-importance tasks being scheduled|
|[#4](https://github.com/miloszmisiek/ci-pp4-one_team/issues/4)|As a Master I can decide on a new user request so that the app functionality is restricted based on rank|

**Senior Officer Goals**
| Issue ID    | User Story |
|-------------|-------------|
|[#6](https://github.com/miloszmisiek/ci-pp4-one_team/issues/6)|As a Senior Officer, I can approve priority 2 and 3 tasks for Junior Officers so that I can control workload for Junior Officers|
|[#26](https://github.com/miloszmisiek/ci-pp4-one_team/issues/26)|As a Senior Officer I can add tasks with Priority Low and Medium without Approval so that Master does not need to approve all tasks which are of lower importance|

**User Goals**
| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/miloszmisiek/ci-pp4-one_team/issues/1)|As a user I can explore home page information so that I know what the idea behind the app is|
|[#2](https://github.com/miloszmisiek/ci-pp4-one_team/issues/2)|As a user I can explore site functionality so that I will use its full potential |
|[#14](https://github.com/miloszmisiek/ci-pp4-one_team/issues/14)|As a user I can see tasks period so that I know how to manage my time effectively|
|[#15](https://github.com/miloszmisiek/ci-pp4-one_team/issues/15)|As a user I can filter tasks for a specific month so that I can plan my work in a long-term|
|[#16](https://github.com/miloszmisiek/ci-pp4-one_team/issues/16)|As a user I can see task priority so that I know which tasks are of higher importance|
|[#17](https://github.com/miloszmisiek/ci-pp4-one_team/issues/17)|As a user I can see essential and clear tasks data so that I have quick access to necessary task information|
|[#18](https://github.com/miloszmisiek/ci-pp4-one_team/issues/18)|As a user I can see today's date so that **I can plan which tasks are closer to their deadlines **|
|[#19](https://github.com/miloszmisiek/ci-pp4-one_team/issues/19)|As a user I can reset my password so that my password is restored when I forgot it or in case of a security breach|
|[#20](https://github.com/miloszmisiek/ci-pp4-one_team/issues/20)|As a user I can edit my account so that I can update my personal data if required|
|[#21](https://github.com/miloszmisiek/ci-pp4-one_team/issues/21)|As a user I can delete my account so that I can remove my profile from the app database|
|[#22](https://github.com/miloszmisiek/ci-pp4-one_team/issues/22)|As a user I can sign up and create my profile so that I have access to app functionality accordingly|
|[#23](https://github.com/miloszmisiek/ci-pp4-one_team/issues/23)|As a user I can sort tasks by table headings so that I will have my screen organized|
|[#24](https://github.com/miloszmisiek/ci-pp4-one_team/issues/24)|As a user I can see task details so that I have a better understanding of the work scope|
|[#25](https://github.com/miloszmisiek/ci-pp4-one_team/issues/25)|As a registered user I can see my dashboard with tasks as a home page so that I don't have to navigate throughout the app to see it|

**Combined Goals**
| Issue ID    | User Story |
|-------------|-------------|
|[#5](https://github.com/miloszmisiek/ci-pp4-one_team/issues/5)|As a task approval responsible person I can see clearly which task is new so that I can effectively review and approve the task if required|
|[#7](https://github.com/miloszmisiek/ci-pp4-one_team/issues/7)|As an officers member I can change tasks status so that it is clear what tasks are left to do|
|[#8](https://github.com/miloszmisiek/ci-pp4-one_team/issues/8)|As a task creator I can set task priority so that it is clear for all users how to prioritize their work|
|[#9](https://github.com/miloszmisiek/ci-pp4-one_team/issues/9)|As a task creator I can set task duration so that it is clearly stated what is planned time for a task completion|
|[#10](https://github.com/miloszmisiek/ci-pp4-one_team/issues/10)|As an Officer/Chief Mate I can see if the task is approved so that I can proceed with a planned job or delegate the task to Bosun|
|[#11](https://github.com/miloszmisiek/ci-pp4-one_team/issues/11)|As an Officer/ a Chief Mate/Master I can add new tasks so that schedule my work in an organized manner|
|[#12](https://github.com/miloszmisiek/ci-pp4-one_team/issues/12)|As a Bosun or Officer, I can see only tasks assigned to my rank so that I don't clutter my task manager with irrelevant tasks|
|[#13](https://github.com/miloszmisiek/ci-pp4-one_team/issues/13)|As a Bosun, I can see only approved tasks so that I have a clear picture of what should be done by the crew|

[Back to contents](#contents)

---
## Technologies Used
- ### Languages
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.
- ### Frameworks and libraries:
    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
- ### Databases:
    + [SQLite](https://www.sqlite.org/): was used as a development database.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

- ### Other tools:
    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pipenv](https://pypi.org/project/pipenv/): the package manager used to install the dependencies. Pipenv combines using `pip` and `virtualenv` - they work togehter as `pipenv`.
    + [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [Draw.io](https://www.lucidchart.com/) was used to make a flowchart for the README file.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.

[Back to contents](#contents)

---
## Features

OneTeam is build with following components:
- landing page (home page for logout users)
- tasks home page (logged in users)
- login page
- registration page
- logout page
- edit profile page
- change password page
- account inactive page
- confirm email page
- reset password page
- add task page
- edit task page
- user's dashboard page
- no permission page

### User Rights
| Feature     | Master  | Senior Officer    | Junior Officer | Bosun |
| ------------- | ------------- | ------------- | ---------- | ------------- |
| landing page                   | Y | Y | Y | Y |
| tasks home page                  | Y | Y | Y | Y | 
| registration page           | Y | Y | Y | Y | 
| logout page                 | Y | Y | Y | Y | 
| edit profile page           | Y | Y | Y | Y | 
| delete profile         | Y | Y |Y | Y | 
| delete other memebers         | Y (admin panel) | N |N | N |
| change password page        | Y | Y | Y | Y | 
| account inactive page                | Y | Y | Y | Y |
| confirm email page       | Y | Y | Y | Y |
| reset password page     | Y  | Y | Y | Y |
| add task page     | Y | Y| Y | N| 
| assigned users for task     | Y | Y| Y | N|
| approve tasks     | Y | Y (Priority Medium and Low) | N| N|
| complete tasks | Y | Y | Y (only assigned to user) | N|
| delete tasks *(except status Waiting for approval)* | Y | Y | Y (only assigned to user) | N|
| edit task page                   |Y | Y| Y | N|
| user's dashboard page               |Y | Y| Y | Y|
| no permission page              |N | Y| Y | Y|

**Navbar**

![Navbar Photo](#)

Navbar is structured with:
- **Logo** to the left (redirects to home page)
- **Home** page button
- **Menu** dropdown

  *Logout Users*
  - Registration link
  - Login link
  
  *Logged In Users*
  - My profile link (user's dashboard)
  - Logout link

Simplistic design without many features to focus user's on major componenets for the app.

**Footer**

![Footer Photo](#)

Footer is structured with:
- **Logo** to the left (not-redirect to home page)
- **Contact** information to the OneTeam owners (dummy data at the moment)
- **Copyright** section for the creator with links

Footer was designed to contain neccessery contact information related to the app and to be easily identified.

**Landing page**

![Landing Page Photo](#)

Landing page is structured with:
- **Hero** section containing the logo, main goal of the app and **Get Started** button which redirect to registration site
- **Mission** section with marine theme photos and short goals desriptions 
- **Final word** section to encourge users for registration with repeated **Get Started** button

**Sign Up page (registration)**

![Sign Up Photo](#)

Sign Up form is based on all-auth package template with custom styling.

All fields are required to create account.
e
Sign up page is structured with:
- **Head title** with **sign in** link and instructions
- **Email address** field
- **Confirm email** field
- **Username** field (must be unique)
- **First Name** field
- **Last Name** field
- **Select Your Rank** field *(Note: default is Bosun for model convienience, but users cannot leave blank field, they must select one rank)*
- **Password** field
- **Confirm Password** field
- **Sign Up** button which submits the form if form is valid


**Sign In page (login)**

![Sign In Photo](#)

Sign In form is based on all-auth package template with custom styling.

Sign In page is structured with:
- **Head title** with **sign up** link and instructions
- **Email or Username** field - users can user both to login
- **Confirm email** field
- **Password** field
- **Remember Me** checkbox which controls the life time of the session - allows users to remain logged in on browser close
- **Forgot Password** link which redirects to **Password Reset** page
- **Sign In** button which submits the form and redirects user to tasks home page

**Sing Out page (logout)**

![Sign Out Photo](#)

Sign Out form is based on all-auth package template with custom styling.

Sign Out page is structured with:
- **Confirmation** message for user if his request is valid (defensive programming)
- **Sign Out** button which submits the form and redirects user to landing page

**Password Reset page**

![Reset Password Photo](#)

Password Reset form is based on all-auth package template with custom styling.

Password Reset page is structured with:
- **Description** message for user how to procced with request
- **Email address** field to type in user's email address used for registration in order to sent the link to reset the password
- **Reset Password** button which submits the form and redirects user password reset completed page


**Tasks Home page**

Tasks Home page is structured with:
- **Hello** message for user which reflects on user's first name and rank.
- **Selections** section:
  - *What's Next* message with anchor icon to reflect on what is purpose of this page - show users what are valid tasks onboard the ship
  - *Select Month* menu - user can choose the month and the app will render tasks releted to the month selected with two options:
    - Tasks with Start Date matching the selection
    - Tasks with End Date matching the selection
  - *Today is* message that informs user what is today's date
- **Add Task** button which redirects to add task page
- **Tasks Table** 


All users has almost identical page layout. The elements that change are:
- **Hello** section - updates user name and rank
- **Add Task** button - not visible for user with rank of *Bosun*









## Important Notes
- Master is assigning the rank and confirming an account
- While user awaits his rank selection and profile approval he can see a site layout, but no tasks are displayed
- After user is confirmed his profile page will display accordingly to his rank

## Tools
- gunicorn
- allauth
- psycopg2
- dj_database_url
- whitenoise
- draw.io
- bootstrap v. 4.4
- [Bootstrap Icons](https://icons.getbootstrap.com/) - chevron logo
- [coolorc.co](https://coolors.co/) - choosing pallete colors for website
- [cssgradient.io](https://cssgradient.io/) - for genertating background gradients
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) - rendering form elements
- [django-session-security](https://django-session-security.readthedocs.io/en/master/index.html) - handling automatic logout after inactivity and browser close

## Credits
1. Models are based on project [Issue Tracker](https://github.com/IuliiaKonovalova/issue_tracker) created by my good friends [Juliia Konovalova](https://github.com/IuliiaKonovalova) and [Aleksei Konovalov](https://github.com/lexach91).
2. Views are based on project [Cool School](https://github.com/IuliiaKonovalova/school_app) by [Juliia Konovalova](https://github.com/IuliiaKonovalova).
3. Fixed bug with static files directory from [Stack Overflow](https://stackoverflow.com/questions/67698211/getting-get-static-css-base-css-http-1-1-404-1795-error-for-static-files)
4. Tables styling come from [css-tricks.com](https://css-tricks.com/responsive-data-tables/)
5. Sorting function used in tables comes from [W3Schools](https://www.w3schools.com/howto/howto_js_sort_table.asp)
6. SelectWithDisabled widget comes from [djangosnippets](https://djangosnippets.org/snippets/2453/)
7. Favicon generated using [favicon.cc](https://www.favicon.cc/)
8. Scroll on top button comes from [W3Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
9. Header, footer and dropdown background was copied from [SheCodes](https://gradients.shecodes.io/gradients/825).

## Acknowledgments
1. My girlfriend for being my biggest supporter throught the entire time!
2. A very big thanks to my friends [Juliia Konovalova](https://github.com/IuliiaKonovalova) and [Aleksei Konovalov](https://github.com/lexach91) for all the help, guidance and sharing their experience with me. You guys are the best!