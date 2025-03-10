# Software Components

### <ins>**Embedding Model:**</ins>
#### **What it does:**
* Determines how to plot the cancer data into a map of cancer transcriptomics by translating the embedding data frame it is provided into coordinates for the embedding plotter
#### **Inputs:**
* Raw gene expression values from the embedding dataframe
#### **Outputs:**
* Embedding coordinates
#### **Assumptions:**
* These is an embedding data frame available to pull data from
  
### <ins>**Embedding Plotter:**</ins>
#### **What it does:**
* Displays the mapped data points based on the calculations from the embedding model
* Can display different data based on what is selected in the filtering panel
#### **Inputs:**
* Filtering panel selections, strings
* A set of coordinates to plot from the embedding model
#### **Outputs:**
* A plot of the filtered data
#### **Assumptions:**
* The embedding model has translated the embedding data frame into a set of coordinates
* The filtering panel has been selected (or no filter is applied) so it knows how to filter the data before displaying it

### <ins>**Filtering Panel:**</ins>
#### **What it does:**
* Displays filtering options and takes user input for how to filter the data that is displayed by the embedding plotter
#### **Inputs:**
* Some categorical or numerical metadata column (ex. Age (numeric), Gender (string), Race (string))
#### **Outputs:**
* A list containing the filter information that was selected
#### **Assumptions:**
* The user has selected from the filtering options
* There is a view controller to communicate with and send the filter selections to

## **Additional Components:**
* Embedding data frame - contains all data from the studies
* View controller - interacts with the embedding data frame to determine which subset of the data (ex. Type of cancer) will be used and also get filter information from the user selections in the filtering panel and communicates with the embedding plotter and/or embedding data frame to determine what should be displayed. This affects the UI directly and changes which data is displayed by the embedding plotter.
* Data selector panel - determines which subset of the data should be used in the model/display (ex. Type of cancer)

# Interactions
This diagram shows the flow for how a filter would be applied to the embedding plotter.
![Applying filter sequence diagram](./assets/filter-flow.png  "Filter sequence diagram")

This diagram shows the flow for how a new sample would be added to the embedding plotter. 
![Uploading sample sequence diagram](./assets/upload-flow.png  "Upload sequence diagram")
