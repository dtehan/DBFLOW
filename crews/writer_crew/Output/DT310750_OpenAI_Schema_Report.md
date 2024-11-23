# Table report for DT310750 schema.

## Table Name: housing_train_binary

The housing_train_binary table captures data related to properties in a housing market analysis and is specifically designed for binary classification tasks in housing price prediction. It includes various attributes that detail the characteristics of each house, such as size, number of bedrooms, and amenities, which are essential for evaluating the property's value.

- sn - is a unique identifier for each property entry  
- price - is the price of the property  
- lotsize - is the size of the lot on which the property is built, measured in square feet  
- bedrooms - is the number of bedrooms in the property  
- bathrms - is the number of bathrooms in the property  
- stories - is the number of stories (levels) in the property  
- driveway - indicates whether the property has a driveway (yes or no)  
- recroom - indicates if there is a recreation room (yes or no)  
- fullbase - indicates if there is a full basement (yes or no)  
- gashw - indicates if there is a gas hot water system installed (yes or no)  
- airco - indicates if the property has air conditioning (yes or no)  
- garagepl - is the number of parking spaces available in the garage  
- prefarea - indicates if the property is located in a preferred area (yes or no)  
- homestyle - describes the style of the home (e.g., eclectic)


## Table Name: ibm_stock

The ibm_stock table captures historical stock price data for IBM and is made up of 4 attributes:  
- id - is a unique identifier for each stock price record  
- name - holds the stock name, which is "ibm" in this case  
- period - is the date when the stock price was recorded  
- stockprice - is the price of the stock on the given date


## Table Name: mydata

The mydata table captures time-series data consisting of a timestamp and its corresponding value, which could represent metrics, measurements, or other numerical data collected over time. This structure allows for tracking changes, trends, or patterns in the recorded values.

- timestamp - represents the date on which the value was recorded
- value - represents the numerical data associated with the given timestamp, typically indicating a quantity or measurement of interest


## Table Name: student

The student table captures data about students in a specific academic setting and is made up of 4 attributes:  
- Student_ID - is a unique identifier for each student.  
- Name - is the student's full name.  
- Course_ID - is the identifier for the course in which the student is enrolled.  
- Marks - represents the student's score or marks achieved in the respective course.


