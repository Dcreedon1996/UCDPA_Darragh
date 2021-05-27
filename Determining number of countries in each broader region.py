# Importing necessary packages
import pandas as pd

# Reading in and printing the data frame
df = pd.read_csv('2020.csv')
print(df)

# Creating a dictionary with the names of the broader regions
Regions = {'Europe': 0, 'Africa': 0, 'Asia': 0, 'America': 0, 'Commonwealth of Independent States': 0}

# Defining a function to count the number of times a regular expression appears in a given data frame column
def count_regex(column, regex):
    """Count the number of times `regex` appears in `column`.

    Args:
    column (pandas series): The column within a dataframe to search.
    regex (str): A regular expression to search for.

    Returns:
        int
    Raises:
        ValueError: If `regex` is not a string.
  """
    if not isinstance(regex, str):
        raise ValueError('`regex` must be a string.')
    count = sum(column.str.count(regex))
    return count

# Iterating over the dictionary so that it appropriately contains the number of countries in each broader region
for region in Regions:
    Regions[region] = count_regex(df['Regional indicator'], r".*"+region+".*")

print(Regions)

# This returns {'Europe': 38, 'Africa': 56, 'Asia': 22, 'America': 25, 'Commonwealth of Independent States': 12}
