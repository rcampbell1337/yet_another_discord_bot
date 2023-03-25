# The Joeman Discord Bot

### Setting up the bot locally

1. Use git clone with the SSH key in whichever local folder you wish to use to develop.
2. Open the project in Visual Studio Code.
3. Run the command py -m venv venv
4. Run the command .\venv\Scripts\activate
5. Run the command pip install -r requirements.txt
6. Create a .env file, and ask me (Robbie) for the credentials to use the live version of the Discord Bot.

### Running the bot
You have probably noticed that if you run the standard py main.py you will recieve an exception message, this is because there are
multiple paths for your local development testing. 

1. You can run "py main.py -live" to run an actual instance of the bot which will interact with discord. This DOES require the bot credentials.
2. You can run "py main.py -test" to run a local instance of your bot which will mock whatever output you expect to happen without actually interacting
with the live discord bot instance. You DO NOT require credntials to run this instance.

### Making changes
There are two branches that we will use for the discord bot. 

1. The "main" branch will always be in sync with our live bot through CI/CD #TODO, whenever anything is merged into here we will automatically deploy it to our live bot. 
2. The "develop" branch will be our testing branch before we actually deploy our bot to live.

When you want to develop changes for the bot, please create a new branch off of the latest develop branch, then when you have made your changes, you can make a pull
request into develop for atleast one developer to review before merging in. Please make sure that the title and description of the PR are descriptive and clearly outline
what changes you have made. That being said, good commit messages are cool, but not the end of the world if you mess it up.

### Coding standards
1. As anal as it may be this project will use flake8, when you try to merge into develop if any Flake8 violations are found the build WILL FAIL.
2. Please unit test your code to the best of your ability, if you get stuck with it, please ask someone else to help you write them (Robbie would probably enjoy doing it anyways)
3. If you install any dependencies to your project please run the following command "pip freeze > requirements.txt" to update the project requirements or the build WILL FAIL.
4. File names/ classes are written in pascal case (HelloWorld), functions are written in snake case (hello_world) and any private members are written in snake case with a
preceding underscore (_hello_world)
5. Please DO NOT version control secrets for the bot, it would be very annoying to regenerate them, always reference them from your local .env file