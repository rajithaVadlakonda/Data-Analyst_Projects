Project 1 Description: Calculation of CAGR and Z-score
•	Objective: To calculate the Compound Annual Growth Rate (CAGR) and Z-score for a given set of companies, and to provide insights into the growth rate of companies. 

•	Methodology:
o	Data Collection and analysis: Gathered historical financial data relevant to the analysis, such as revenue, profits, stock prices, and other metric data for which growth and variability analysis were performed. I ensured the data was complete and included the duration required for accurate calculations.
o	Calculations: The compound annual growth rate (CAGR) was estimated using the turnover of a company. The Z-score was calculated using sales, EBITDA, working capital, total assets and liabilities.
o	Tools and Software’s:  Spreadsheet software tools like Microsoft Excel were used for data organization and calculations, and Python was used for more complex data handling and statistical analysis. Python libraries such as NumPy and Pandas were used for data manipulation.

•	Reporting: The CAGR and Z scores were calculated for all 74 companies. The better performing and non performing companies were identified based on the Z-score values (0-3).

Project 2 Description: Segregation of Individual Nested JSON Data to CSV file
•	Objective: The primary goal of this project is to convert and segregate individual nested JSON data entries into a structured CSV file format. This involves flattening nested structures and ensuring all relevant data fields are accurately represented in the CSV format for easier analysis and manipulation.

•	Methodology: 
o	Data Collection: Gathered individual nested JSON data entries from DataGardener solutions. 
o	Data Analysis: Analyzed the nested structure of the JSON data to identify key fields (education and profession) and nested objects or arrays (degree, start year, end year, etc.) that need to be extracted. Determined the necessary fields for the CSV file.
o	Flattening Process: Flatten nested structures into a tabular format by creating new columns based on the data set and concatenating nested values into a single column.
o	Data cleaning and Transformation: By using Python Pandas, null values were identified and removed from the data set to maintain consistency in the CSV output. 
o	Tools and software: For data manipulation, Python Pandas was used; .json was used for reading JSON data; CSV was used for writing the CSV file; .geopy was used for postal code identification.

•	Reporting: The key fields, like the educational background of each individual were segregated based on the nested structures of degree and year of course. The geographical locations of the individuals were identified using the postal code.


