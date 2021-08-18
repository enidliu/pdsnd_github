import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def input_mod(input_print,enterable_list):
    """
    Simplify code when user choose cities or months data
    Arg:
        (Str) input_print - asking quesetions
        (Str) enterable_list - find list(cities or months)
    Return:
        (Str) ret - return user's choice about city, month or day
    """
    while True:
        ret = input(input_print).title()
        if ret in enterable_list:
            return ret.lower()
            break
        print('Sorry, pls entre {}.'.format(enterable_list))
def see_datas(data):
    """user choose a data to input
       Arg:
          (str) data - choose a data to input(cities,months,days)
       Return:
          (str) city, month or day - return user's choice about city, month or day
    """
    cities =['Chicago','New York City', 'Washington']
    months =['January','February','March','April','May','June']
    days={'1':'Sunday', '2':'Monday', '3':'Tuesday','4':'Wednesday','5':'Thursday', '6':'Friday', '7':'Saturday'}
    while True:
        if data=='cities':
            return input_mod('Would you like to see data for Chicago, New York City or Washington:\n',cities)
        elif data=='months':
            return input_mod('which month from January to June?\n',months)
        elif data=='days':
            while True:
                day = input ('Which day? Please type an interger\n')
                if day in days:
                    return days[day]
                    break
                print ('Sorry, please enter a correct interger\n')


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
    city=see_datas('cities')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
                       enter=input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()
                       if enter=='none':
                           month='all'
                           day='all'
                           break
                       elif enter == 'both':
                            month=see_datas('months')
                            day=see_datas('days')
                            break
                       elif enter == 'month':
                            month=see_datas('months')
                            day='all'
                            break
                       elif enter == 'day':
                            month='all'
                            day=see_datas('days')
                            break
                       else:
                            print('Sorry, please input a correct content')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
        months = ['january', 'february', 'march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month']==month]

    if day !='all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print ('The most common month is:', popular_month)


    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common popular day of the week is:',popular_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().index[0]
    print('Most commonly used start station: {}.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end=df['End Station'].value_counts().index[0]
    print('Most commonly used end station: {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    Trip = df.groupby(['Start Station','End Station']).size().idxmax()

    print ('Most frequent combination of start and end station trip is {} to {}.'.format(Trip[0],Trip[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds.'.format(Total_time))

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('Mean travel time: {} seconds.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('User type\n{0}: {1}\n{2}:{3}'.format(user_type.index[0],user_type.iloc[0], user_type.index[1],user_type.iloc[1]))

    # TO DO: Display counts of gender
    cities_columns=df.columns
    if 'Gender' in cities_columns:
          user_gender=df['Gender'].value_counts()
          print('Male:{0}\nFemale:{1}.'.format(user_gender.loc['Male'],user_gender.loc['Female']))
    else:
          print('Sorry, this city do not have gender data')


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in cities_columns:
          earliest_birth=df['Birth Year'].min()
          recent_birth=df['Birth Year'].max()
          common_birth=df['Birth Year'].mode()[0]
          print ('Earliest user year of birth: %i.'%(earliest_birth))
          print('Most recent user year of birth: %i.'%(recent_birth))
          print ('Most common user year of birth: %i'%(common_birth))
    else:
          print("Sorry, this city do not have birth year data")
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
