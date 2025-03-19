# This markdown covers how we cleaned the data for the colon cancer dataset

We downloaded the "All cells tSNE dataset" and metadata and metatable from <https://singlecell.broadinstitute.org/single_cell/study/SCP1162/human-colon-cancer-atlas-c295#study-download>.

I then used a vlookup in excel to match the cell name from the tSNE data to the cell name in the metadata to add the important columns from the study to the tSNE data mappings. This will allow us to filter by these additional columns and have the tSNE plot of those cells.
