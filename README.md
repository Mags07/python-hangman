# THE HANGMAN

(Developer: Margarita Buyukli)
The Hangman is Python terminal game which runs on Heroku. The user gets 6 tries to guess all the letters before being hanged.
**
![The Hangman](/pic.png)

[THE HANGMAN >>> Live live website ](https://python-hangman-project.herokuapp.com/)

## Table of Contents
- [**How to Play**](#how-to-play)
- [**User Experience**](#user-experience)
- [**Features**](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [**Technical Design**](#technical-design)
    - [Flowchart](#flowchart)
- [**Technologies Used**](#technologies-used)
    - [Frameworks & Tools](#frameworks--tools)
- [**Validation**](#validation)
    - [Testing](#testing)
- [**Bugs**](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Remaining Bugs](#remaining-bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

## How to play

Users play Hangman by inputting letters in terminal, with the intention of guessing the hidden word. The hangman word is hidden by underscored. Once the user guesses a letter correctly, the letter apears in the correct area so help the user guess the rest. The user has 6 lives to start with. With each incorect guess, the hangman graphic gets added a 'limb'. The user can also play again wheather they won or soft the previous round.

## User Experience

1. User is shown the rules of the game.
2. User is shown what letters they have guessed correctly in the right spacing.
3. User is shown the letters were not correct, so they do not try to use them again.
4. User wants to have option to leave the game.
5. User is can see how many tries they have left per word.

[Back to Table Of Contents](#table-of-contents)

# Features

## Existing Features

![Intro Section](/pic.png)
- Introduction section with Rules

    - Once the user opens the game, they are shown the game rules and they are asked to press P or p to Play.

![Game Play](/pic.png)
- Play game

    - Random word is generated and displayed. Hangman develops as more incorrect lettes are guessed.
    - The input terminal will only accept letters and no numbers, signs or multiple of anything.
    - When the user guesses correctly the letter apears in the correct place instead of the underscore.
    - If the guess is wrong, the user will see the wrong letters they guess in a list.
    - In case user enter same input more than once, they will be told to guess another letter.

![Play Game](/pic.png)

![Invalid Guess](/pic.png)

![Correct Guess](/pic.png)

![Wrong Guess](/pic.png)

![Already Guessed](/pic.png)

![You Win](/pic.png)

- User Wins

    - When user guess correctly whole word, user wins and the message is displayed with option to play again.

![Game Over](/docs/game-over.png)
- Game Over

    - When user uses up their guesses this is how it looks.

![Not Play Again](/pic.png)
- Play Again

    - Wheather the gamer wins or looses, they are given the option to play again.
    - If they use to play another round, a new word is generated and game starts again. 
    - If user choose not to play again, they get a thank you page and they exit. 

[Back to Table Of Contents](#table-of-contents)

## Future Features
- User names and passwords
- Highscore
- Different levels of difficulty

## Technical Design

### Flowchart

 - This Flowchart shows the flow of the user's experience of the game.

![Hangman Flowchart](/pic.png)

[Back to Table Of Contents](#table-of-contents)

## Technologies Used

- Languages:
    - Python

- Libraries:
    - os to clear the terminal

### Frameworks & Tools

- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment
- [Am I Responsive](https://ui.dev/amiresponsive) was used to create Am I Responsive image and check responsivnes

[Back to Table Of Contents](#table-of-contents)

## Validation

## Testing

The testing approach is as follows:
1. Manual testing correct and incorrect user inputs
2. Automated unit testing using the Python unittest library
3. Tested through CI PEP8 Linter (https://pep8ci.herokuapp.com/). 
    - No errors were returned.

[Back to Table Of Contents](#table-of-contents)

# Bugs

## Solved Bugs

- A couple of times I got the error 'line too long' which either I worded shorter or I divided into seperate lines.

[Back to Table Of Contents](#table-of-contents)

## Remaining Bugs

- No bugs remaining

## Deployment

### Heroku
<hr>
The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name and then choose your region
3. Click on create app
4. Go to "Settings"
5. Add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on the Fork button in the top right corner
3. Copy of the repository will be in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files (next to 'Add file') and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Code

- [ASCII Art Generator](http://patorjk.com/software/taag/) was used to create program title, you win and game over art
- Code Institute -  "Love Sandwiches - Essentials Project

## Acknowledgements

- Special Thanks to my mentor
- Thanks to my girlfriend, family and friends for support
- Thanks to Code Institute and fellow students on Slack channels 

[Back to Table Of Contents](#table-of-contents)