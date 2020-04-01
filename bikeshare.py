import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington dc': 'washington.csv' }

MONTH_LIST = ['january',
              'february',
              'march',
              'april',
              'may',
              'june',
              'all']

DAY_LIST = ['monday',
             'tuesday',
             'wednesday',
             'thursday',
             'friday',
             'saturday',
             'sunday',
             'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\nHello! Let\'s explore some US bikeshare data! You can look up the data for Chicago, New York City, or Washington DC.")


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("\nPlease input city name: ").lower()

    while city not in CITY_DATA:
        print("\nBikeshare data for this city is not available! Please input the name of another city: ")
        city = input("\nPlease input another city name: ").lower()

    print("\nOk, time to explore {}.".format(city.title()))



    # TO DO: get user input for the month

    month = input("\nPlease input the name of a month between January and June, or typle 'all' to get data from every available month: ").lower()

    while month not in MONTH_LIST:
            print("\nI\'m sorry, this is not a valid response!")
            month = input("\nPlease input the name of a month between January and June, or typle 'all' to get data from every month: ").lower()

    print("\nGreat! You chose {}.".format(month.title()))



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("\nPlease input a day of week, or typle 'all' to get data from every day: ").lower()

    while day not in DAY_LIST:
            print("\nI\'m sorry, this is not a valid response!")
            day = input("\nPlease input a day of week, or typle 'all' to get data from every day: ").lower()

    print("\nGreat! You chose {}.".format(day.title()))
    print("\nNow let\'s take a look at the data for {}.".format(city.title()))

    print('-'*100)
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract hour
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTH_LIST.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    try:
        pop_month_number = df['month'].mode()[0]
        pop_month_name = MONTH_LIST[pop_month_number-1]
        print("The Most Popular Month is: {}".format(pop_month_name.title()))
    except Exception as e:
        print("\nCould not calculate the Most Popular Month due to the Error: {}".format(e))

    # TO DO: display the most common day of week
    try:
        pop_day_of_week = df['day_of_week'].mode()[0]
        print("The Most Popular Day of the Week is: {}".format(pop_day_of_week.title()))
    except Exception as e:
        print("\nCould not calculate the Most Popular Day of the Week due to the Error: {}".format(e))


    # TO DO: display the most common start hour
    try:
        pop_start_hour = int(df['hour'].mode()[0])

        if pop_start_hour == 0:
            am_pm = 'am'
            pop_start_hour = 12
        elif 1 <= pop_start_hour < 13:
            am_pm = 'am'
            pop_start_hour_am_pm = pop_start_hour
        elif 13 <= pop_start_hour < 24:
            am_pm = 'pm'
            pop_start_hour_am_pm = pop_start_hour - 12
        print("The Most Popular Start Hour is: {}{}".format(pop_start_hour_am_pm, am_pm))
    except Exception as e:
        print("\nCould not calculate the Most Popular Start Hour due to the Error: {}".format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        pop_start_station = df['Start Station'].mode()[0]
        pop_start_station_amt = df['Start Station'].value_counts()[0]
        print("The Most Popular Start Station is",pop_start_station,"- it was used", pop_start_station_amt, "times.")
    except Exception as e:
        print("\nCould not calculate the Most Popular Start Station due to the Error: {}".format(e))


    # TO DO: display most commonly used end station
    try:
        pop_end_station = df['End Station'].mode()[0]
        pop_end_station_amt = df['End Station'].value_counts()[0]
        print("The Most Popular End Station is",pop_end_station,"- it was used", pop_end_station_amt, "times.")
    except Exception as e:
        print("\nCould not calculate the Most Popular End Station due to the Error: {}".format(e))

    # TO DO: display most frequent combination of start station and end station trip
    try:
        trip = df['Start Station'] + " to " + df['End Station']
        pop_trip = trip.mode()[0]
        pop_trip_amt = trip.value_counts()[0]
        print("The Most Popular Trip is",pop_trip,"- it was done", pop_trip_amt, "times.")
    except Exception as e:
        print("\nCould not calculate the Most Popular Trip due to the Error: {}".format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    try:
        total_travel_time = df['Trip Duration'].sum()
        print("The Total Amount of Time Traveled is",total_travel_time,"seconds, or",total_travel_time%3600,"hours.")
    except Exception as e:
        print("\nCould not calculate the Total Amount of Time Traveled due to the Error: {}".format(e))

    # TO DO: display mean travel time

    try:
        mean_travel_time = df['Trip Duration'].mean()
        print("The Mean Amount of Time Traveled is",mean_travel_time,"seconds, or",mean_travel_time%60,"minutes.")
    except Exception as e:
        print("\nCould not calculate the Mean of Time Traveled due to the Error: {}".format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_amt = df['User Type'].count()
    print("The Total Number of Bikeshare Users is: {}".format(user_amt))

    user_amt_by_type = df['User Type'].value_counts()
    print("\nThe Total Number of Bikeshare Users by Type is:\n{}".format(user_amt_by_type))

    # Display counts of gender
    try:
        user_amt_by_gender = df['Gender'].value_counts()
        print("\nThe Total Number of Bikeshare Subscribers by Gender is:\n{}".format(user_amt_by_gender))

    except Exception as e:
        print("\nCould not calculate Subscriber Gender Data.")


    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        current_year = int(dt.datetime.now().year)

        earliest_year = df['Birth Year'].min()
        oldest_age = current_year-earliest_year
        print("\nThe Oldest Bikeshare Subscriber(s) were born in",int(earliest_year),"- making them",int(oldest_age),"years old today.")

        latest_year = df['Birth Year'].max()
        youngest_age = current_year-latest_year
        print("The Youngest Bikeshare Subscriber(s) were born in",int(latest_year),"- making them",int(youngest_age),"years old today.")

        common_year = df['Birth Year'].mode()
        common_age = current_year-common_year
        print("The Most Common Year Bikeshare Subscribers were born in is",int(common_year),"- meaning that the majority of subscribers are",int(common_age),"years old today.")

    except Exception as e:
        print("\nCould not calculate Subscriber Birth Year Data.")



    print("\n*PLEASE NOTE: Gender and Birth Year Data are only available for Bikeshare Subscribers (not Customers)\n in New York City and Chicago. This data is not available at all for Washington DC.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        index = 0
        print(df.iloc[index:index+5])

        while True:
            answer = input("\nWould you like to see five more lines of raw data? Enter yes or no: ").lower()


            if answer in ['yes', 'no']:

                if answer == 'yes':
                    index+=5
                    print(df.iloc[index:index+5])

                else:
                    break

            else:
                print("This is not a valid response. Please type 'yes' or 'no'.")


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
