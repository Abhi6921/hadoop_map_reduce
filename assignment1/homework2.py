import csv
from functools import reduce

def average_value_by_preferred_foot(filename):
    
    # mapper function process the input data from the file, and returns the value and preferred foot.
    def mapper(row):
        #extract the 'Preferred Foot' and 'Value' from the dataset
        preferredFoot = row['Preferred Foot']
        #remove unecessary chars like 'K', 'M' or '€' with empty string
        value_string = row['Value'].replace(',', '').replace('€', '').replace('K', '').replace('M', '')
        # example value_string or preferred foot is empty then return none
        if value_string == '' or value_string == '-':
            return None
        
        if preferredFoot == '' or preferredFoot == '-':
            return None
        player_Value = float(value_string)
        return (preferredFoot, (player_Value, 1))

    # reduce the mapped data, and convert it to a mapped dictionary with value and preferred foot
    def reducer(dictionary, current_value):
        #if value returned from mapper is none, return dictionary unchanged, 
        # otherwise extract preferredFoot and player value add to dictionary
        if current_value is None:
            return dictionary
        preferredFoot, (player_value, player_count) = current_value
        if preferredFoot in dictionary:
            dictionary[preferredFoot][0] += player_value
            dictionary[preferredFoot][1] += player_count
        else:
            dictionary[preferredFoot] = [player_value, player_count]
        # return values with player value and counts of preferred foot for each player
        return dictionary
    

    # open and read the .csv file.
    with open(filename, newline='') as csvfile:
        fileReader = csv.DictReader(csvfile)
        soccer_data = list(fileReader)

    # map the data extracted from the .csv file.
    mapped_soccer_data = list(map(mapper, soccer_data))

    # Now, we use the reduce function to reduce the mapped soccer data
    reduced_soccer_data = reduce(reducer, mapped_soccer_data, {})

    # calculate the average value of player by preferred foot and return the result
    preferredFoot_and_value_result = {}
    for preferredFoot, (total_player_value, player_count) in reduced_soccer_data.items():
        preferredFoot_and_value_result[preferredFoot] = '€{:.0f}'.format(round(total_player_value / player_count, 1))

    return preferredFoot_and_value_result


#initialize the function and print the result
output_result = average_value_by_preferred_foot('Soccer2019.csv')
print(output_result)