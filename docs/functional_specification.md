
# Functional Specification

## Background

`catmap` stands for ca(ncer) t(ranscriptomics) map. More specifically, catmap is a data visualization application and tool used to visualize and project single cell gene expression data from cancer cells. First, catmap dimensionally reduces single cell gene expression datasets and visualizes them. We want the visualization to be interactive; users should be able to apply relevant filters and color by selected metadata (e.g. the patient's stage of cancer during tissue sampling). Secondly, we hope to expand beyond a visualization tool and allow new samples to be mapped into the same space as existing datasets. We hope this provides a tool that can contextualize tissue samples in a clinical setting as well as aid diagnosis and predict patient outcomes.

## Data

Our data is from the research paper, “An integrated single-cell transcriptomic dataset for non-small cell lung cancer”  https://www.nature.com/articles/s41597-023-02074-6. The main dataset we are using has 224,611 rows each corresponding to cells from human primary non-small cell lung cancer (NSCLC) tumors. It has data on the RNA of the cell, what stage the cancer is in, the patient, and the cell cluster levels. Also in the dataset we have a sparse matrix of gene expressions from the RNA sequence. These are more difficult to work with because each cell has 72,131 columns of gene expression with many of them being 0. Finally we have PCA and UMAP dimensionality reduction matrices which will be useful in creating our own dimensionality reduction.

Additionally we have are using another data set from the Broad institute: https://singlecell.broadinstitute.org/single_cell/study/SCP1162/human-colon-cancer-atlas-c295#study-summary. This dataset profiles immune responses in tumor cells of 62 patients and 371,223 cells for colorectal tumors and adjacent normal tissues.

## User Stories

### Patient

One user could be the patient who is getting screened for cancer. This user would want to be able to view the results of their transcriptions on the map of the different types of cancer. They would interact with the map by being able to see the degree of certainty and how closely they are to a certain type of cancer if at all. They would need a simple interface to be able to see this information. They likely would have little programming knowledge and would need a simple interface to view their result.

### Doctor

One user would be the doctors who are working with patients who have cancer. Doctors would want to use our software to aid their diagnosis of the patient through a visual representation of the cancer type based on known forms of cancer. They would interact with it through our app where they would need to input the data for a new patient to add to the map. They would either have access to a visual representation of all data in the database or would be able to take an individual patient’s data and determine a diagnosis based on the location of the new data in the map. They need a simple interface that does not require coding expertise because we expect their knowledge to be in the domain of medicine rather than software engineering. The results displayed would need to make sense to someone with a medical background who may not know much about machine learning.

### Public Health

Public Health includes policymakers, researchers, etc who are trying to understand cancer at a population level. Their goal is to characterize cancer in populations using gene expression data and stratify it by demographics and health outcomes. They would want to use catmap to visualize reference databases and also compare them to their other datasets. An example question they might answer might be “Does cancer expression vary significantly between lower-income and wealthier individuals?” They need to be able to view the data holistically and export it between software and upload bulk populations. They might also want to use catmap to produce visualizations of newly gathered sample data. We assume they have proficient biology, statistics, and programming skills.

### Maintainer

The maintainer would keep the cancer transcription app running and respond to bug reports. They would need to update the model based on new data to improve accuracy. They would be highly proficient in programming skills and data science.

## Use Cases

### Use case: Interacting with filter on the cancer map

* User: Open the app and open the visualization of interest
* System: Display the full map of cancer transcriptomics with no filtering applied
* User: Select a field to group by(e.g. cancer stage)
* System: Show the map colored by the selected filter and allow filtering through toggling groups

### Use case: Mapping the data for a new patient
* User: Open the app and open the visualization of interest
* System: Display the full map of cancer transcriptomics with no filtering applied
* User: Navigate to a new page where they can enter new data
* System: Prompt for the input file
* System: Map the new data on a new embedding page
* User: Analyze the mapped location of the input data and the predicted labels

### Use case: Patient viewing summary

* User: Open the app with your physician nearby
* System: Display the full map of cancer transcriptomics with no filtering applied
* User: Navigate to a new page where they can enter new data
* System: Prompt for the input file
* System: Map the new data on a new embedding page
* User: Analyze the mapped location of the input data and the predicted labels with help from doctor to interpret results

### Use Case: Maintainer maintaining the app

* User:
	* Be able to update code and respond to issues
	* Be able to update the model with new data
	* Be able to push this new version of the app to users
	* Be able to fix bugs that are reported in the app
	* Be able to add new datasets
