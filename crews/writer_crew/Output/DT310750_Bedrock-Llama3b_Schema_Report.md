# Table report for DT310750 schema.

## Table Name: housing_train_binary

 The housing_train_binary table captures data about housing properties and is used to store information about the properties, including their characteristics such as price, lot size, number of bedrooms and bathrooms, and features like driveways, air conditioning, and garage spaces. This table is likely used by a real estate or housing database to store data about properties for sale or rent.

• sn - is a unique identifier for the property
• price - is the price of the property
• lotsize - is the size of the property's lot
• bedrooms - is the number of bedrooms in the property
• bathrms - is the number of bathrooms in the property
• stories - is the number of stories in the property
• driveway - indicates whether the property has a driveway
• recroom - indicates whether the property has a recreation room
• fullbase - indicates whether the property has a full basement
• gashw - indicates whether the property has a gas water heater
• airco - indicates whether the property has air conditioning
• garagepl - is the number of garage spaces available
• prefarea - is the preferred area of the property
• homestyle - is the style of the property (e.g. eclectic, classic)


## Table Name: ibm_stock

 The ibm_stock table captures data about IBM stock prices and is used to track the historical stock prices of IBM over time. It contains the date, stock price, and other relevant information about IBM's stock.

* id - is a unique identifier for each stock entry
* name - is the name of the stock (in this case, IBM)
* period - is the date range for which the stock price is recorded
* stockprice - is the price of the stock on the specified date


## Table Name: mydata

 The mydata table captures data about the timestamp and corresponding value, likely used for storing and tracking data over time. 
* timestamp - is a string that represents the date and time of the data
* value - is a large integer that stores the value associated with the timestamp


## Table Name: student

 The student table captures data about students and their academic performance. It contains information about each student, including their unique identifier, name, course ID, and marks.

• Student_ID - is a unique identifier for each student
• Name - is the student's full name
• Course_ID - is the ID of the course the student is enrolled in
• Marks - is the student's score in the course


