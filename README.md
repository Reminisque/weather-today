# weather-today
A simple Python program that scrapes and prints out weather results from a Google search weather widget.

## Setup and usage
Open up your terminal and install `pipenv`:
```
pip install pipenv
```
Then navigate to the root folder of the project and run the following command to install depedencies:
```
pipenv install
```
Before running the program, open up `config.py` in your editor, change the value of `USER-AGENT` to the User-Agent of your browser and save it:
```
USER_AGENT = "Replace this string with browser user-agent"
```

Run the program:
```
pipenv run python main.py
```
