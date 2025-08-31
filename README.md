# Python and SQL Notebook Data Analysis

 Executing SQL queries on SQLite3 database within a Notebook using the Polars DataFrame library to gather insights related to sales and product performance.

## Table of Contents
- [Project Overview](#project-overview)
- [Python Libraries](#python-libraries)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Demo](#demo)

## Project Overview
This project demonstrates how **Python**, the **Polars** DataFrame library and **SQLite3** can be used to perform DML operations, joins, CTEs, and SQL functions for data analysis on a dimensionally modelled data warehouse within a **Jupyter Notebook**.



## Python Libraries
- **SQLite3** - database connection management.
- **Polars** - SQL query execution and DataFrame creation.
- **Jupyter Notebooks** - interactive method for exploratory data analysis (EDA) and documentation.


## Setup and Installation
1. Clone the repo:
```
git clone https://github.com/data-with-chris/python-sql-notebook-analysis.git
cd python-sql-notebook-analysis
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
## Usage
Run the program (from the root of the repository)
```
jupyter notebook notebooks/demo.ipynb
```
## Demo
You can view the fully executed notebook (with outputs) on GitHub:

[View the demo notebook here](notebooks/demo.ipynb)





