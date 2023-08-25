import numpy as np
import pandas as pd


def salaries():

    salaries_df = pd.read_csv(
        "/Users/anandkumar/Downloads/data/Salaries.csv")
    print(salaries_df)

    # Before Analyze the data should explore the data

    print(salaries_df.shape)

    print(salaries_df.columns)

    print(salaries_df.dtypes)

    print(salaries_df.nunique())
    print(salaries_df.count())
    print(salaries_df.isnull().sum())
    print(salaries_df[salaries_df.duplicated('Notes')])

    # Display Top 10 Rows of the Dataset
    print(salaries_df.head(10))

    # Display Last 10 rows of the DatSet
    print(salaries_df.tail(10))

    # Find the shape of Our Dataset(Number of rows and colums)
    print(salaries_df.shape)

    # Getting information about our Dataset Like TotalNumber Rows,Total Number of columns,Datatypes of each colums and memory Req
    print(salaries_df.info())

    # Check the null values in the dataset
    print(salaries_df.isnull().sum())
    print(salaries_df.count())

    # Drop ID,Notes,Agency,and status
    print(salaries_df.drop(
        ['Id', "Notes", "Agency", "Status"], axis=1, inplace=False))

    print(salaries_df)

    # Get overAll stastics about the dataframe
    print(salaries_df.describe(include="all"))
    print(salaries_df.mean())
    #
    #
    # Find the occurence of The employes names

    print(salaries_df.columns)

    print(salaries_df['EmployeeName'].value_counts().head(5))

    # Find the Number of unique job titles
    print(salaries_df["JobTitle"].nunique())

    # Total Number of job Title contain captain

    print(salaries_df[salaries_df["JobTitle"].str.contains(
        "CAPTAIN", case=False)])

    # Display All the Employes names form the fireDepartment

    print(salaries_df.columns)

    print(salaries_df[salaries_df["JobTitle"].str.contains(
        "FIRE DEPARTMENT", case=False)]["EmployeeName"])

    # Find minimum,maximum,and Average Base pay
    print(salaries_df.columns)

    print(salaries_df['BasePay'].describe())

    # Replace "Not provided"in Empolyename column to NAN
    print(salaries_df.columns)
    salaries_df["EmployeeName"] = salaries_df["EmployeeName"].replace(
        "Not provided", np.nan)

    print(salaries_df)

    # Drop the rows having missing 5 values

    print(salaries_df.count())

    salaries_df.drop(
        salaries_df[salaries_df.isnull().sum(axis=1) == 5].index, axis=0, inplace=True
    )
    print(salaries_df)

    # Find Job Title of AlBERTPARDINI
    print(salaries_df.columns)
    print(salaries_df[salaries_df["EmployeeName"]
          == "ALBERT PARDINI"]["JobTitle"])

    # How Much Albert pardini make(include benefits)
    print(salaries_df.dtypes)
    print(salaries_df[salaries_df["EmployeeName"]
          == "ALBERT PARDINI"]["TotalPayBenefits"])

    # Display Name of the person Having the highest basepay

    print(salaries_df.columns)
    max_basepay = salaries_df["BasePay"].max()
    max_basepay_rows = salaries_df[salaries_df["BasePay"] == max_basepay]
    print(max_basepay_rows)

    # Find Average BasePay of ALL Employee per year
    print(salaries_df.columns)

    sal = salaries_df.groupby('Year').mean()
    print(sal)

    # Find the Average BasePay of ALL Employess per job title
    print(salaries_df.columns)
    print(salaries_df.groupby('JobTitle').mean()["BasePay"])

    # Find Average Base PAY OF employee hAVING JOB TITLE accountant

    print(salaries_df[salaries_df["JobTitle"]
          == "ACCOUNTANT"]["BasePay"].mean())

    # Find the most 5 common jobs title
    print(salaries_df.columns)
    print(salaries_df["JobTitle"].value_counts().head())


salaries()
