# Outputs a text file with the test results for a specific ProxyLM experiment.

from src.proxy_regressor.utils import set_seed_all, get_dataset_random, get_all_features_combinations

NUM_REPEATS = 5
RANDOM_SEED = 42
TEST_SIZE = 0.3

# Test data
# Gather dataset; try all combinations
feature_combinations = get_all_features_combinations()

for feature_combo in feature_combinations:    
    include_lang_cols = False

    for i in range(NUM_REPEATS):
                set_seed_all(i + RANDOM_SEED)
                X_train, X_test, Y_train, Y_test, score_se_df, X_columns = get_dataset_random(
                                                                    "nllb", "nusa", # Change this for different experiments
                                                                    score_name="spBLEU", 
                                                                    test_size=TEST_SIZE,
                                                                    include_lang_cols=include_lang_cols,
                                                                    nlperf_only=feature_combo["nlperf_only"],
                                                                    dataset_features=feature_combo["dataset_features"],
                                                                    lang_features=feature_combo["lang_features"],
                                                                    with_trfm=feature_combo["with_trfm"],
                                                                    with_small100_ft=feature_combo["with_small100_ft"],
                                                                    with_small100_noft=feature_combo["with_small100_noft"],
                                                                    with_model_noft=feature_combo["with_model_noft"],
                                                                    seed=(i + RANDOM_SEED))
            
                with open("Y_test_results.txt", "a") as file:
                    file.write(", ".join(map(str, Y_test)) + "\n")  # Converts Y_test to a string and writes each value