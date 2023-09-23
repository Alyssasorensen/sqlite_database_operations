# sqlite_database_operations
## HHA 504 Homework Assignment 3

### Details on the Datasets I Selected
I selected datasets from Stony Brook Medicine and Memorial Healthcare System - Miramar Hospital. Both of the datasets focus on the hospital's standard charges for services. Both of the datasets were CSV files. The dataset from Stony Brook Medicine includes columns such as code, description, type, package/line_level, gross charge, discounted cash price, and other columns that focused on the standard charges of certain insurance providers and plan types. Stony Brook Medicine had a wide variety of insurance providers. The other dataset was focused on Memorial Hospital Miramar. The dataset from Memorial Hospital Miramar included columns such as CDM ross charge, procedure code, procedure description, lawson number, revenue code, and default charge. Both datasets had varying standard charges and had both categorical and numerical values.         

### Account of the Exploratory Data Analysis Process
Before beginning the EDA process, I had to load in the packages. After loading the packages, I loaded the datasets from Stony Brook Medicine and Memorial Hospital Miramar. To start the EDA process, I printed the heads of both datasets to show an overview of each. I then printed summary statistics for both of the datasets. This included the count, mean, standard deviation, minimum value, 25% quartile, 50% quartile, 75% quartile, and maximum value for each of the columns. Following this, I cleaned the data and handled missing values. I did this by entering the following code,
> def clean_column_names(sbm):
>
>   def clean_name(name):
>        cleaned_name = re.sub(r'[^a-zA-Z0-9]', '', name)
>        return cleaned_name.lower()
>
>    sbm.columns = [clean_name(col) for col in sbm.columns]
>    return sbm
>
> sbm = clean_column_names(sbm)
> sbm
