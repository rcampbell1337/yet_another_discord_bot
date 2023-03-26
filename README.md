# The Joeman Discord Bot

# Development

### Setting up the bot locally
1. Use git clone with the SSH key in whichever local folder you wish to use to develop.
2. Open the project in Visual Studio Code.
3. Run the command py -m venv venv
4. Run the command .\venv\Scripts\activate
5. Run the command pip install -r requirements.txt
6. Create a .env file, and ask me (Robbie) for the credentials to use the live version of the Discord Bot.

### Running the bot
You have probably noticed that if you run the standard py main.py you will recieve an exception, this is because there are
multiple paths for your local development testing. 

1. You can run "py main.py -live" to run an actual instance of the bot which will interact with discord. This DOES require the bot credentials.
2. You can run "py main.py -test" to run a local instance of your bot which will mock whatever output you expect to happen without actually interacting

with the live discord bot instance. You DO NOT require credentials to run this instance.

### Recommended local development
"py main.py -test" has been written to facilitate local development, mocking the live functionality of the Discord Bot by showing the output of messages which have been sent. 
This is how one should use the local development mocks:
1. When you run the py main.py -test command you will recieve the following response:
![image](https://user-images.githubusercontent.com/56073739/227771118-e84b40d2-f1bd-4eee-b1db-064e1d18f4a3.png)
2. Enter a command that you want to test: ![image](https://user-images.githubusercontent.com/56073739/227771180-88848cf9-00f2-495f-ab70-37b93368b324.png)
3. Note the response that is recieved when you enter: ![image](https://user-images.githubusercontent.com/56073739/227771231-6a0c6a4a-6b9e-4faa-a7ee-981af013bfb6.png)

Please tell me if there is anything that needs to be added to the mock, for the foreseeable future it will be quite basic.

### Creating a new command
There are a few helpers that exist to help with the development process, but the key here is that each time you create a command it should extend from an Abstract Base Class
(these are always defined with a preceding I). Point being that when we create them, the only config that exists will be the definition of the subclass itself, and then a subsequent
import into the Bot.py file (this is necessary in Python as it cannot find subclasses without a reference to the file in question). There is no need for a neverending switch
case, it is dynamically done in the Bot.py file by looking for all derived classes of our interface. We can also create new Interface types and add them to the file using a similar pattern to the one already utilised. An example of how to do this can be found in the "Hello.py" file, where a message must be defined (this corresponds to the trigger in discord) and the "message_to_send" message must be overridden.

### Unit testing
You can run unit tests with the python unittest library with the following command: py -m unittest discover testing "\*_test.py"
Please name your test files with the following convention: {name_of_message_file}_test.py


### Coding standards
1. As anal as it may be this project will use flake8, when you try to merge into develop if any Flake8 violations are found the build WILL FAIL.
2. Please unit test your code to the best of your ability, if you get stuck with it, please ask someone else to help you write them (Robbie would probably enjoy doing it anyways)
3. If you install any dependencies to your project please run the following command "pip freeze > requirements.txt" to update the project requirements or the build WILL FAIL.
4. Classes are written in pascal case (HelloWorld), functions, files and folders are written in snake case (hello_world) and any private members are written in snake case with a
preceding underscore (_hello_world)
5. Please DO NOT version control secrets for the bot, it would be very annoying to regenerate them, always reference them from your local .env file
6. Please use type hints wherever you can, it's not always possible but it is very helpful for readbility.

# GIT

### Making changes
There are two branches that we will use for the discord bot. 

1. The "main" branch will always be in sync with our live bot through CI/CD #TODO, whenever anything is merged into here we will automatically deploy it to our live bot. 
2. The "develop" branch will be our testing branch before we actually deploy our bot to live.

Both of the branches will be locked for direct pushes and must go through pull request to be merged into.

When you want to develop changes for the bot, please create a new branch off of the latest develop branch, then when you have made your changes, you can make a pull
request into develop for atleast one developer to review before merging in. Please make sure that the title and description of the PR are descriptive and clearly outline
what changes you have made. That being said, good commit messages are cool, but not the end of the world if you mess it up.
