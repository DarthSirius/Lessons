data['schools'] = data['schools'].astype(str)
# Because data in 'schools' is all messed up, we extract the ratings using regex
import re
# Leave only information about the raiting
data['schools_rating'] = data['schools'].apply(lambda x: re.sub(r'data.*', '', x))
# Remove '/10'
data['schools_rating'] = data['schools_rating'].apply(lambda x: re.sub(r'/10', '', x))
# Remove other unnecessary symbols
data['schools_rating'] = data['schools_rating'].apply(lambda x: re.sub(r'[^\w\s,]', '', x))
data['schools_rating'] = data['schools_rating'].apply(lambda x: x.replace('rating', ''))
data['schools_rating'] = data['schools_rating'].apply(lambda x: x[:-2])
data['schools_rating'] = data['schools_rating'].apply(lambda x: x[1:])

# Create a new column called 'school_count' that will count the number of schools
data['school_count'] = data['schools_rating'].apply(lambda x: (len(x.split(','))) if x != '' else 0)
data['school_count'] = data['school_count'].astype('int')
# Remove all letters
data['schools_rating'] = data['schools_rating'].apply(lambda x: re.sub(r'[a-zA-Z]', '', x))
# Remove comas withought numbers before them
data['schools_rating'] = data['schools_rating'].apply(lambda x: re.sub(r'\s+,', '', x))
# Remove comas at the end
data['schools_rating'] = data['schools_rating'].apply(lambda x: x[:-1])

# Create a new column 'schools_rating_list'
data['schools_rating_list'] = data['schools_rating'].apply(lambda x: [int(i) for i in re.findall(r'\d+', x)])
# Create a new column 'schools_rating_ave'
data['schools_rating_ave'] = data['schools_rating_list'].apply(lambda x: round(sum(x) / len(x), 2) if len(x) > 0 else 0)
# Unfortunately, '0' in 'schools_rating_ave' represents missing values.
# However, it may be interpreted as really bad schools around.
# Replace '0' with the average

data['schools_rating_ave'] = data['schools_rating_ave'].apply(np.round, decimals=2)

# Calculate the average of the 'schools_rating_ave' column
average = data['schools_rating_ave'].mean()

# Replace zero values with the average
data['schools_rating_ave'] = data['schools_rating_ave'].apply(
    lambda x: average if x < 1 else x
)

# Calculate the average distance to the schools around
# Leave only information about the distance

def extract_text(text):
  # Use a regex pattern to extract the text between 'Distance' and 'Grades'
  pattern = r"Distance': \['(.+?)'\], 'Grades'"
  match = re.search(pattern, text)
  if match:
    # Return the text that was found
    return match.group(1)
  else:
    # Return None if no text was found
    return None

# Apply the extract_text function to each cell in the 'schools' column
data['schools_distance'] = data['schools'].apply(extract_text)
data['schools_distance'] = data['schools_distance'].astype(str)
# Remove ' mi'
data['schools_distance'] = data['schools_distance'].apply(lambda x: re.sub(r'\smi', '', x))
# Remove other unnecessary symbols
data['schools_distance'] = data['schools_distance'].str.replace(r'[^\d.,\s]', '', regex=True)

# Convert cleaned strings into lists of float numbers
data['schools_distance'] = data['schools_distance'].apply(lambda x: [float(num) for num in x.split(',')] if x else [])

# Create a new column called 'schools_distance_ave'
data['schools_distance_ave'] = data['schools_distance'].apply(lambda x: round(sum(x)/len(x), 2) if x else 0)