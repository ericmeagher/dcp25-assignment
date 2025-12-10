# Data Centric Programming Assignment 2025

- [Assignment Brief](assignment.md)

Name: Eric Meagher

Student Number: C24733845

# Screenshots
- Menu
<img src="C:\Users\ericm\OneDrive\Pictures\Screenshots\Screenshot 2025-12-09 212621.png">

- GUI
<img src="C:\Users\ericm\OneDrive\Pictures\Screenshots\Screenshot 2025-12-09 212828.png">

# Description of the project
This is my Datacentric Programming Project which contains a list of different traditional Irish tunes, and also provides a user interface for people to lookup different tunes.

# Instructions for use
1. Run the program in Visual Studio Code, a menu will then pop up in the terminal giving you a list of 6 different options.

2. To chose one of the options you enter the corresponding number next to the text option.

3. Good to Go.

# How it works:
***The program:***

- Reads all the .abc music files and turns each tune into a Python dictionary with fields like x, title, meter, key, rtype, and body.​

- Stores those dictionaries as rows in a SQLite database table called tunes inside tunes.db.​

- Loads the tunes table into pandas so you can search and filter by title, book number, or tune type, either from the text menu or the simple Tkinter GUI.​

# List of files in the project

| File       | Source                     |
|------------|----------------------------|
| main.py    | Self written               |
| database.py| Self written               |
| abc_parser.py | From lab starter code / notes |
| gui.py     | Self written/Youtube       |


# References
* database.py
https://nagasudhir.blogspot.com/2024/11/import-export-pandas-dataframes-to.html

* gui.py
https://www.youtube.com/watch?v=vjR45AHBprk&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T&index=8
https://www.youtube.com/watch?v=atBeNqFJ9SY&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T&index=18
https://www.youtube.com/watch?v=VkTrrqnWjsg&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T&index=4

* abc_parser.py
Notes from Lab 5 in https://github.com/skooter500/dcp25/blob/main/week5/lab_solution.py

# What I am most proud of in the assignment
I am proud that I completed this assignment, as it was quite intimidating at first. But once I broke it down into its smaller pieces I was able to work on it and get it working. 

# What I learned
I learned that a program doesn’t have to be one huge file, it can be split into separate files (like abc_parser.py, database.py, main.py, gui.py) with each handling a different job, and then those files can import each other and work together as one program. 
