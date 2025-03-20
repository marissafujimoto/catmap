# Maintainer
Click the links below to learn more about how to use the catmap application for each of the individual use cases we support.

[Visualizing and Interpreting catmaps](use_cases/visualizing_and_interpreting_cancer_datasets.md) 

[Embedding and Interpreting New Data](use_cases/embedding_and_interpreting_new_data.md) 


As a maintainer there are many tasks you might be responsible for including but not limited to:
## Responding to Issues / Questions:
These should be taken in the [catmap github issues](https://github.com/marissafujimoto/catmap/issues).
## Making Changes to the Machine Learning Models
 
The models and weights were trained in colab following the notebooks available in `notebooks`. To update the models or train new ones, work from these examples using colab.
  
The weights and preprocessed output of the model is stored in `catmap/src/catmap/data`. For larger models / data consider storing the files with [figshare](https://figshare.com/).
## Updating Code / Tests
Changes to the catmap code should go through [pull requests](https://github.com/marissafujimoto/catmap/pulls) and have at least one reviewer. Automated github actions will test for regression against existing tests and formatting, but you should also expand test coverage appropriately for your test and ensure your documentation is reasonable.
## Adding Features
Similarly adding new features should be tested and reviewed in a pull request with tests updated / added to support the new feature.
Additionally the usage examples in `examples` should be updated to guide users on how to use the new feature.