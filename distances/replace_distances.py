import pandas as pd
from collections import Counter

#MT560
lang_columns = [0, 1]  # Columns for source and target languages

df = pd.read_csv('experiment_csvs\\URIEL\\mt560_experiments.csv', header=None, usecols=lang_columns)

# Convert specified columns to lists
langs = {f'Column_{i}': df[i].tolist() for i in range(df.shape[1])}

# Access the lists using the correct keys
source_langs = langs['Column_0'][1:]
target_langs = langs['Column_1'][1:]
langs = [source_langs, target_langs]
distances = []
for i in range(len(source_langs)):
    distances.append([source_langs[i], target_langs[i]])

# Count occurrences of each pair
pair_counts = Counter(tuple(pair) for pair in distances)

pairs = []
for pair, count in pair_counts.items():
    pairs.append(pair)

feat_columns = [2, 3, 4, 5, 6, 7, 8]  # Columns for the URIEL+ features

df2 = pd.read_csv('distances\\URIEL++\\baseline\\mt560_distances.csv', header=None, usecols=feat_columns)

df2 = df2.iloc[1:]

distances = {
    f'Column_{i}': [float(item.strip('[]')) for item in df2.iloc[:, i].tolist()]
    for i in range(df2.shape[1])
}
 
distances_dict = {}
counter = 0
for pair in pairs:
    distances_dict[pair] = [distances['Column_0'][counter], distances['Column_1'][counter], distances['Column_2'][counter], distances['Column_3'][counter], distances['Column_4'][counter], distances['Column_5'][counter]]
    counter += 1
# Read the CSV file without headers
df3 = pd.read_csv('experiment_csvs\\URIEL\\mt560_experiments.csv')
morphological_column = []
for index, row in df3.iterrows():
    counter = 0
    for pair in pairs:
        replacement_values = distances_dict.get(pair, [])
        if row[0] == pair[0] and row[1] == pair[1]:
            start_col = 89
            end_col = 89 + len(replacement_values)
            if end_col <= len(df3.columns):
                df3.loc[index, df3.columns[start_col:end_col]] = replacement_values
                morphological_column.append(distances['Column_6'][counter])
                break
            else:
                print(f"Warning: Column slice {df3.columns[start_col:end_col]} is out of bounds for index {index}")
        counter += 1
df3['morphological'] = morphological_column
# Save the modified DataFrame back to a CSV file
df3.to_csv('src\\proxy_regressor\\csv_datasets\\mt560_experiments.csv', index=False)



# NUSA
# Specify the columns you want (by index or name)
columns_to_extract = [2, 3, 4, 5, 6, 7, 8]  # For example, to extract the first and third columns (0-based index)
# Read the CSV file without headers
df = pd.read_csv('distances\\URIEL++\\baseline\\nusa_distances.csv', header=None, usecols=columns_to_extract)
# Skip the first row if it contains headers
df = df.iloc[1:]
# Convert specified columns to lists
distances = {
    f'Column_{i}': [float(item.strip('[]')) for item in df.iloc[:, i].tolist()]
    for i in range(df.shape[1])
}
 
distances_dict = {}
counter = 0
for category in ['genetic', 'geographic', 'syntactic', 'inventory', 'phonological', 'featural', 'morphological']:
    specific_distances = []
    for distance in distances['Column_' + str(counter)]:
        for i in range(4):
            specific_distances.append(distance)
    distances_dict[category] = specific_distances
    counter += 1
df2 = pd.read_csv('experiment_csvs\\URIEL\\nusa_experiments.csv')
for key in distances_dict:
    df2[key] = distances_dict[key]
# Save the modified DataFrame back to a CSV file
df2.to_csv('src\\proxy_regressor\\csv_datasets\\nusa_experiments.csv', index=False)