# Table report for DT310750 schema.

## Table Name: housing_train_binary

The housing_train_binary table is designed to capture detailed information about residential properties for use in training machine learning models or conducting housing market analyses. The attributes within the table provide critical data points about each property, including its price, size, number of bedrooms and bathrooms, and various features, helping stakeholders understand property characteristics and potential valuation.

- **sn** - serves as a unique identifier for each property entry.
- **price** - represents the sale price of the property.
- **lotsize** - indicates the size of the property lot in square feet.
- **bedrooms** - denotes the number of bedrooms in the property.
- **bathrms** - specifies the number of bathrooms.
- **stories** - refers to the number of floors or stories the property has.
- **driveway** - indicates whether the property has a driveway (yes/no).
- **recroom** - signifies the presence of a recreational room (yes/no).
- **fullbase** - shows whether the property has a full basement (yes/no).
- **gashw** - indicates if the property has gas hot water heating (yes/no).
- **airco** - denotes the presence of air conditioning (yes/no).
- **garagepl** - represents the number of garage parking spaces available.
- **prefarea** - indicates if the property is located in a preferred area (yes/no).
- **homestyle** - describes the architectural style of the property.


## Table Name: ibm_stock

The ibm_stock table captures historical stock price data for IBM, providing insights into the company's stock performance over time. This data can be utilized for financial analysis, research, and investment decision-making. The table consists of four attributes that detail key aspects of each record:

- **id** - is a unique identifier for each stock record.
- **name** - is the name of the company, which is IBM in this case.
- **period** - is the date corresponding to the stock price, indicating when the stock price was recorded.
- **stockprice** - is the recorded price of IBM stock on the specified date.


## Table Name: mydata

The mydata table is utilized to store time-series data, capturing specific values associated with various timestamps. This structure allows for efficient tracking and analysis of trends over time, making it suitable for applications such as monitoring metrics, financial data, or any other numeric measurements that change over a specified period.

- **timestamp** - records the date and time associated with the logged value, formatted as a string.
- **value** - holds a numeric representation of the data point corresponding to the given timestamp, stored as a big integer.


## Table Name: student

The student table captures data about students enrolled in various courses and their corresponding marks. This table is essential for educational institutions to evaluate student performance and manage course enrollment. It consists of four attributes that detail each student's information and their academic achievements:

- **Student_ID** - is a unique identifier for each student.
- **Name** - is the full name of the student.
- **Course_ID** - is the identifier for the course that the student is enrolled in.
- **Marks** - is the score achieved by the student in the respective course.


