import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to see the data for: Chicago, New York City, or Washington?\n").lower()
        
        if city in ('chicago', 'new york city','washington'):
            break 
        else: 
            print("\nPlease re-enter the city correctly, try again: \n")
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month would you like to see the data for: January, February, March, April, 'May', or June?" 
                      " type 'all' if you do not want to filter by month.\n").title()
        
        if month in ('January', 'February', 'March', 'April','May', 'June','All'):
            break
        else:
            print("\nPlease re-enter the month correctly, try again: \n")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day would you like to see the data for: Sunday, Monday, Tuesday, Wednesday, or Thursday?"
               " type 'all' if you do not want to filter by day.\n").title()
    
        if day in ('Sunday','Monday','Tuesday','Wednesday','Thursday','All'):
            break
        else:
            print('\nPlease re-enter the day correctly, try again: \n')
   
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("\nThe most popular month is = {}".format(common_month))


    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print("\nThe most popular day of the week is = {}".format(common_weekday))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nThe most popular start hour is = {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nThe most popular starting station is: {}".format(common_start_station))
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nThe most popular end station is: {}".format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    print("\nThe most frequent combinations of start and end station trips are: {} , {}".format(common_start_station, common_end_station))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time = {} hours".format(total_travel_time/3600))
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nMean Travel Time = {} hours".format(mean_travel_time/3600))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print("The count of user types are as follows:\n{}".format(user_types_counts))


    # TO DO: Display counts of gender
    """First we need to check if this data has a gender column (e.g., Washington has no Gender column!)"""
    
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("\nThe gender count is as follows:\n{} ".format(gender_count))
    else:
        print("\nThis dataset does not contain a Gender column")
        
    

    # TO DO: Display earliest, most recent, and most common year of birth
    """First we need to check if this dataframe has a birth column (e.g., Washington has no Gender column!)"""
    
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        
        most_recent_birth_year = df['Birth Year'].max()
        
        common_birth_year = df['Birth Year'].mode()[0]
        
        print("\nThe earliest birth is at: {}".format(earliest_birth_year))
        print("\nThe most recent birth year is at: {}".format(most_recent_birth_year))
        print("\nThe most common birth year is: {}".format(common_birth_year))
    else:
        print("\nThis dataset does not contain a birth year column")
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_rows(df):
    """Displays 5 rows based on the choice of the user"""
    
    i = 0 
    user_choice = input("Would you like to see the raw data? answer by typing Y for (yes) or N for (no) ").lower()
    if user_choice == 'y' or user_choice == 'yes':
        print("The first five rows of the dataset are: \n",df[i:i+5])
        user_choice = input("\nWould you like to see an additional five rows? answer by typing Y for (yes) or N  for (no)").lower()
        
        while user_choice == 'y' or user_choice == 'yes':
            i += 5
            print("\n The next five rows are: ", df[i:i+5])
            user_choice = input("\nWould you like to see an additional five rows? answer by typing Y for (yes) or N for (no)\n").lower()
    
    
        

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



