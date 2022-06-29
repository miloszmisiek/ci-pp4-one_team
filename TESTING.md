## Manual Testing

Where automated unittesting was not completed or where extra testing was required to ensure propre functionality, the use of manual testing was implemented. The actions and results are listed below.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| **Sign Up**     |                        |                  |      |             |
| 1           | Click on the Get started button | Redirection to signup page | Y |          |
| 2           | Click on Menu button and Register link | Redirection to signup page | Y |          |
| 3           | Form fields format validation | Correct input format required from user | Y |          |
| 4           | Submit signup with blank fields | Form validation triggered, highlight the field, submission aborted | Y |          |
| 5           | Submit signup with correct values | Account Inactive site displayed | Y |      Email send/receive tested with real email account    |
| 6           | Sign in link in the header message | Redirects to login page | Y |          |
| **Sign In**     |                        |                  |      |             |
| 1           | Click on the Menu button and Login link | Redirection to login page | Y |          |
| 2           | Click on Sign Up link in the header message | Redirection to signup page | Y |          |
| 3           | Type in valid username or email with password for login and submit button| Redirection to tasks home page  | Y |          |
| 4           | Type in invalid username or email with password for login and submit button | Validation message appears | Y |          |
| 5           | Type in valid username or email with password for login and submit button - account active, email address not confirmed| Redirection to confirm your email page  | Y |          |
| 6           | Type in valid username or email with password for login and submit button - account inactive| Redirection to Account Inactive page  | Y |          |
| 7           | Sing In with Remember Me selected  | Remain logged in on browser close | Y |          |
| 8           | Sign In with Remeber me unselected  | User logged out on browser close | Y         | |
| 9           | Click Forgot Password link | Redirection to Rest Password page  | Y |          |
| **Rest Password**     |                        |                  |      |             |
| 1           | Type in correct email and press Rest Passwrod| Redirection to Password Rest done page | Y |   Tested with real email account       |
| 2           | Type in incorrect email and press Reset Password | Validation message appears to inform user on incorrect email | Y |          |
| 3           | Press Reset Password with blank email field | Form validation triggered, submition aborted | Y |          |
| **Tasks Home Page**     |                        |                  |      |             |
| 1           | User logs in | Hello message with current user's first name and rank below | Y |        |
| 2           | User logs in | Today is section represents today's date. Tasks sorted by end date ascending. Arrow showing down. | Y |        |
| 3           | Click Select Month and choose month from dropdown menu | Page refresh with tasks Start Date and End Date matching user's month selection | Y |        |
| 4           | Bosun logs in | Add Task button hidden | Y |        |
| 5           | Junior logs in | Add Task button visible | Y |        |
| 6           | Senior logs in | Add Task button visible | Y |        |
| 7           | Master logs in | Add Task button visible | Y |        |
| 8           | User clicks Add Task | Redirects to Add Task page | Y |        |
| 9           | User clicks Hide Completed button | Page refresh and with completed tasks excluded. | Y |        |
| **Table Functionality**     |                        |                  |      |             |
| 1           | User clicks table headings | Tasks sorted ascending/descending with respective heading clicked. Arrow changes on ascending down and on descendin up | Y |        |
| 2           | Bosun clicks Scheduled cell | Nothing happens | Y |        |
| 3           | Junior clicks Scheduled cell for task assigned to his user | Change Status modal appears with change to complete message | Y |        |
| 4           | Junior clicks Scheduled cell for task assigned to different user | Nothing happens | Y |        |
| 5           | Senior clicks Scheduled cell for any user's (except Master) task assigned to | Change Status modal appears with change to complete message | Y |        |
| 5           | Senior clicks Scheduled cell for task assigned to Master | Nothing happens | Y |        |


[Back to contents](#contents)
