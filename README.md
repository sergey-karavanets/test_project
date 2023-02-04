# Test task for the position of Python Developer

In this test task, you need to develop an online catalog of company employees (there can be a lot of employees).

### General information

1. The test task is divided into two parts. The implementation of the second part without the first working does not make sense and will not be considered.

2. You must send your test solution to our email either as a link to a repository at github/bitbucket/gitlab/etc or as a git bundle.

3. Indicate in the letter the list of completed items for each part, the framework you have chosen. If you did not complete all the items of the test task, please indicate the reason why you did not complete them (not enough time, not enough experience / knowledge, something else).

4. When performing a test task, you can additionally use any third-party Python and / or Javascript / CSS libraries, without any restrictions. All 3rd party Python/Javascript/CSS libraries should be added to the project via pip/bower/npm/yarn if the library supports this installation method.

### Technical requirements

- Django 2.1+ / Flask 1.0+
- MySQL 5.6+ / PostgreSQL 10+
- Python 3.7+

### Part 1.

Create a web page that will display the employee hierarchy in a tree form. Information about each employee should be stored in a database and contain the following data:

- Full Name;
- Position;
- Employment date;
- Salary.

### Part 2.

1. Create a database using Django / Flask migrations.

2. Use DB seeder for Django ORM / Flask-SQLAlchemy to populate the database.

3. Create another page and display on it a list of employees with all the information about the employee from the database and the ability to sort by any field.

4. Using standard Django / Flask functions, authenticate the user for the section of the website that is accessible only to registered users.

5. Make it possible to upload a photo of an employee and display it on the page where you can edit the data about the employee. Add an additional column with an employee's thumbnail photo on the list page of all employees.