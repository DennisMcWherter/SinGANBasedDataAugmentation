# SinGANBasedDataAugmentation

## Steps outline

1. Run Imbalance Notebook
2. Run KMeans notebook
3. Copy representative samples from KMeans to SinGAN's `Input/Images` directory
4. Run SinGAN on all newly generated representatives
5. Copy SinGAN-generated representatives to `data/output_samples`
6. Run `create_singan_metadata.py`
7. Run `reduce_training_data.py` to filter data
8. Run Training and Evaluation Notebook

## BAGAN Benchmark

We trained BAGAN using 150 epochs on our two unbalanced classes. The resulting 150 generated images per class are included in the `data` directory. We trained BAGAN on the entire training dataset. This differs from SinGAN where representatives were chosen.
