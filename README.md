Requirements
------------
- Git
- Python 3.9 or later  (you may need to add a specific PPA, so please ask if you are confused)
You can have multiple Python versions (2.x and 3.x)
installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3.9 like this:

    $ sudo apt-get install python3.9

For other Linux flavors, macOS and Windows, packages are available at

  https://www.python.org/getit/
  
Quick Start
------------
Clone the repository into your preferred directory

    $ git clone https://github.com/tylovejoy/acc-bot.git

Create a virtual environment in that same directory

    $ python3.9 -m venv venv

Activate the virtual environment
   
    $ source venv/bin/activate
    (venv) $

Change directory to acc-bot

    (venv) $ cd acc-bot

Install requirements.txt

    (venv) $ pip install -r requirements.txt

Create .env file in the acc-bot root folder

    (venv) $ touch .env
    (venv) $ nano .env

The .env file should have the bot token (which will be securely sent to you)

    BOT_TOKEN = "some_token_here"


Run the bot in the terminal

    (venv) $ python main.py
