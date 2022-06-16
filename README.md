# Automated birthday email


## Description

This program uses Python's pandas library to access a .csv file in order to check if current day matches a birthday record stored. If it does, an email is automatically generated (based on email templates) and sent to the email address coresponding the matching birthday date. To be more efficient, this code can be hosted in the cloud with pythonanywhere and it can be scheduled as a task to automatically run daily.


## Getting Started

1. Clone the repository by entering the following command in your IDE terminal:
	git clone https://github.com/andreibarstan/automatic_birthday_wisher.git

2. Install "pandas" library:
	pip3 install pandas --user 

3. Open main.py file and populate "my_email" and "password" variables. 

3. Run the program:
	python main.py


## Acknowledgments

* Udemy - Python bootcamp
* pandas library documentation
* smtplib library documentation