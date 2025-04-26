# Writes the unseen resuls in a more readable text file, calculate average SE across test RMSE columns

import csv

# Define file path
input_csv_path = 'full_seen_unseen_results_spBLEU_m2m100_mt560_xgb.csv'

# Read the CSV file and extract the third row as a dictionary
with open(input_csv_path, mode='r') as file:
    reader = csv.reader(file)

    headers = next(reader)   # Read the header row
    next(reader)             # Skip the second row
    third_row = next(reader) # Read the third row

    unseen_results = dict(zip(headers, third_row))

# Write unseen results to a text file and calculate average RMSE for SE columns
output_txt_path = 'unseen.txt'
with open(output_txt_path, mode='w') as file:
    total_se = 0.0
    se_count = 0

    for metric_name, value in unseen_results.items():
        if 'rmse_se' in metric_name and metric_name != 'cv_rmse_se' and value != '':
            total_se += float(value)
            se_count += 1
            print(metric_name)

        file.write(f'{metric_name}: {value}\n')

    average_se = total_se / se_count if se_count > 0 else 0
    print(f'Average SE: {average_se}')
