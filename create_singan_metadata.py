from pathlib import Path

# First determine the set of representative samples
# Produces a lookup table for id -> label
metadata = dict([(x.parts[-1].split('.')[0], x.parts[-2]) for x in Path('./representative_data').glob('**/*.jpg')])

all_paths = [x for x in Path('./data/output_samples').glob('**/*.png')]

with open('metadata_output/singan_train_metadata.txt', 'w') as f:
    for path in all_paths:
        f.write(str(path) + '\t' + metadata[path.parts[2]] + '\n')
print('Produced metadata_output/singan_train_metadata.txt')
