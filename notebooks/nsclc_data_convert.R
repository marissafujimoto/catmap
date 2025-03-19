# read dataframe into Seurat Object
refquery_final <- readRDS("~/Documents/Data 515/Course Project/Data/refquery_final.rds")
meta_data = refquery_final@meta.data

# convert predscores into dataframes
predscore_ct1_count = as.data.frame(as.matrix(refquery_final@assays[["prediction.score.celltypel1"]]@counts))
predscore_ct1_data = as.data.frame(as.matrix(refquery_final@assays[["prediction.score.celltypel1"]]@counts))
predscore_ct2_count = as.data.frame(as.matrix(refquery_final@assays[["prediction.score.celltypel2"]]@counts))
predscore_ct2_data = as.data.frame(as.matrix(refquery_final@assays[["prediction.score.celltypel2"]]@data))

# convert the study's mappings to dataframes so we can compare our model's
PCA_reduction = as.data.frame(refquery_final@reductions[["pca"]]@cell.embeddings)
umap_reduction = as.data.frame(refquery_final@reductions[["umap"]]@cell.embeddings)
umap_ref_reduction = as.data.frame(refquery_final@reductions[["umap.ref"]]@cell.embeddings)

# write csvs of the study's mappings so we can compare
write.csv(meta_data,"metadata.csv", row.names = TRUE)
write.csv(PCA_reduction,"pca_reduction.csv", row.names = TRUE)
write.csv(umap_reduction,"umap_reduction.csv", row.names = TRUE)
write.csv(umap_ref_reduction,"umap_ref_reduction.csv", row.names = TRUE)
table(Meta_data$Subtype)

# convert Seurat object to h5ad to use ScanPy
refquery_final_new = refquery_final
refquery_final_new[["RNA"]] <- as(object = refquery_final_new[["RNA"]], Class = "Assay")
SeuratDisk::SaveH5Seurat(refquery_final_new, "refquery_final_new.h5Seurat")
SeuratDisk::Convert("refquery_final_new.h5Seurat", dest = "h5ad")

#install required package to write the new object
remotes::install_github("pmbio/MuDataSeurat")

# write new h5ad object
library(MuDataSeurat)
WriteH5AD(refquery_final, "refquery_final.h5ad")
