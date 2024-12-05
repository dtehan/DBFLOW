# Table report for DT310750 schema.

## Table Name: housing_train_binary

The housing_train_binary table is used for housing data analysis, particularly in the context of binary classification tasks. This table contains various attributes related to different housing features and characteristics, which can be used to predict certain binary outcomes, such as whether a house is considered high-value or low-value. Here is a detailed description of each attribute:

- **sn**: A unique identifier for each housing entry in the dataset.
- **price**: The market price of the house, indicating its monetary value.
- **lotsize**: The size of the land on which the house is built, measured in a specific unit (e.g., square feet).
- **bedrooms**: The number of bedrooms in the house.
- **bathrms**: The number of bathrooms in the house.
- **stories**: The number of stories or levels in the house.
- **driveway**: Indicates whether the house has a driveway (e.g., "yes" or "no").
- **recroom**: Indicates whether the house has a recreational room (e.g., "yes" or "no").
- **fullbase**: Indicates whether the house has a full basement (e.g., "yes" or "no").
- **gashw**: Indicates whether the house has a gas heating and water system (e.g., "yes" or "no").
- **airco**: Indicates whether the house has air conditioning (e.g., "yes" or "no").
- **garagepl**: The number of parking spaces available in the garage.
- **prefarea**: Indicates whether the house is located in a preferred area (e.g., "yes" or "no").
- **homestyle**: The architectural style of the house (e.g., "eclectic", "classic", etc.).


## Table Name: ibm_stock

The `ibm_stock` table captures historical data on the stock prices of IBM, a notable technology company. It is composed of four attributes, each providing specific details about the stock prices recorded at different points in time.

- `id` - A unique identifier for each stock price record in the table.
- `name` - The name of the company, specifically "IBM" in this case, indicating that the stock prices pertain to IBM.
- `period` - The date on which the stock price was recorded, providing a temporal context for the stock price data.
- `stockprice` - The recorded stock price of IBM on the specified date, offering insight into the company's financial performance at that time.


## Table Name: mydata

The `mydata` table is used to capture time-series data, where each row represents a specific value recorded at a given timestamp. This table is typically used for storing and analyzing data that changes over time, allowing for trend analysis, reporting, and other temporal insights.

- **timestamp**: This attribute is a string representation of a date or datetime value in VARCHAR format. It is used to denote the specific moment when the associated value was recorded. The format is flexible (e.g., 'YYYY-MM-DD'), allowing for various datetime representations.
- **value**: This attribute is a large integer (BIGINT) that holds the actual data point recorded at the specified timestamp. It represents the quantitative measure or metric being tracked over time.

The table is designed to ensure that each timestamp is unique and non-null, with corresponding values that are also non-null, ensuring data integrity for time-series analysis.


## Table Name: student

The student table captures data about students and their performance in specific courses. It is made up of 4 attributes, each serving a unique function in recording and organizing student-related information.

- **Student_ID**: This is a unique identifier for each student, ensuring that each student can be distinctly recognized within the database.
- **Name**: This attribute stores the full name of the student, allowing for the identification and personalization of student records.
- **Course_ID**: This attribute represents the unique identifier for each course a student is enrolled in, facilitating the linkage between students and their respective courses.
- **Marks**: This attribute records the marks or grades achieved by the student in the specified course, providing a quantitative measure of the student's performance in that course.


