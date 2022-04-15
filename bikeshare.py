import time
import pandas as pd
import numpy as np
from time import strftime
from time import gmtime

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
        print('-'*40)
        print('INSTRUCTIONS: YO CAN WRITE ALL INPUTS AS A NUMBERS OR WORDS IN UPPER CASE OR LOWER CASE')
        print('-'*40)
        city = input('Please choose one of the following cities that you want to explore data:\n1-Chicago\n2-New York\n3-Washington\n4-Other City\nyour input: ').lower()
        if city == '1' or city=='chicago':
            city = 'chicago'
            break
        if city == '2' or city=='new york':
            city = 'new york city'
            break
        if city == '3' or city=='washington':
            city = 'washington'
            break
        if city == '4' or city=='other' or city=='other city':
            print('>'*20 + ' NO OTHER CITIES CURRUNTLY, TRY AGAIN ' + '<'*20)
        else:
            print('>'*20 + ' INCORRECT INTRY,TRY AGAIN ' + '<'*20)
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = 0
        try:
            month = input('Please choose one of the following month:\n1-january\n2-february\n3-march\n4-april\n5-may\n6-june\n7-all\nyour input: ').lower()
            month_list = ['january','february','march','april','may','june','all']
            if month in month_list:
                month = month_list.index(month)+1
                break
            elif month in ['1','2','3','4','5','6','7']:
                month = int(month)
                break
            else:
                print('>'*20 + ' INCORRECT ENTRY, TRY AGAIN ' + '<'*20)
        except:
            print('>'*20 + ' incorrect entry, TRY AGAIN ' + '<'*20)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please choose a day of weeek:\n1-monday\n2-tuesday\n3-wednesday\n4-thursday\n5-friday\n6-saturday\n7-sunday\n8-all\nyour input:').lower()
        day_dict = {'1':'monday', '2':'tuesday', '3':'wednesday', '4':'thursday', '5':'friday', '6':'saturday', '7':'sunday'}
        day_str_dict = {'monday':'monday', 'tuesday':'tuesday', 'wednesday':'wednesday', 'thursday':'thursday', 'friday':'friday', 'saturday':'saturday', 'sunday':'sunday'}
        if day  == '8' or day=='all':
            day = 'All Day'
            break
        elif day in ['1','2','3','4','5','6','7']:
            day = day_dict[day]
            break
        elif day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            day = day_str_dict[day]
            break
        else:
            print('>'*20 + ' INCORRECT ENTRY, TRY AGAIN ' + '<'*20)
 
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
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 7:
        filt = df['month']==month
        df = df[filt]
    if day != 'All Day':
        filt = df['day of week']==day.title()
        df = df[filt]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    common_month = month_dict[common_month]
    print('The Most COMMON MONTH To Travel is: ',common_month)

    # TO DO: display the most common day of week
    common_day = df['day of week'].mode()[0]
    print('The Most COMMON DAY Of Week To Travel is: ',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The Most COMMON HOUR To Travel at hour ',common_hour , ':00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_to_see_data(df):
    while True:
        index = 0
        ask = input('Do you want to see first FIVE ROWS of data:\n1-See First 5 (write 1 or yes)\n2-See Another Number Of Rows (write 2 or see another)\n3-No Continue To Program (write 3 or no)\nYour Input:').lower()
        if ask == '3' or ask=='no':
            break
            
        elif ask == '2' or ask=='see another':
            while True:
                try:
                    print('-'*40)
                    ask_number = int(input('How many rows do you want to see:\nYour Input:'))
                    index = ask_number
                    print(df[0:index])
                    print('-'*40)
                    ask_number = input('Do you want to see another amont of rows:\n1-yes\n2-no\nYour Input:').lower()
                    if ask_number == '2' or ask_number=='no':
                        break
                    if ask_number != '1' or ask_number=='yes':
                        print('>'*20 + ' INCORRECT ENTRY, TRY AGAIN' + '<'*20)
                            
                except:
                    print('>'*20 + ' INCORRECT ENTRY, TRY AGAIN' + '<'*20)
            break
        elif ask == '1' or ask=='yes':
            while True:
                print(df[index:index+5])
                print('-'*40)
                ask = input('Do you want to see NEXT FIVE ROWS of data:\n1-yes\n2-no\nYour Input: ').lower()
                if ask == '2' or ask=='no':
                    break
                if ask == '1' or ask=='yes':
                    index += 5
                else:
                    print('>'*20 + ' INCORRECT ENTRY, TRY AGAI. ' + '<'*20)
        else:
            print('>'*20 + ' INCORRECT ENTRY, TRY AGAIN ' + '<'*20)
            
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most COMMONLY USED START STATION is: ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most COMMONLY USED END STATION is: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start to end'] = df['Start Station']+ 'To' + df['End Station']
    common_start_to_end = df['start to end'].mode()[0]
    print('The Most Frequent Combination Of START STATION AND END STATION trip is: ', common_start_to_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = strftime('%H:%M:%S',gmtime(total_travel_time))
    '''print('Total Travel Time is: ', str(datetime.timedelta(seconds=total_travel_time)))'''
    print('TOTAL Travel Time is: ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = strftime('%H:%M:%S',gmtime(mean_travel_time))
    '''print('AVERAGE Of Travel Time is: ', str(datetime.timedelta(seconds=mean_travel_time)))'''
    print('AVERAGE Of Travel Time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('COUNTS Of USER TYPES is: ',user_count)

    # TO DO: Display counts of gender
    if 'Gender' in df:
          gender_count = df['Gender'].value_counts()
          print('COUNTS of GENDER is: ',gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
          earliest_year = df['Birth Year'].min()
          print('Earliest Year Of Birth is: ',earliest_year)
          most_recent = df['Birth Year'].max()
          print('Most Recent Year Of Birth is: ', most_recent)
          most_common = df['Birth Year'].mode()[0]
          print('most Common Year Of Birth is: ',most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        month_dict ={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'All Months'}
        month = month_dict[month]
        print('You Explore Data in {} City, in {}, on {}'.format(city,month,day))
        print('Number of raws of data is {} raws'.format(df.shape[0]))
        print('-'*40)
        
        ask_to_see_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
