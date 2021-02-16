# Bird Watcher

This repository contains a set of Python tools developed to facilitate the collection of live tweets
based on a list of user provided key words/phrases. This project is built around the Tweepy library
and is designed to collect the raw json data of any tweet containing one of the provided search terms.
The file `api_config.py` can be used to quickly generate and API object with any tweepy based project. 
A secondary script is included: 'process_tweets.py' which will quickly extract pertinent data from the
raw json twitter data relating specifically to the user (along with the text, location, and key identifiers)
and store that data in csv format for later use with other programs. 


## Getting Started

These tools are optimized for Python 3.x, require the Tweepy library to be installed, and you must have a
Twitter developer account along with a set of unique API keys, tokens, and secret values to function.

### Prerequisites

## Twitter API Authentication Credentials

The Twitter API requires a series of authentication credentials linked to a valid twitter account to work.
These credentials are four text strings: Consumer key, Consumer secret, Access token, Access secret. 
To obtain these credentials for your application you'll need to sign up for a Twitter Developer Account.
If you already have a Twitter user account, then follow the steps below to generate your key, token, and secrets.
Otherwise, please go ahead and sign up as a new Twitter user before proceeding any further.

## Applying for a Twitter Developer Account

Navigate to the [Twitter Developer Page](https://developer.twitter.com/en) to apply for a developer account.
Once here, you will need to select the Twitter user responsible for the developer account.
Twitter will request some specific information about how you plan to use your new developer account,
including whether or not you will be primarily using it for personal purposes or for on behalf of an organization.


## Creating a New Application

Note: Twitter only grants authentication credentials to applications, not to individual accounts.
An app can actually be any tool or bot that relies on the Twitter API. This means that you will need to
create and register this tool a a new app in order to be able to make calls to the Twitter API.

To register your app, go to your [Twitter Apps Page](https://developer.twitter.com/en/apps) and select the Create an app option.
Note: You will need to provide the following information about your new application and how you plan to use it:
These details include providing a name, description, intended uses for the app, and any associated URL/website.

## Generating the Authentication Credentials

Once you've filled out all the information for your application and gotten approval from Twitter return to
the [Twitter Apps Page](https://developer.twitter.com/en/apps) where you should see a list of all the Apps
you have created along with  a 'Details' button next to each application's name. Click the 'Details' button
to go o the next page, where you can finally generate the required credentials.
By selecting the Keys and tokens tab, you can generate and copy your Application's key, token, and secrets
for use with this project.

After generating the credentials, save them somewhere secure - we will touch on how integrate them into this project
under the Usage section. 

## Python

Python 3 is essential for running this program and we also suggest setting a python virtual environment
(venv) or (pipenv) when running this tool in order to keep your workspace isolated.

If you already know you have an appropriate version of Python installed on your system, you can skip to Usage

If you know you're missing Python3, you can find download the appropriate package for your OS via the link below.
If you're unsure, or you have never installed Python before check out the next section about installing python.

* [Python.org](https://www.python.org/getit/) - Get Python 3.x here

## Installing Python

First check to see if Python is installed on your system and if so, what version is running. 
How that process works depends largely on your Operating System (OS).

### Linux

Note: Most Linux distributions come with Python preloaded, but it might not be with the latest version
 and you could only have Python 2 instead of Python 3 (which is what this program is written in).
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

### Windows

In windows, open ‘cmd’ (Command Prompt) and type the following command.

```
C:\> python --version

```
Using the --version switch will show you the version that’s installed. Alternatively, you can use the -V switch:
```
C:\> python -V

```
Either of the above commands will give the version number of the Python interpreter installed or they will display an error if otherwise.

### Mac OSX

Starting with Catalina, Python no longer comes pre-installed on most Mac computers, and many older models only
have Python 2 pre-installed, not Python 3. In order to check the Python version currently installed on your Mac,
open a command-line application, i.e. Terminal, and type in any of the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```
Note:
You’ll want to either download or upgrade to the latest version of Python if any of the following conditions are true:
* None of the above commands return a version number on your machine.
* The only versions you see listed when running the above commands are part of the Python 2.x series.
* Your version of Python 3 isn’t at least version 3.8x.

If Python is not already on your system, or it is not version 3.8x or above, you can find
detailed installation instructions for your particular OS, here:

Detailed instructions for installing Python3 on Linux, MacOS, and Windows, are available at link below:

* [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) - How to install Python3

## Package Management with pip

Once you have verified that you have Python 3.x installed and running on your system, you'll be using the built in
package manager 'pip' to handle the rest of the installations. 

pip is the reference Python package manager and is used to install and update packages. 
You’ll need to make sure you have the latest version of pip installed on your system.

### Linux

Note: Debian and most other distributions include a python-pip package. If, for some reason, you prefer to use 
one of the Linux distribution-provided versions of pip instead vist [https://packaging.python.org/guides/installing-using-linux-tools/].
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

# Upgrade pip python3
$ python3 -m pip install --user --upgrade pip
```

### Windows

The Python installers for Windows include pip. You should be able to see the version of pip by opening ‘cmd’ (the Command Prompt) and entering the following: 

```
C:\> python -m pip --version

```
You can make sure that pip is up-to-date by running:
```
C:\> python -m pip install --upgrade pip

```


### Mac OSX

 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python -m pip --version

# Check the Python 3 version
$ python3 -m pip --version
```
You can also install pip yourself to ensure you have the latest version. It’s recommended to use the system pip to bootstrap a user installation of pip:
```
# Upgrade pip
$ python -m pip install --user --upgrade pip

#Upgrade pip python3
$ python3 -m pip install --user --upgrade pipn
```

## Setting up a Virtual Environment in Python

It is recommended that you create a virtual environment in order to perform operations with this program on your system, 
this will need to be accomplished before installing any further dependencies this tool relies on.
The 'venv' module is the preferred way to create and manage virtual environments for this tool. 
Luckily since Python 3.3m venv is included in the Python standard library.
 Below are the steps needed to create a virtual environment and activate it in the working directory for this tool.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> python -m venv env

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
# If you only have Python3 installed or Python3 is set as your default
$ python -m venv env

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 -m venv env
```

Note: The second argument is the location to create the virtual environment.
so accourding to the above commands: venv will create a virtual Python installation in the env folder.
In general, you can simply create this in your project yourself and call it env (or whatever you want).

Tip: You should be sure to exclude your virtual environment directory from your version control system using .gitignore or similar.

## Activating the Virtual Environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment
erves to put the virtual environment-specific python and pip executables into your shell’s PATH.

### Linux

To create a virtual environment, go to your project’s directory and run venv, as shown below:
```
$ source env/bin/activate
```

### Windows

To create a virtual environment, go to your project’s directory and run venv, as shown below: 

```
C:\> .\env\Scripts\activate

```

### Mac OSX

To create a virtual environment, go to your project’s directory and run venv, as shown below: Double check your system's version by using the following commands:
```
$ source env/bin/activate
```
Now the development environment has been properly set up with and up to date version of Python 3 there are only two 
additional dependencies besides the standard libraries included with Python. Note: as long as your virtual environment is activated
pip will install packages into that specific environment and you’ll be able to import and use those packages in your Python application.
 Instructions about installing the two required packages via pip follow: 


## Additional Dependencies

Included in this repository should be a 'requirements.txt' file, with the required libraries formatted as shown below.

```
certifi==2020.12.5
chardet==4.0.0
idna==2.10
oauthlib==3.1.0
PySocks==1.7.1
requests==2.25.1
requests-oauthlib==1.3.0
six==1.15.0
tweepy==3.10.0
urllib3==1.26.3

```

To install these dependencies with via the 'requirements.txt' file, simply use  `pip -m install -r requirements.txt`
Note: The above dependencies are required by Tweepy and are typically installed alongside Tweepy.

### Linux

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```

### Windows

Make sure the document 'requirements.txt' is in your current working directory and run: 

```
C:\> python -m pip install -r requirements.txt

```

### Mac OSX

Make sure the document 'requirements.txt' is in your current working directory and run:
```
$ python -m pip install -r requirements.txt
```
To install these dependencies without the 'requirements.txt' file, follow the below instructions:

### Linux

Make sure that your virtual environment is activated if you are using one before running the below:
```
$ python -m pip install tweepy

```

### Windows

Make sure that your virtual environment is activated if you are using one before running the below:

```
C:\> python -m pip install tweepy

```

### Mac OSX

Make sure that your virtual environment is activated if you are using one before running the below:
```
$ python -m pip install tweepy
```

Once you have generated the API credentials and installed this one key library using this program is fairly straight forward.

## Usage 'get_tweets.py'

The first step in using these tools is to export your Twitter Application Credentials as environment variables so
that these tools can properly interface with the Twitter API. Open up your terminal and activate you virtual environment
if you're using one. Once you're ready to begin using these tools export the credentials as shown below:

```
$ export CONSUMER_KEY=“{ADD_YOUR_KEY_HERE}”
$ export CONSUMER_SECRET="{ADD_CONSUMER_SECRET_HERE}"
$ export ACCESS_TOKEN="{ADD_YOUR_TOKEN_HERE}"
$ export ACCESS_TOKEN_SECRET="{ADD_YOUR_TOKEN_SECRET_HERE}"
```
Note: make sure to replace the appropriate values for your application inside the double quotation marks.
Once these environment variables have been properly initialized you're ready to move on to the next step.

To open up a Stream Listener and begin collecting Live Tweets based on your search terms, begin with `get_tweets.py`
Run `python get_tweets.py` - as shown below there are also a set of optional arguments:

```
usage: get_tweets.py [-h] [-s SEARCH_TERMS [SEARCH_TERMS ...]] [-o [OUT_FILE]]
                     [-t [TIME_LIMIT]] [-p [PAGE_LIMIT]]

Python script to collect live tweets containing matches to a list of key words

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH_TERMS [SEARCH_TERMS ...], --search_terms SEARCH_TERMS [SEARCH_TERMS ...]
                        Key word(s) or phrase(s) to search for
  -o [OUT_FILE], --out_file [OUT_FILE]
                        Output file to save raw json tweets
  -t [TIME_LIMIT], --time_limit [TIME_LIMIT]
                        Set time limit (in seconds) for the program. Default: 3600
                        seconds
  -p [PAGE_LIMIT], --page_limit [PAGE_LIMIT]
                        Set the limit for # of tweets saved per file. Defaul: 20,000
```

If no arguments are specified upon running this program, the program will display the help menu seen above automatically.
The optional arguments shown above allow the user to either specify Search Terms: A list of words or phrases separated by spaces,
Out File: where the raw tweets in json format will be saved, Time Limit: set how long you wish the program to run, default is 1 hour,
Page Limit: this limits how many tweets are stored in a single file (and will automatically add numbers to end of new file names to keep track
of the order)m the default here is set to 20,0000 tweets which results in a file around 1.75GB in size.
If either the search terms of the out file name is not specified as a command line argument the user will be prompted to enter those values

Operating System specific instructions are included below:

### Linux

If you're in the same directory as the 'get_tweets.py' file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python get_tweets.py
or
$ python get_tweets.py -h

$ python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 get_tweets.py
or
$ python3 get_tweets.py -h

$ python3 get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```
If you're not in the directory where the 'get_tweets.py' file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/get_tweets.py
or
$ python /Path/to/the/directory/get_tweets.py -h

$ python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'


# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/get_tweets.py
or
$ python3 /Path/to/the/directory/get_tweets.py -h

python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```

### Windows

On some recent versions of Windows, it's possible to run Python scripts by only entering
the name of the file containing this project's code at the command prompt:
```
C:\> get_tweets.py
or
C:\> get_tweets.py -h

C:\> get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```
If you're in the same directory as this Python's project (.py) file, simply enter the above command,
or you can directly call the python interpreter via the below command: 
```
C:\> python get_tweets.py
or
C:\> python get_tweets.py -h

C:\> python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
```
C:\> python /Path/to/the/directory/get_tweets.py
or
C:\> python /Path/to/the/directory/get_tweets.py -h

C:\> python /Path/to/the/directory/get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```

### MacOS

If you're in the same directory as the 'get_tweets.py' file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python get_tweets.py
or 
$ python get_tweets.py -h

$ python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 get_tweets.py
or
$ python3 get_tweets.py -h

$ python3 get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'
```
If you're not in the directory where the 'get_tweets.py' file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/get_tweets.py
or
$ python /Path/to/the/directory/get_tweets.py -h

$ python /Path/to/the/directory/get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/get_tweets.py
or
$ python3 /Path/to/the/directory/get_tweets.py -h

$ python3 /Path/to/the/directory/get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'

```
Upon the successful execution of the 'get_tweets.py' file, the results displayed to the
standard output should mimic what is shown below (with some differences based on the input supplied):

```
 $ python get_tweets.py -o raw_tweets.json -t 120 -s KeyWord HashTag 'Some Phrase'

 ***** Running Program *****
[+] Creating API...
INFO:root:API successfully created
[+] Starting Listener...
[+] Program will run for 120.0 seconds...
[+] Searching for the following key words:
	['KeyWord', 'HashTag', 'Some Phrase']
[+] Saving stream to 'raw_tweets.json' ...

```
Upon seeing the above, this program should be working as intended and will continue running for the specified time limit
listenning for tweets that match the provided search terms and saving them in the designated out file.
To terminate the program early you can either kill the process or perform a keyboard interrupt.

## Usage 'process_tweets.py'

The first step in using these tools is to export your Twitter Application Credentials as environment variables so
that these tools can properly interface with the Twitter API. Open up your terminal and activate you virtual environment
if you're using one. Once you're ready to begin using these tools export the credentials as shown below:

```
$ export CONSUMER_KEY=“{ADD_YOUR_KEY_HERE}”
$ export CONSUMER_SECRET="{ADD_CONSUMER_SECRET_HERE}"
$ export ACCESS_TOKEN="{ADD_YOUR_TOKEN_HERE}"
$ export ACCESS_TOKEN_SECRET="{ADD_YOUR_TOKEN_SECRET_HERE}"
```
Note: make sure to replace the appropriate values for your application inside the double quotation marks.
Once these environment variables have been properly initialized you're ready to move on to the next step.

To open up a Stream Listener and begin collecting Live Tweets based on your search terms, begin with `get_tweets.py`
Run `python process_tweets.py` - as shown below there are also a set of optional arguments:

```
usage: process_tweets.py inFile outFile.csv

Python script designed to parse specific twitter data from a json file to a csv file

```

If no arguments are specified upon running this program, the program will display the help menu seen above automatically.
The optional arguments shown above allow the user to either specify Search Terms: A list of words or phrases separated by spaces,
Out File: where the raw tweets in json format will be saved, Time Limit: set how long you wish the program to run, default is 1 hour,
Page Limit: this limits how many tweets are stored in a single file (and will automatically add numbers to end of new file names to keep track
of the order)m the default here is set to 20,0000 tweets which results in a file around 1.75GB in size.
If either the search terms of the out file name is not specified as a command line argument the user will be prompted to enter those values

Operating System specific instructions are included below:

### Linux

If you're in the same directory as the 'process_tweets.py' file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python process_tweets.py inFile outFile.csv

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 process_tweets.py inFile outFile.csv
```
If you're not in the directory where the 'process_tweets.py' file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/process_tweets.py inFile outFile.csv


# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/process_tweets.py inFile outFile.csv
```

### Windows

On some recent versions of Windows, it's possible to run Python scripts by only entering
the name of the file containing this project's code at the command prompt:
```
C:\> process_tweets.py inFile outFile.csv
```
If you're in the same directory as this Python's project (.py) file, simply enter the above command,
or you can directly call the python interpreter via the below command: 
```
C:\> python process_tweets.py inFile outFile.csv
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
```
C:\> python /Path/to/the/directory/process_tweets.py inFile outFile.csv
```

### MacOS

If you're in the same directory as the 'process_tweets.py' file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python process_tweets.py inFile outFile.csv

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 process_tweets.py inFile outFile.csv
```
If you're not in the directory where the 'process_tweets.py' file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/process_tweets.py inFile outFile.csv


# If you have both Python2 and Python3 installed and want to specify Python3

$ python3 /Path/to/the/directory/process_tweets.py inFile outFile.csv


```
Upon the successful execution of the 'process_tweets.py' file, the results displayed to the
standard output should mimic what is shown below (with some differences based on the input supplied):

```
 $ python process_tweets.py raw_tweets.json clean_tweets.csv

File Imported: raw_tweets.json
# Tweets Imported: 338
File Exported: clean_tweets.csv

```
Upon seeing the above, this program should be working as intended and will have extracted the specified data
from the json formatted raw tweet file and exported it to the designated CSV file.
The number of tweets converted is conveniently displayed.

## Authors

* **Peter Robards** - *Initial work* - [PeterRobards](https://github.com/PeterRobards)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



