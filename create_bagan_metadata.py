from pathlib import Path

# Path structure holds label
all_paths = [(x, x.parts[-2]) for x in Path('./data/bagan_samples').glob('**/*.jpg')]

with open('metadata_output/bagan_train_metadata.txt', 'w') as f:
    for (path,label) in all_paths:
        f.write(str(path) + '\t' + label + '\n')
print('Produced metadata_output/bagan_train_metadata.txt')
