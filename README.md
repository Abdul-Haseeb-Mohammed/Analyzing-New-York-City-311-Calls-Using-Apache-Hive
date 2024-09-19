# Analyzing New York City 311 Calls

## Project Overview

This project involves analyzing the 311 call data for New York City to gain insights into the types of complaints, their distribution, and the performance of city agencies. The dataset includes various details about the complaints and service requests made to the NYC 311 call center.

## Data Processing and Analysis

### Data Preprocessing

Before analysis, the dataset is preprocessed using a Python script. The preprocessing step involves:

- **Converting Timestamp Formats**: The script converts timestamps from a 12-hour to a 24-hour format to ensure consistency and facilitate accurate time-based analysis.

### Data Ingestion

The cleaned dataset is uploaded to Hadoop’s distributed file system (HDFS). An external table in Apache Hive is created to map the cleaned CSV file into a structured format. This table allows for efficient querying and analysis of the data.

### Analysis Queries

Using Apache Hive, the following queries are executed:

- **Top 10 Complaint Types**
- **Top 10 Complaint Types for the Year 2022**
- **Top 10 Cities with Most Complaints**
- **Top 10 Streets with the Most Incidents in Brooklyn**
- **Top 10 Streets with the Most Incidents in Bronx**
- **Facility Types with Most Complaints**
- **Top 10 Agencies Which Received Most Complaints in 2022**
- **Top 10 Agencies Which Received Most Complaints (Overall)**
- **Agencies with the Most Open Complaints Up to 2018**
- **Top 5 Location Types with Most Complaints**

### Visualization

The results from Hive queries are visualized using Tableau. This helps in presenting the data in an intuitive format, making it easier to interpret and share findings.

### Conclusion

This project demonstrates the use of Hive for handling large datasets and performing complex queries, as well as sharing results with Tableau for effective data visualization and analysis.
