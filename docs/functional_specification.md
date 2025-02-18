
# Functional Specification

## Background

`catmap` stands for ca(ncer) t(ranscriptomics) map. More specifically, catmap is a data visualization application and tool used to visualize and project single cell gene expression data from cancer cells. First, catmap dimensionally reduces single cell gene expression datasets and visualizes them. We want the visualization to be interactive; users should be able to apply relevant filters and color by selected metadata (e.g. the patient's stage of cancer during tissue sampling). Secondly, we hope to expand beyond a visualization tool and allow new samples to be mapped into the same space as existing datasets. We hope this provides a tool that can contextualize tissue samples in a clinical setting as well as aid diagnosis and predict patient outcomes.

## Data

TODO Erik

## User Stories

### Patient

One user could be the patient who is getting screened for cancer. This user would want to be able to view the results of their transcriptions on the map of the different types of cancer. They would interact with the map by being able to see the degree of certainty and how closely they are to a certain type of cancer if at all. They would need a simple interface to be able to see this information. They likely would have little programming knowledge and would need a simple interface to view their result.

### Doctor

One user would be the doctors who are working with patients who have cancer. Doctors would want to use our software to aid their diagnosis of the patient through a visual representation of the cancer type based on known forms of cancer. They would interact with it through our app where they would need to input the data for a new patient to add to the map. They would either have access to a visual representation of all data in the database or would be able to take an individual patient’s data and determine a diagnosis based on the location of the new data in the map. They need a simple interface that does not require coding expertise because we expect their knowledge to be in the domain of medicine rather than software engineering. The results displayed would need to make sense to someone with a medical background who may not know much about machine learning.

### Public Health

Public Health includes policymakers, researchers, etc who are trying to understand cancer at a population level. Their goal is to characterize cancer in populations using gene expression data and stratify it by demographics and health outcomes. They would want to use catmap to visualize reference databases and also compare them to their other datasets. An example question they might answer might be “Does cancer expression vary significantly between lower-income and wealthier individuals?” They need to be able to view the data holistically and export it between software and upload bulk populations. They might also want to use catmap to produce visualizations of newly gathered sample data. We assume they have proficient biology, statistics, and programming skills.

### Data Scientist

The data scientist would keep the cancer transcription app running and respond to bug reports. They would need to update the model based on new data to improve accuracy. They would be highly proficient in programming skills and data science.

## Use Cases

  

### Use case: Interacting with filter on the cancer map

* User: Open the app
* System: Display the full map of cancer transcriptomics with no filtering applied
* User: Select a filter based on age, gender, race, etc.
* System: Show the map based on the subset of data

### Use case: Mapping the data for a new patient
* User: Open the app
* System: Display the full map of cancer transcriptomics with no filtering applied
* User: Navigate to a new page where they can enter new data
* System: Prompt for the new input
* User: Input the data
* System: Map the new data to the existing cancer map
* User: Analyze the mapped location of the input data


  

### Use case: Patient viewing summary

* User:  Open the app, user authentication
* System: Display the full map of cancer transcriptomics with no filtering applied.
* User: Select their cancer screening
* System: Display a point on the map corresponding to their result

### Use Case: Data Scientist maintaining the app

* User:
-- Be able to access the backend of the app
-- Be able to update the model with new data
-- Be able to push this new version of the app to users
-- Be able to fix bugs that are reported in the app
-- Be able to add new datasets

