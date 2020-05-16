import time
import pandas as pd
import numpy as np
import json

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
    city = input("Enter city name: ")
    city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week: ")
    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = month.title()
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day!= 'all':
        day = day.title()
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: ",df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common day of week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour: ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most popular start station: ",df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station

    print("Most popular end station: ",df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start and end stations:")
    print(df[['Start Station','End Station']].mode())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total trip duration: ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time: ",df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User type counts: ")
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print("Gender count:")
    print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest birth year: ",df['Birth Year'].min())
    print("Most recent birth year: ",df["Birth Year"].max())
    print("Common birth year: ",df["Birth Year"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
	#Call the load_data() functions
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        start_row = 0
	#Loop runs until user wants to see individual data. Loop stops once user enters no.  
        while True:
            x = input("Would you like to see individual data?\nEnter y if yes, else enter n:")
            if x == 'n' or x == 'N':
                break
            elif x == 'y' or x =='Y':
                li = list(range(start_row,start_row+5))
                z = json.loads(df.iloc[li].to_json())
		print("Individual Data:")
                print(json.dumps(z,indent = 2))
                start_row += 5
                
                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
