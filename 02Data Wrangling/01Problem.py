# Creating a Dataframe

# load the library
import pandas as pd

# Create a Dataframe
dataframe = pd.DataFrame()

# Adding the data into the dataframe
dataframe['Name'] = ['Ambani', 'Elon', 'Birla']
dataframe['Age'] = [48, 60, 68]
dataframe['Driver'] = [True, False, True]

# Show dataframe#
# print(dataframe)

# Create row
new_person = pd.Series(['Molly', 34, True], index=['Name', 'Age', 'Driver'])

# Append data
new_df = dataframe.append(new_person, ignore_index=True)

# Show dataframe
print(new_df)

