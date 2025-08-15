import pandas as pd

# Read the music_project_en.csv file and store it in df
df = pd.read_csv('./datasets/music_project_en.csv')

# Get the first 10 rows from table df
print(df.head(10))

# Get general information about the data
df.info()

# Displays column names
print(df.columns)


# Loop through headers making everything lowercase
new_col_names = []
for low in df.columns:
    name_lowered = low.lower()
    new_col_names.append(name_lowered)

    
df.columns = new_col_names    
print(df.columns)


# Loop through headers removing spaces
new_col_names_2 = []
for old_names in new_col_names:
    name_stripped = old_names.strip()
    new_col_names_2.append(name_stripped)


df.columns = new_col_names_2
print(df.columns)

# Rename the "userid" column
df.rename(columns = {'userid':'user_id'}, inplace=True)
print(df.columns)

# Calculate the number of missing values
print(df.isna().sum())

# Loop through headers replacing missing values with 'unknown'
cols = ['track', 'artist', 'genre']
    
for col in cols:
    df[col] = df[col].fillna('unknown')

# Count missing values
print(df.isna().sum())

#Count duplicates
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Check for duplicates
print(df.duplicated().sum())

# Inspeccionar los nombres de géneros únicos
df['genre'].unique()


# Function to replace implicit duplicates
def replace_wrong_genres(df, wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genres, correct_genre)
        return df

    
# Remove implicit duplicates
print(replace_wrong_genres(df, ['hip', 'hop', 'hip-hop'], 'hiphop'))

# Checking for implicit duplicates
print(df['genre'].unique())

# Count the songs played in each city
print(df.groupby(by='city')['track'].count())

# Calculate the songs played on each of the three days
print(df.groupby(by='day')['track'].count())


# Declare the number_tracks() function with the parameters: day= and city=
def number_track(df, day, city):
    tracks_by_day = df[df['day'] == day] # Stores the rows of the DataFrame where the value in the 'day' column is equal to the day= parameter

    tracks_by_city = tracks_by_day[tracks_by_day['city'] == city] # Filters rows where the value in the 'city' column is equal to the city= parameter

    user_count = tracks_by_city['user_id'].count() # Extract the 'user_id' column from the filtered table and apply the count() method

    return user_count # Returns the number of values in the 'user_id' column


# The number of songs played in Springfield on Monday
print(number_track(df, 'Monday', 'Springfield'))

# The number of songs played in Shelbyville on Monday
print(number_track(df, 'Monday', 'Shelbyville'))

# The number of songs played in Springfield on Wednesday
print(number_track(df, 'Wednesday', 'Springfield'))

# The number of songs played in Shelbyville on Wednesday
print(number_track(df, 'Wednesday', 'Shelbyville'))

# The number of songs played in Springfield on Friday
print(number_track(df, 'Friday', 'Springfield'))

# The number of songs played in Shelbyville on Friday
print(number_track(df, 'Friday', 'Shelbyville'))
