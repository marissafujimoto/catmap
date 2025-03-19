# Embedding New Patient Data

Catmap can be used to embed transcriptomic data collected from NSCLC patients. Catmap has limited ability to preprocess new patient data. We recommend using (seurat)[https://satijalab.org/seurat/) to preprocess your data. Ultimately it will need to be processed in the following fashion:

1. Select for the 2000 genes catmap is trained on. These genes can be loaded from the variable names of the adata_test.h5ad available in the catmap/test/data/ subdirectory.
Export an h5ad / anndata file with the X as the raw gene counts for these genes.

2. Then in the catmap UI go to the NSCLC page and click Embed New Data and follow the prompts to upload your patient data. You can use the data available in catmap/test/data to test this. The results should appear as below

TODO pic of embedding result.
