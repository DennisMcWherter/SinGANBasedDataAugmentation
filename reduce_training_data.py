# Simple script to reduce the training metadata we load
# This will help us train faster

import numpy as np

np.random.seed(123)

# Percent of categories to keep
PERCENT_TO_KEEP=0.1

def load_metadata(file):
    with open(file, 'r') as f:
        return [x.strip().split('\t') for x in f.readlines()]

def write_metadata(metadata, file):
    with open(file, 'w') as f:
        for x in metadata:
            f.write(x[0] + '\t' + x[1] + '\n')

preserved_categories = []

# NOTE: If you have generated singan data, we can derivate the preserved categories
singan_metadata = load_metadata('./metadata_output/singan_train_metadata.txt')
preserved_categories = list(set([x[1] for x in singan_metadata]))

train_metadata = load_metadata('./metadata_output/train_metadata.txt')
test_metadata = load_metadata('./metadata_output/test_metadata.txt')

all_labels = np.array(list(set([x[1] for x in train_metadata])))

np.random.shuffle(all_labels)

num_to_keep = int(np.round(len(all_labels) * PERCENT_TO_KEEP))

kept_labels = list(all_labels[:num_to_keep])
kept_labels.extend(preserved_categories)
kept_labels = set(kept_labels)

# Filter data based on labels
filtered_training = [x for x in train_metadata if x[1] in kept_labels]
filtered_test = [x for x in test_metadata if x[1] in kept_labels]

write_metadata(filtered_training, './metadata_output/filtered_train_metadata.txt')
write_metadata(filtered_test, './metadata_output/filtered_test_metadata.txt')

print('Done.')
