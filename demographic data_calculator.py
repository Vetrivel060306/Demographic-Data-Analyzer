import pandas as pd



def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.loc[:, 'race'].value_counts()

    # What is the average age of men?
    male = df['sex'] == "Male"
    male_df = df[male]
    age_male = male_df.loc[:, ['sex', 'age']]
    average_age_men = round( age_male['age'].mean().max(),1)

    # What is the percentage of people who have a Bachelor's degree?

    bac = df['education'] == 'Bachelors'
    bachelors = df[bac]
    bachelor = bachelors.loc[:, ['education']]
    bachelors_sum = len(bachelor)

    edu = df['education']
    education = len(edu)
    percentage_bachelors =round((bachelors_sum / education) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_df = df[high]
    higher_education = len(high_df)

    low = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    low_df = df[low]
    low_education = len(low_df)

    # percentage with salary >50K
    higher = high_df['salary'] == ">50K"
    high_salary = high_df[higher]
    higher_salary = len(high_salary)
    higher_education_rich = round((higher_salary / higher_education) * 100,1)

    lower = low_df['salary'] == ">50K"
    lower_salary = low_df[lower]
    lower_education = len(lower_salary)
    lower_education_rich = round((lower_education / low_education) * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours= df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df['hours-per-week'] == min_work_hours
    num_min_workers = len(df[min_hours])

    salary_parse = df[min_hours]
    salary_parser = salary_parse.loc[:, ['hours-per-week', 'salary']]
    salary_parser_rich = salary_parse['salary'] == '>50K'
    rich_min_hour = len(salary_parser[salary_parser_rich])
    rich_percentage = (rich_min_hour / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_high_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_percentages = (country_high_salary_counts / country_counts * 100).fillna(0)
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)


    # Identify the most popular occupation for those who earn >50K in India.
    high_salary = df['salary'] == '>50K'
    high_salary_rich = df[high_salary]
    column = high_salary_rich.loc[:, ['native-country', 'occupation', 'salary']]
    india_parse = column['native-country'] == 'India'
    india = column[india_parse].value_counts()
    top_IN_occupation = (india.index[0])[1]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
