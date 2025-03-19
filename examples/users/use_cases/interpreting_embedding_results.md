# Interpreting the Embedding Results

Three steps happen during the embedding process.

1. A trained model embeds the new data using its learned embedding trained from our reference dataset.
2. A random forest classifier predicts the cell types of the new cells.
3. A UMAP reduction is calculated for the newly embedded points.

Note that the UMAP reduction does not correspond to the reference NSCLC page’s UMAP coordinates since it focuses only on the newly uploaded data.

Also note that the ratio of classified points depends on the method of collection of the tissue samples and specifically the ratio of tissue types collected.
