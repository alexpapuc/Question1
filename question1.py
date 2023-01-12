"""Given a list of signals which need sent out, each at a different set frequency,
generate the timing map (example shown below) using either python or pseudo code.
Below are a few requirements:
-	The minimum time between each signal generated is 10ms.
-	Each packet will have a set priority which will need to be considered.
-	Two signals cannot be sent at once.
-	The ability to take an input variable which changes the timing map length, measured in ms.
-	A reminder: Frequency(Hz) = 1 / Time(s)
"""

import pandas as pd


# create a dictionary with data inputs
dict_signals = {1 : {'Name' : 'Network Timeout', 'Frequency' : '200 Hz'},
                2 : {'Name' : 'Power State', 'Frequency' : '125 Hz'},
                3: {'Name': 'Engine Status', 'Frequency': '100 Hz'},
                4: {'Name': 'GPS Position', 'Frequency': '1 Hz'}
                }


#read dict_signals keys in order to create a list for priority
priority_keys = list(dict_signals.keys())
priority_keys.sort()
result_dict = {}  # create an empty dictionary in order to save the result
list_of_result_dict = []  # create an empty list in order to save the result

# read an input value for time in order to have posibility to change the time
try:
    time_ms = int(input('Enter time in millisecond:'))
    mod = time_ms % 10
    if mod != 0:
        raise Exception


except ValueError:
    print('You should enter numerical values')


except Exception:
    print("Sorry! You have to enter a number divisible by 10")


else:
    counter_time = 0      # set a start point for while loop
    no_of_priority_keys = len(priority_keys)
    counter_priority = int(priority_keys[0])   # set the first value from ordered list as a first priority
    while counter_time <= time_ms:
        #set as point of start for keys, the first value from sorted priority_keys list
        if counter_priority <= no_of_priority_keys:   #set a stop when the value reach the maximum proirity
            #print(f"Packet name {dict_signals[counter_priority]['Name']}, Time(ms) {counter_time}")
            #adding the results in a dictionary in order to display the result as a dataframe for a better visualising
            result_dict['Packet name'] = dict_signals[counter_priority]['Name']
            result_dict['Time(ms)'] = counter_time
            #print(dict_signals[counter_priority]['Name'], counter_time)
            copy_of_result_dict = result_dict.copy()
            list_of_result_dict.append(copy_of_result_dict)
            counter_priority += 1
            counter_time += 10
        else:
            counter_priority = priority_keys[0]   #reset the priority to default value

    df_results = pd.DataFrame(list_of_result_dict)
    print(df_results) #display the results in IDE
