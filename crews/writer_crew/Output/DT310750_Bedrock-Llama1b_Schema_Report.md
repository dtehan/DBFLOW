# Table report for DT310750 schema.

## Table Name: housing_train_binary

 A table is a collection of related data that is stored in a single unit, such as a database. It is used to store data that is related to a specific entity, such as an employee, account, or job. Tables are used to organize and structure data in a way that makes it easier to query, analyze, and manage.

The attributes of a table are the individual pieces of data that make up the table. They are used to describe the structure and content of the data. In the example provided, the attributes of the employee table are:
* EmployeeNo: a unique identifier for the employee
* FirstName: the customer's first name
* LastName: the customer's last name
* DOB: the date or birth of the employee
* JoinedDate: the date that the customer became an employee
* DepartmentNo: the department number

The attributes of the accounts table are:
* cust_id: a unique identifier for the customer
* last_name: the customer's last name
* first_name: the customer's first name
* city: the city that the customer lives in

The attributes of the job table are:
* job_id: a unique identifier for all jobs
* job_description: a description of what the job will do
* EmployeeNo: the employee number of the person who will perform the job
* cust_id: the customer number of the person that the job is being performed for

The attributes of the housing_train_binary table are:
* sn: a unique identifier for the train
* price: the price of the train
* lotsize: the size of the lot
* bedrooms: the number of bedrooms
* bathrms: the number of bathrooms
* stories: the number of stories
* driveway: the type of driveway
* recroom: the type of room
* fullbase: the type of base
* gashw: the type of garage
* airco: the type of air conditioning
* garagepl: the type of garage parking
* prefarea: the type of area
* homestyle: the type of home style


## Table Name: ibm_stock

 The table is used to store stock information, specifically the IBM stock prices. It captures data about the IBM stock, including its name, period, and stock price.

                 Here is a bulleted list of the attributes:
* id - a unique identifier for each stock entry
* name - the name of the IBM stock
* period - the date when the stock was last updated
* stockprice - the current stock price


## Table Name: mydata

 A table is a fundamental data structure in database design that allows for the storage and retrieval of data in a structured and organized manner. It is a collection of related data that can be accessed and manipulated using SQL commands.

Here is a brief paragraph describing the business function of the table:

The employee table captures data about employees, providing a comprehensive view of their personal and professional information, including their employee number, first name, last name, date of birth, and joined date. This information is essential for managing employee relationships, tracking employee performance, and making informed business decisions.

Here is a bulleted list describing the attributes of the table:

* EmployeeNo - a unique identifier for the employee
* FirstName - the employee's first name
* LastName - the employee's last name
* DOB - the employee's date of birth
* JoinedDate - the date the employee joined the company


## Table Name: student

 A table is a collection of related data that is stored in a single unit, allowing for efficient storage and retrieval of data. It is a fundamental concept in database design and is used to organize and manage data in a structured and organized manner.

The attributes of a table are:
• Unique identifier (primary key): a unique value that distinguishes each row in the table and allows for efficient retrieval of data.
• Data: the actual data stored in the table, which can include text, numbers, dates, and other types of data.
• Constraints: rules that define the structure and relationships between the data in the table, such as primary keys, foreign keys, and indexes.
• Indexes: additional data structures that improve the performance of queries on the table by allowing for faster retrieval of data.

In the context of the provided examples, the tables are used to capture data about employees, accounts, jobs, and students. Each table has its own unique attributes that describe the data it stores, and the tables are designed to be used together to manage and analyze that data.

Here are the expected outputs for each table:

**Employee Table**

* The employee table captures data about employees and is made up of the following attributes:
	+ Unique identifier (EmployeeNo)
	+ First name
	+ Last name
	+ Date of birth (DOB)
	+ Joined date (JoinedDate)
	+ Department number (DepartmentNo)
* The table is used to manage employee data and is a key component of the HR system.

**Accounts Table**

* The accounts table captures data about accounts and is made up of the following attributes:
	+ Unique identifier (cust_id)
	+ Last name
	+ First name
	+ City
* The table is used to manage customer data and is a key component of the financial system.

**Job Table**

* The job table captures data about jobs and is made up of the following attributes:
	+ Unique identifier (job_id)
	+ Job description
	+ Employee number
	+ Customer number
* The table is used to manage job data and is a key component of the HR system.

**Student Table**

* The student table captures data about students and is made up of the following attributes:
	+ Unique identifier (Student_ID)
	+ Name
	+ Course ID
	+ Marks
* The table is used to manage student data and is a key component of the educational system.


