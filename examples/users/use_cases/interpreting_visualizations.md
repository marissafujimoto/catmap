# Interpreting Visualizations

For the visualizations, you will see visual embeddings of the top expressed genes in our training datasets. More details about the machine learning algorithms and preprocessing are available in the README, but some general takeaways are:

1. The embeddings were trained on raw counts data using an unsupervised approach.
2. As a rough rule of thumb, the distances of the embeddings tend to be more significant when the points are close compared to when they are further. Do not rely on larger distances (> 20% of the total embedding volume) to mean any significance. This is because while the final embedding is in two dimensions, the machine learning algorithm operates in higher dimensional space.
3. The known labels of the cells (e.g. the patient they come from) are projected onto the points after training.

