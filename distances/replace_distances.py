# Updates MT560 and NUSA experiment CSVs with URIEL+ distances

import pandas as pd
from collections import Counter

# --- MT560 Dataset Processing ---

# Load source and target languages from MT560 experiment file
mt560_lang_cols = [0, 1]
mt560_df = pd.read_csv('experiment_csvs\\URIEL\\mt560_experiments.csv', header=None, usecols=mt560_lang_cols)

# Extract source and target language lists (excluding header)
source_langs = mt560_df[0].tolist()[1:]
target_langs = mt560_df[1].tolist()[1:]
lang_pairs = list(zip(source_langs, target_langs))

# Count frequency of each unique language pair
pair_counts = Counter(lang_pairs)
unique_pairs = list(pair_counts.keys())

# Load corresponding URIEL+ distances
mt560_distance_cols = [2, 3, 4, 5, 6, 7, 8]
mt560_dist_df = pd.read_csv('distances\\mt560_distances.csv', header=None, usecols=mt560_distance_cols).iloc[1:]

# Build dictionary: language pair → feature distances (excluding morphological for now)
distance_features = {
    f'feature_{i}': [float(val.strip('[]')) for val in mt560_dist_df.iloc[:, i].tolist()]
    for i in range(mt560_dist_df.shape[1])
}

# Construct dictionary mapping each pair to their corresponding distances
pair_to_distances = {
    pair: [distance_features[f'feature_{i}'][idx] for i in range(6)]  # first 6 features
    for idx, pair in enumerate(unique_pairs)
}

# Prepare list for morphological values (last column)
morphological_values = []

# Load full MT560 experiments file (with all columns)
mt560_full_df = pd.read_csv('experiment_csvs\\URIEL\\mt560_experiments.csv')

# Insert URIEL+ distances into the appropriate columns for each matching pair
for idx, row in mt560_full_df.iterrows():
    current_pair = (row[0], row[1])
    if current_pair in pair_to_distances:
        replacement_values = pair_to_distances[current_pair]
        start_col = 89
        end_col = start_col + len(replacement_values)

        if end_col <= len(mt560_full_df.columns):
            mt560_full_df.loc[idx, mt560_full_df.columns[start_col:end_col]] = replacement_values
            morphological_values.append(distance_features['feature_6'][unique_pairs.index(current_pair)])
        else:
            print(f"Warning: Column range {start_col}:{end_col} out of bounds for row {idx}")

# Add morphological feature as its own column
mt560_full_df['morphological'] = morphological_values

# Save updated MT560 dataset
mt560_full_df.to_csv('src\\proxy_regressor\\csv_datasets\\mt560_experiments.csv', index=False)

# --- NUSA Dataset Processing ---

# Load URIEL++ distances for NUSA
nusa_distance_cols = [2, 3, 4, 5, 6, 7, 8] # Add indices if there are more distance types
nusa_dist_df = pd.read_csv('distances\\nusa_distances.csv', header=None, usecols=nusa_distance_cols).iloc[1:]

# Convert each column to a list of floats and repeat each value 4 times (NUSA structure)
nusa_distance_dict = {}
for i, feature in enumerate(['genetic', 'geographic', 'syntactic', 'inventory', 'phonological', 'featural', 'morphological']):
    repeated_values = []
    for val in nusa_dist_df.iloc[:, i]:
        repeated_values.extend([float(val.strip('[]'))] * 4)
    nusa_distance_dict[feature] = repeated_values

# Load full NUSA experiment file and add each feature column
nusa_full_df = pd.read_csv('experiment_csvs\\URIEL\\nusa_experiments.csv')
for feature, values in nusa_distance_dict.items():
    nusa_full_df[feature] = values

# Save updated NUSA dataset
nusa_full_df.to_csv('src\\proxy_regressor\\csv_datasets\\nusa_experiments.csv', index=False)
