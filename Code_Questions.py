'''
March 16 2019
Code to parse contents of a set of dataframes
'''

import pandas as pd
import numpy as np

BLCA = pd.read_csv(".../data/BLCA.data_mutations_extended.txt", sep='	')
BRCA = pd.read_csv(".../data/BRCA.data_mutations_extended.txt", sep='	')
CESC = pd.read_csv(".../data/CESC.data_mutations_extended.txt", sep='	')
GBM= pd.read_csv(".../data/GBM.data_mutations_extended.txt", sep='	')
HNSC = pd.read_csv(".../data/HNSC.data_mutations_extended.txt", sep='	')
KIRC = pd.read_csv(".../data/KIRC.data_mutations_extended.txt", sep='	')
KIRP = pd.read_csv(".../data/KIRP.data_mutations_extended.txt", sep='	')
LIHC = pd.read_csv(".../data/LIHC.data_mutations_extended.txt", sep='	')
LUAD = pd.read_csv(".../data/LUAD.data_mutations_extended.txt", sep='	')
LUSC = pd.read_csv(".../data/LUSC.data_mutations_extended.txt", sep='	')
OV = pd.read_csv(".../data/OV.data_mutations_extended.txt", sep='	')
PRAD = pd.read_csv(".../data/PRAD.data_mutations_extended.txt", sep='	')
SARC = pd.read_csv(".../data/SARC.data_mutations_extended.txt", sep='	')
SKCM = pd.read_csv(".../data/SKCM.data_mutations_extended.txt", sep='	')
STAD = pd.read_csv(".../data/STAD.data_mutations_extended.txt", sep='	')
THCA = pd.read_csv(".../data/THCA.data_mutations_extended.txt", sep='	')
UCEC = pd.read_csv(".../data/UCEC.data_mutations_extended.txt", sep='	')
LAML = pd.read_csv(".../data/LAML.data_mutations_extended.txt", sep='	')

samples = pd.read_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/scna_data/cell_lines/samples.csv")

BLCA.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
BRCA.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
CESC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
GBM.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
HNSC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
KIRC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
KIRP.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
LIHC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
LUAD.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
LUSC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
OV.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
PRAD.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
SARC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
SKCM.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
STAD.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
THCA.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)
UCEC.rename(columns={'Tumor_Sample_Barcode':'Samples'}, inplace=True)

BLCA['Samples'] = BLCA['Samples'].str[:-3]
BRCA['Samples'] = BRCA['Samples'].str[:-3]
CESC['Samples'] = CESC['Samples'].str[:-3]
GBM['Samples'] = GBM['Samples'].str[:-3]
HNSC['Samples'] = HNSC['Samples'].str[:-3]
KIRC['Samples'] = KIRC['Samples'].str[:-3]
KIRP['Samples'] = KIRP['Samples'].str[:-3]
LIHC['Samples'] = LIHC['Samples'].str[:-3]
LUAD['Samples'] = LUAD['Samples'].str[:-3]
LUSC['Samples'] = LUSC['Samples'].str[:-3]
OV['Samples'] = OV['Samples'].str[:-3]
PRAD['Samples'] = PRAD['Samples'].str[:-3]
SARC['Samples'] = SARC['Samples'].str[:-3]
SKCM['Samples'] = SKCM['Samples'].str[:-3]
STAD['Samples'] = STAD['Samples'].str[:-3]
THCA['Samples'] = THCA['Samples'].str[:-3]
UCEC['Samples'] = UCEC['Samples'].str[:-3]

BLCA = pd.merge(BLCA, samples, on="Samples")
BRCA = pd.merge(BRCA, samples, on="Samples")
CESC = pd.merge(CESC, samples, on="Samples")
GBM= pd.merge(GBM, samples, on="Samples")
HNSC = pd.merge(HNSC, samples, on="Samples")
KIRC = pd.merge(KIRC, samples, on="Samples")
KIRP = pd.merge(KIRP, samples, on="Samples")
LIHC = pd.merge(LIHC, samples, on="Samples")
LUAD = pd.merge(LUAD, samples, on="Samples")
LUSC = pd.merge(LUSC, samples, on="Samples")
OV = pd.merge(OV, samples, on="Samples")
PRAD = pd.merge(PRAD, samples, on="Samples")
SARC = pd.merge(SARC, samples, on="Samples")
SKCM = pd.merge(SKCM, samples, on="Samples")
STAD = pd.merge(STAD, samples, on="Samples")
THCA = pd.merge(THCA, samples, on="Samples")
UCEC = pd.merge(UCEC, samples, on="Samples")


# # BLCA has no scna TCGA sample name matchest
# BLCA.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/BLCA.data_mutations_extended.txt", sep='	', index=False)
# BRCA.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/BRCA.data_mutations_extended.txt", sep='	', index=False)
# CESC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/CESC.data_mutations_extended.txt", sep='	', index=False)
# GBM.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/GBM.data_mutations_extended.txt", sep='	', index=False)
# HNSC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/HNSC.data_mutations_extended.txt", sep='	', index=False)
# KIRC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/KIRC.data_mutations_extended.txt", sep='	', index=False)
# KIRP.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/KIRP.data_mutations_extended.txt", sep='	', index=False)
# LIHC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/LIHC.data_mutations_extended.txt", sep='	', index=False)
# LUAD.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/LUAD.data_mutations_extended.txt", sep='	', index=False)
# LUSC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/LUSC.data_mutations_extended.txt", sep='	', index=False)
# OV.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/OV.data_mutations_extended.txt", sep='	', index=False)
# PRAD.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/PRAD.data_mutations_extended.txt", sep='	', index=False)
# SARC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/SARC.data_mutations_extended.txt", sep='	', index=False)
# SKCM.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/SKCM.data_mutations_extended.txt", sep='	', index=False)
# STAD.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/STAD.data_mutations_extended.txt", sep='	', index=False)
# THCA.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/THCA.data_mutations_extended.txt", sep='	', index=False)
# UCEC.to_csv("/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/tumor_tissue4/UCEC.data_mutations_extended.txt", sep='	', index=False)

# Parse PolyPhen and SIFT columns to list deleterious/benign and score separately
BLCA['PolyPhen'] = BLCA['PolyPhen'].astype(str).str[:-1]
BRCA['PolyPhen'] = BRCA['PolyPhen'].astype(str).str[:-1]
CESC['PolyPhen'] = CESC['PolyPhen'].astype(str).str[:-1]
GBM['PolyPhen'] = GBM['PolyPhen'].astype(str).str[:-1]
HNSC['PolyPhen'] = HNSC['PolyPhen'].astype(str).str[:-1]
KIRC['PolyPhen'] = KIRC['PolyPhen'].astype(str).str[:-1]
KIRP['PolyPhen'] = KIRP['PolyPhen'].astype(str).str[:-1]
LIHC['PolyPhen'] = LIHC['PolyPhen'].astype(str).str[:-1]
LUAD['PolyPhen'] = LUAD['PolyPhen'].astype(str).str[:-1]
LUSC['PolyPhen'] = LUSC['PolyPhen'].astype(str).str[:-1]
OV['PolyPhen'] = OV['PolyPhen'].astype(str).str[:-1]
PRAD['PolyPhen'] = PRAD['PolyPhen'].astype(str).str[:-1]
SARC['PolyPhen'] = SARC['PolyPhen'].astype(str).str[:-1]
SKCM['PolyPhen'] = SKCM['PolyPhen'].astype(str).str[:-1]
STAD['PolyPhen'] = STAD['PolyPhen'].astype(str).str[:-1]
THCA['PolyPhen'] = THCA['PolyPhen'].astype(str).str[:-1]
UCEC['PolyPhen'] = UCEC['PolyPhen'].astype(str).str[:-1]

BRCA[['PolyPhen','PolyPhen_Probability']] = BRCA['PolyPhen'].str.split('(',expand=True)
BLCA[['PolyPhen','PolyPhen_Probability']] = BLCA['PolyPhen'].str.split('(',expand=True)
CESC[['PolyPhen','PolyPhen_Probability']] = CESC['PolyPhen'].str.split('(',expand=True)
GBM[['PolyPhen','PolyPhen_Probability']] = GBM['PolyPhen'].str.split('(',expand=True)
HNSC[['PolyPhen','PolyPhen_Probability']] = HNSC['PolyPhen'].str.split('(',expand=True)
KIRC[['PolyPhen','PolyPhen_Probability']] = KIRC['PolyPhen'].str.split('(',expand=True)
KIRP[['PolyPhen','PolyPhen_Probability']] = KIRP['PolyPhen'].str.split('(',expand=True)
LIHC[['PolyPhen','PolyPhen_Probability']] = LIHC['PolyPhen'].str.split('(',expand=True)
LUAD[['PolyPhen','PolyPhen_Probability']] = LUAD['PolyPhen'].str.split('(',expand=True)
LUSC[['PolyPhen','PolyPhen_Probability']] = LUSC['PolyPhen'].str.split('(',expand=True)
OV[['PolyPhen','PolyPhen_Probability']] = OV['PolyPhen'].str.split('(',expand=True)
PRAD[['PolyPhen','PolyPhen_Probability']] = PRAD['PolyPhen'].str.split('(',expand=True)
SARC[['PolyPhen','PolyPhen_Probability']] = SARC['PolyPhen'].str.split('(',expand=True)
SKCM[['PolyPhen','PolyPhen_Probability']] = SKCM['PolyPhen'].str.split('(',expand=True)
STAD[['PolyPhen','PolyPhen_Probability']] = STAD['PolyPhen'].str.split('(',expand=True)
THCA[['PolyPhen','PolyPhen_Probability']] = THCA['PolyPhen'].str.split('(',expand=True)
UCEC[['PolyPhen','PolyPhen_Probability']] = UCEC['PolyPhen'].str.split('(',expand=True)

BRCA['PolyPhen'] = BRCA['PolyPhen'].str.replace('[', '')
BLCA['PolyPhen'] = BLCA['PolyPhen'].str.replace('[', '')
CESC['PolyPhen'] = CESC['PolyPhen'].str.replace('[', '')
GBM['PolyPhen'] = GBM['PolyPhen'].str.replace('[', '')
HNSC['PolyPhen'] = HNSC['PolyPhen'].str.replace('[', '')
KIRC['PolyPhen'] = KIRC['PolyPhen'].str.replace('[', '')
KIRP['PolyPhen'] = KIRP['PolyPhen'].str.replace('[', '')
LIHC['PolyPhen'] = LIHC['PolyPhen'].str.replace('[', '')
LUAD['PolyPhen'] = LUAD['PolyPhen'].str.replace('[', '')
LUSC['PolyPhen'] = LUSC['PolyPhen'].str.replace('[', '')
OV['PolyPhen'] = OV['PolyPhen'].str.replace('[', '')
PRAD['PolyPhen'] = PRAD['PolyPhen'].str.replace('[', '')
SARC['PolyPhen'] = SARC['PolyPhen'].str.replace('[', '')
SKCM['PolyPhen'] = SKCM['PolyPhen'].str.replace('[', '')
STAD['PolyPhen'] = STAD['PolyPhen'].str.replace('[', '')
THCA['PolyPhen'] = THCA['PolyPhen'].str.replace('[', '')
UCEC['PolyPhen'] = UCEC['PolyPhen'].str.replace('[', '')

BLCA['SIFT'] = BLCA['SIFT'].astype(str).str[:-1]
BRCA['SIFT'] = BRCA['SIFT'].astype(str).str[:-1]
CESC['SIFT'] = CESC['SIFT'].astype(str).str[:-1]
GBM['SIFT'] = GBM['SIFT'].astype(str).str[:-1]
HNSC['SIFT'] = HNSC['SIFT'].astype(str).str[:-1]
KIRC['SIFT'] = KIRC['SIFT'].astype(str).str[:-1]
KIRP['SIFT'] = KIRP['SIFT'].astype(str).str[:-1]
LIHC['SIFT'] = LIHC['SIFT'].astype(str).str[:-1]
LUAD['SIFT'] = LUAD['SIFT'].astype(str).str[:-1]
LUSC['SIFT'] = LUSC['SIFT'].astype(str).str[:-1]
OV['SIFT'] = OV['SIFT'].astype(str).str[:-1]
PRAD['SIFT'] = PRAD['SIFT'].astype(str).str[:-1]
SARC['SIFT'] = SARC['SIFT'].astype(str).str[:-1]
SKCM['SIFT'] = SKCM['SIFT'].astype(str).str[:-1]
STAD['SIFT'] = STAD['SIFT'].astype(str).str[:-1]
THCA['SIFT'] = THCA['SIFT'].astype(str).str[:-1]
UCEC['SIFT'] = UCEC['SIFT'].astype(str).str[:-1]

BRCA[['SIFT','SIFT_Probability']] = BRCA['SIFT'].str.split('(',expand=True)
BLCA[['SIFT','SIFT_Probability']] = BLCA['SIFT'].str.split('(',expand=True)
CESC[['SIFT','SIFT_Probability']] = CESC['SIFT'].str.split('(',expand=True)
GBM[['SIFT','SIFT_Probability']] = GBM['SIFT'].str.split('(',expand=True)
HNSC[['SIFT','SIFT_Probability']] = HNSC['SIFT'].str.split('(',expand=True)
KIRC[['SIFT','SIFT_Probability']] = KIRC['SIFT'].str.split('(',expand=True)
KIRP[['SIFT','SIFT_Probability']] = KIRP['SIFT'].str.split('(',expand=True)
LIHC[['SIFT','SIFT_Probability']] = LIHC['SIFT'].str.split('(',expand=True)
LUAD[['SIFT','SIFT_Probability']] = LUAD['SIFT'].str.split('(',expand=True)
LUSC[['SIFT','SIFT_Probability']] = LUSC['SIFT'].str.split('(',expand=True)
OV[['SIFT','SIFT_Probability']] = OV['SIFT'].str.split('(',expand=True)
PRAD[['SIFT','SIFT_Probability']] = PRAD['SIFT'].str.split('(',expand=True)
SARC[['SIFT','SIFT_Probability']] = SARC['SIFT'].str.split('(',expand=True)
SKCM[['SIFT','SIFT_Probability']] = SKCM['SIFT'].str.split('(',expand=True)
STAD[['SIFT','SIFT_Probability']] = STAD['SIFT'].str.split('(',expand=True)
THCA[['SIFT','SIFT_Probability']] = THCA['SIFT'].str.split('(',expand=True)
UCEC[['SIFT','SIFT_Probability']] = UCEC['SIFT'].str.split('(',expand=True)

BRCA['SIFT'] = BRCA['SIFT'].str.replace('[', '')
BLCA['SIFT'] = BLCA['SIFT'].str.replace('[', '')
CESC['SIFT'] = CESC['SIFT'].str.replace('[', '')
GBM['SIFT'] = GBM['SIFT'].str.replace('[', '')
HNSC['SIFT'] = HNSC['SIFT'].str.replace('[', '')
KIRC['SIFT'] = KIRC['SIFT'].str.replace('[', '')
KIRP['SIFT'] = KIRP['SIFT'].str.replace('[', '')
LIHC['SIFT'] = LIHC['SIFT'].str.replace('[', '')
LUAD['SIFT'] = LUAD['SIFT'].str.replace('[', '')
LUSC['SIFT'] = LUSC['SIFT'].str.replace('[', '')
OV['SIFT'] = OV['SIFT'].str.replace('[', '')
PRAD['SIFT'] = PRAD['SIFT'].str.replace('[', '')
SARC['SIFT'] = SARC['SIFT'].str.replace('[', '')
SKCM['SIFT'] = SKCM['SIFT'].str.replace('[', '')
STAD['SIFT'] = STAD['SIFT'].str.replace('[', '')
THCA['SIFT'] = THCA['SIFT'].str.replace('[', '')
UCEC['SIFT'] = UCEC['SIFT'].str.replace('[', '')

#Find total number of unique samples in the dataframe

BRCA_total_samples = BRCA['Samples'].nunique()
BLCA_total_samples = BLCA['Samples'].nunique()
CESC_total_samples = CESC['Samples'].nunique()
GBM_total_samples = GBM['Samples'].nunique()
HNSC_total_samples = HNSC['Samples'].nunique()
KIRC_total_samples = KIRC['Samples'].nunique()
KIRP_total_samples = KIRP['Samples'].nunique()
LIHC_total_samples = LIHC['Samples'].nunique()
LUAD_total_samples = LUAD['Samples'].nunique()
LUSC_total_samples = LUSC['Samples'].nunique()
OV_total_samples = OV['Samples'].nunique()
PRAD_total_samples = PRAD['Samples'].nunique()
SARC_total_samples = SARC['Samples'].nunique()
SKCM_total_samples = SKCM['Samples'].nunique()
STAD_total_samples = STAD['Samples'].nunique()
THCA_total_samples = THCA['Samples'].nunique()
UCEC_total_samples = UCEC['Samples'].nunique()


#Select ATRX and DAXX deleterious mutations
select_ATRX_BRCA = (((BRCA['PolyPhen_Probability'].astype(float) > 0.84) & (BRCA['PolyPhen'] == 'probably_damaging')) | ((BRCA['SIFT_Probability'].astype(float) < 0.6) & (BRCA['SIFT'] == 'deleterious'))) & (BRCA['Hugo_Symbol'] == 'ATRX')
select_ATRX_CESC = (((CESC['PolyPhen_Probability'].astype(float) > 0.84) & (CESC['PolyPhen'] == 'probably_damaging')) | ((CESC['SIFT_Probability'].astype(float) < 0.6) & (CESC['SIFT'] == 'deleterious'))) & (CESC['Hugo_Symbol'] == 'ATRX')
select_ATRX_GBM = (((GBM['PolyPhen_Probability'].astype(float) > 0.84) & (GBM['PolyPhen'] == 'probably_damaging')) | ((GBM['SIFT_Probability'].astype(float) < 0.6) & (GBM['SIFT'] == 'deleterious'))) & (GBM['Hugo_Symbol'] == 'ATRX')
select_ATRX_HNSC = (((HNSC['PolyPhen_Probability'].astype(float) > 0.84) & (HNSC['PolyPhen'] == 'probably_damaging')) | ((HNSC['SIFT_Probability'].astype(float) < 0.6) & (HNSC['SIFT'] == 'deleterious'))) & (HNSC['Hugo_Symbol'] == 'ATRX')
select_ATRX_KIRC = (((KIRC['PolyPhen_Probability'].astype(float) > 0.84) & (KIRC['PolyPhen'] == 'probably_damaging')) | ((KIRC['SIFT_Probability'].astype(float) < 0.6) & (KIRC['SIFT'] == 'deleterious'))) & (KIRC['Hugo_Symbol'] == 'ATRX')
select_ATRX_KIRP = (((KIRP['PolyPhen_Probability'].astype(float) > 0.84) & (KIRP['PolyPhen'] == 'probably_damaging')) | ((KIRP['SIFT_Probability'].astype(float) < 0.6) & (KIRP['SIFT'] == 'deleterious'))) & (KIRP['Hugo_Symbol'] == 'ATRX')
select_ATRX_LIHC = (((LIHC['PolyPhen_Probability'].astype(float) > 0.84) & (LIHC['PolyPhen'] == 'probably_damaging')) | ((LIHC['SIFT_Probability'].astype(float) < 0.6) & (LIHC['SIFT'] == 'deleterious'))) & (LIHC['Hugo_Symbol'] == 'ATRX')
select_ATRX_LUAD = (((LUAD['PolyPhen_Probability'].astype(float) > 0.84) & (LUAD['PolyPhen'] == 'probably_damaging')) | ((LUAD['SIFT_Probability'].astype(float) < 0.6) & (LUAD['SIFT'] == 'deleterious'))) & (LUAD['Hugo_Symbol'] == 'ATRX')
select_ATRX_LUSC = (((LUSC['PolyPhen_Probability'].astype(float) > 0.84) & (LUSC['PolyPhen'] == 'probably_damaging')) | ((LUSC['SIFT_Probability'].astype(float) < 0.6) & (LUSC['SIFT'] == 'deleterious'))) & (LUSC['Hugo_Symbol'] == 'ATRX')
select_ATRX_OV = (((OV['PolyPhen_Probability'].astype(float) > 0.84) & (OV['PolyPhen'] == 'probably_damaging')) | ((OV['SIFT_Probability'].astype(float) < 0.6) & (OV['SIFT'] == 'deleterious'))) & (OV['Hugo_Symbol'] == 'ATRX')
select_ATRX_PRAD = (((PRAD['PolyPhen_Probability'].astype(float) > 0.84) & (PRAD['PolyPhen'] == 'probably_damaging')) | ((PRAD['SIFT_Probability'].astype(float) < 0.6) & (PRAD['SIFT'] == 'deleterious'))) & (PRAD['Hugo_Symbol'] == 'ATRX')
select_ATRX_SARC = (((SARC['PolyPhen_Probability'].astype(float) > 0.84) & (SARC['PolyPhen'] == 'probably_damaging')) | ((SARC['SIFT_Probability'].astype(float) < 0.6) & (SARC['SIFT'] == 'deleterious'))) & (SARC['Hugo_Symbol'] == 'ATRX')
select_ATRX_SKCM = (((SKCM['PolyPhen_Probability'].astype(float) > 0.84) & (SKCM['PolyPhen'] == 'probably_damaging')) | ((SKCM['SIFT_Probability'].astype(float) < 0.6) & (SKCM['SIFT'] == 'deleterious'))) & (SKCM['Hugo_Symbol'] == 'ATRX')
select_ATRX_STAD = (((STAD['PolyPhen_Probability'].astype(float) > 0.84) & (STAD['PolyPhen'] == 'probably_damaging')) | ((STAD['SIFT_Probability'].astype(float) < 0.6) & (STAD['SIFT'] == 'deleterious'))) & (STAD['Hugo_Symbol'] == 'ATRX')
select_ATRX_THCA = (((THCA['PolyPhen_Probability'].astype(float) > 0.84) & (THCA['PolyPhen'] == 'probably_damaging')) | ((THCA['SIFT_Probability'].astype(float) < 0.6) & (THCA['SIFT'] == 'deleterious'))) & (THCA['Hugo_Symbol'] == 'ATRX')
select_ATRX_UCEC = (((UCEC['PolyPhen_Probability'].astype(float) > 0.84) & (UCEC['PolyPhen'] == 'probably_damaging')) | ((UCEC['SIFT_Probability'].astype(float) < 0.6) & (UCEC['SIFT'] == 'deleterious'))) & (UCEC['Hugo_Symbol'] == 'ATRX')
select_ATRX_BLCA = (((BLCA['PolyPhen_Probability'].astype(float) > 0.84) & (BLCA['PolyPhen'] == 'probably_damaging')) | ((BLCA['SIFT_Probability'].astype(float) < 0.6) & (BLCA['SIFT'] == 'deleterious'))) & (BLCA['Hugo_Symbol'] == 'ATRX')

select_DAXX_BLCA = (((BLCA['PolyPhen_Probability'].astype(float) > 0.84) & (BLCA['PolyPhen'] == 'probably_damaging')) | ((BLCA['SIFT_Probability'].astype(float) < 0.6) & (BLCA['SIFT'] == 'deleterious'))) & (BLCA['Hugo_Symbol'] == 'DAXX')
select_DAXX_BRCA = (((BRCA['PolyPhen_Probability'].astype(float) > 0.84) & (BRCA['PolyPhen'] == 'probably_damaging')) | ((BRCA['SIFT_Probability'].astype(float) < 0.6) & (BRCA['SIFT'] == 'deleterious'))) & (BRCA['Hugo_Symbol'] == 'DAXX')
select_DAXX_CESC = (((CESC['PolyPhen_Probability'].astype(float) > 0.84) & (CESC['PolyPhen'] == 'probably_damaging')) | ((CESC['SIFT_Probability'].astype(float) < 0.6) & (CESC['SIFT'] == 'deleterious'))) & (CESC['Hugo_Symbol'] == 'DAXX')
select_DAXX_GBM = (((GBM['PolyPhen_Probability'].astype(float) > 0.84) & (GBM['PolyPhen'] == 'probably_damaging')) | ((GBM['SIFT_Probability'].astype(float) < 0.6) & (GBM['SIFT'] == 'deleterious'))) & (GBM['Hugo_Symbol'] == 'DAXX')
select_DAXX_HNSC = (((HNSC['PolyPhen_Probability'].astype(float) > 0.84) & (HNSC['PolyPhen'] == 'probably_damaging')) | ((HNSC['SIFT_Probability'].astype(float) < 0.6) & (HNSC['SIFT'] == 'deleterious'))) & (HNSC['Hugo_Symbol'] == 'DAXX')
select_DAXX_KIRC = (((KIRC['PolyPhen_Probability'].astype(float) > 0.84) & (KIRC['PolyPhen'] == 'probably_damaging')) | ((KIRC['SIFT_Probability'].astype(float) < 0.6) & (KIRC['SIFT'] == 'deleterious'))) & (KIRC['Hugo_Symbol'] == 'DAXX')
select_DAXX_KIRP = (((KIRP['PolyPhen_Probability'].astype(float) > 0.84) & (KIRP['PolyPhen'] == 'probably_damaging')) | ((KIRP['SIFT_Probability'].astype(float) < 0.6) & (KIRP['SIFT'] == 'deleterious'))) & (KIRP['Hugo_Symbol'] == 'DAXX')
select_DAXX_LIHC = (((LIHC['PolyPhen_Probability'].astype(float) > 0.84) & (LIHC['PolyPhen'] == 'probably_damaging')) | ((LIHC['SIFT_Probability'].astype(float) < 0.6) & (LIHC['SIFT'] == 'deleterious'))) & (LIHC['Hugo_Symbol'] == 'DAXX')
select_DAXX_LUAD = (((LUAD['PolyPhen_Probability'].astype(float) > 0.84) & (LUAD['PolyPhen'] == 'probably_damaging')) | ((LUAD['SIFT_Probability'].astype(float) < 0.6) & (LUAD['SIFT'] == 'deleterious'))) & (LUAD['Hugo_Symbol'] == 'DAXX')
select_DAXX_LUSC = (((LUSC['PolyPhen_Probability'].astype(float) > 0.84) & (LUSC['PolyPhen'] == 'probably_damaging')) | ((LUSC['SIFT_Probability'].astype(float) < 0.6) & (LUSC['SIFT'] == 'deleterious'))) & (LUSC['Hugo_Symbol'] == 'DAXX')
select_DAXX_OV = (((OV['PolyPhen_Probability'].astype(float) > 0.84) & (OV['PolyPhen'] == 'probably_damaging')) | ((OV['SIFT_Probability'].astype(float) < 0.6) & (OV['SIFT'] == 'deleterious'))) & (OV['Hugo_Symbol'] == 'DAXX')
select_DAXX_PRAD = (((PRAD['PolyPhen_Probability'].astype(float) > 0.84) & (PRAD['PolyPhen'] == 'probably_damaging')) | ((PRAD['SIFT_Probability'].astype(float) < 0.6) & (PRAD['SIFT'] == 'deleterious'))) & (PRAD['Hugo_Symbol'] == 'DAXX')
select_DAXX_SARC = (((SARC['PolyPhen_Probability'].astype(float) > 0.84) & (SARC['PolyPhen'] == 'probably_damaging')) | ((SARC['SIFT_Probability'].astype(float) < 0.6) & (SARC['SIFT'] == 'deleterious'))) & (SARC['Hugo_Symbol'] == 'DAXX')
select_DAXX_SKCM = (((SKCM['PolyPhen_Probability'].astype(float) > 0.84) & (SKCM['PolyPhen'] == 'probably_damaging')) | ((SKCM['SIFT_Probability'].astype(float) < 0.6) & (SKCM['SIFT'] == 'deleterious'))) & (SKCM['Hugo_Symbol'] == 'DAXX')
select_DAXX_STAD = (((STAD['PolyPhen_Probability'].astype(float) > 0.84) & (STAD['PolyPhen'] == 'probably_damaging')) | ((STAD['SIFT_Probability'].astype(float) < 0.6) & (STAD['SIFT'] == 'deleterious'))) & (STAD['Hugo_Symbol'] == 'DAXX')
select_DAXX_THCA = (((THCA['PolyPhen_Probability'].astype(float) > 0.84) & (THCA['PolyPhen'] == 'probably_damaging')) | ((THCA['SIFT_Probability'].astype(float) < 0.6) & (THCA['SIFT'] == 'deleterious'))) & (THCA['Hugo_Symbol'] == 'DAXX')
select_DAXX_UCEC = (((UCEC['PolyPhen_Probability'].astype(float) > 0.84) & (UCEC['PolyPhen'] == 'probably_damaging')) | ((UCEC['SIFT_Probability'].astype(float) < 0.6) & (UCEC['SIFT'] == 'deleterious'))) & (UCEC['Hugo_Symbol'] == 'DAXX')

print(BRCA.head(3))
BLCA['BLCA_Delet_Mut_ATRX'] = np.where(select_ATRX_BLCA, '1', '0')
BRCA['BRCA_Delet_Mut_ATRX'] = np.where(select_ATRX_BRCA, '1', '0')
CESC['CESC_Delet_Mut_ATRX'] = np.where(select_ATRX_CESC, '1', '0')
GBM['GBM_Delet_Mut_ATRX'] = np.where(select_ATRX_GBM, '1', '0')
HNSC['HNSC_Delet_Mut_ATRX'] = np.where(select_ATRX_HNSC, '1', '0')
KIRC['KIRC_Delet_Mut_ATRX'] = np.where(select_ATRX_KIRC, '1', '0')
KIRP['KIRP_Delet_Mut_ATRX'] = np.where(select_ATRX_KIRP, '1', '0')
LIHC['LIHC_Delet_Mut_ATRX'] = np.where(select_ATRX_LIHC, '1', '0')
LUAD['LUAD_Delet_Mut_ATRX'] = np.where(select_ATRX_LUAD, '1', '0')
LUSC['LUSC_Delet_Mut_ATRX'] = np.where(select_ATRX_LUSC, '1', '0')
OV['OV_Delet_Mut_ATRX'] = np.where(select_ATRX_OV, '1', '0')
PRAD['PRAD_Delet_Mut_ATRX'] = np.where(select_ATRX_PRAD, '1', '0')
SARC['SARC_Delet_Mut_ATRX'] = np.where(select_ATRX_SARC, '1', '0')
SKCM['SKCM_Delet_Mut_ATRX'] = np.where(select_ATRX_SKCM, '1', '0')
STAD['STAD_Delet_Mut_ATRX'] = np.where(select_ATRX_STAD, '1', '0')
THCA['THCA_Delet_Mut_ATRX'] = np.where(select_ATRX_THCA, '1', '0')
UCEC['UCEC_Delet_Mut_ATRX'] = np.where(select_ATRX_UCEC, '1', '0')

BRCA['BRCA_Delet_Mut_DAXX'] = np.where(select_DAXX_BRCA, '1', '0')
BLCA['BLCA_Delet_Mut_DAXX'] = np.where(select_DAXX_BLCA, '1', '0')
CESC['CESC_Delet_Mut_DAXX'] = np.where(select_DAXX_CESC, '1', '0')
GBM['GBM_Delet_Mut_DAXX'] = np.where(select_DAXX_GBM, '1', '0')
HNSC['HNSC_Delet_Mut_DAXX'] = np.where(select_DAXX_HNSC, '1', '0')
KIRC['KIRC_Delet_Mut_DAXX'] = np.where(select_DAXX_KIRC, '1', '0')
KIRP['KIRP_Delet_Mut_DAXX'] = np.where(select_DAXX_KIRP, '1', '0')
LIHC['LIHC_Delet_Mut_DAXX'] = np.where(select_DAXX_LIHC, '1', '0')
LUAD['LUAD_Delet_Mut_DAXX'] = np.where(select_DAXX_LUAD, '1', '0')
LUSC['LUSC_Delet_Mut_DAXX'] = np.where(select_DAXX_LUSC, '1', '0')
OV['OV_Delet_Mut_DAXX'] = np.where(select_DAXX_OV, '1', '0')
PRAD['PRAD_Delet_Mut_DAXX'] = np.where(select_DAXX_PRAD, '1', '0')
SARC['SARC_Delet_Mut_DAXX'] = np.where(select_DAXX_SARC, '1', '0')
SKCM['SKCM_Delet_Mut_DAXX'] = np.where(select_DAXX_SKCM, '1', '0')
STAD['STAD_Delet_Mut_DAXX'] = np.where(select_DAXX_STAD, '1', '0')
THCA['THCA_Delet_Mut_DAXX'] = np.where(select_DAXX_THCA, '1', '0')
UCEC['UCEC_Delet_Mut_DAXX'] = np.where(select_DAXX_UCEC, '1', '0')

BRCA_ATRX_select = BRCA[BRCA['BRCA_Delet_Mut_ATRX'].str.contains('1')]
BLCA_ATRX_select = BLCA[BLCA['BLCA_Delet_Mut_ATRX'].str.contains('1')]
CESC_ATRX_select = CESC[CESC['CESC_Delet_Mut_ATRX'].str.contains('1')]
GBM_ATRX_select = GBM[GBM['GBM_Delet_Mut_ATRX'].str.contains('1')]
HNSC_ATRX_select = HNSC[HNSC['HNSC_Delet_Mut_ATRX'].str.contains('1')]
KIRC_ATRX_select = KIRC[KIRC['KIRC_Delet_Mut_ATRX'].str.contains('1')]
KIRP_ATRX_select = KIRP[KIRP['KIRP_Delet_Mut_ATRX'].str.contains('1')]
LIHC_ATRX_select = LIHC[LIHC['LIHC_Delet_Mut_ATRX'].str.contains('1')]
LUAD_ATRX_select = LUAD[LUAD['LUAD_Delet_Mut_ATRX'].str.contains('1')]
LUSC_ATRX_select = LUSC[LUSC['LUSC_Delet_Mut_ATRX'].str.contains('1')]
OV_ATRX_select = OV[OV['OV_Delet_Mut_ATRX'].str.contains('1')]
PRAD_ATRX_select = PRAD[PRAD['PRAD_Delet_Mut_ATRX'].str.contains('1')]
SARC_ATRX_select = SARC[SARC['SARC_Delet_Mut_ATRX'].str.contains('1')]
SKCM_ATRX_select = SKCM[SKCM['SKCM_Delet_Mut_ATRX'].str.contains('1')]
STAD_ATRX_select = STAD[STAD['STAD_Delet_Mut_ATRX'].str.contains('1')]
THCA_ATRX_select = THCA[THCA['THCA_Delet_Mut_ATRX'].str.contains('1')]
UCEC_ATRX_select = UCEC[UCEC['UCEC_Delet_Mut_ATRX'].str.contains('1')]

BRCA_DAXX_select = BRCA[BRCA['BRCA_Delet_Mut_DAXX'].str.contains('1')]
BLCA_DAXX_select = BLCA[BLCA['BLCA_Delet_Mut_DAXX'].str.contains('1')]
CESC_DAXX_select = CESC[CESC['CESC_Delet_Mut_DAXX'].str.contains('1')]
GBM_DAXX_select = GBM[GBM['GBM_Delet_Mut_DAXX'].str.contains('1')]
HNSC_DAXX_select = HNSC[HNSC['HNSC_Delet_Mut_DAXX'].str.contains('1')]
KIRC_DAXX_select = KIRC[KIRC['KIRC_Delet_Mut_DAXX'].str.contains('1')]
KIRP_DAXX_select = KIRP[KIRP['KIRP_Delet_Mut_DAXX'].str.contains('1')]
LIHC_DAXX_select = LIHC[LIHC['LIHC_Delet_Mut_DAXX'].str.contains('1')]
LUAD_DAXX_select = LUAD[LUAD['LUAD_Delet_Mut_DAXX'].str.contains('1')]
LUSC_DAXX_select = LUSC[LUSC['LUSC_Delet_Mut_DAXX'].str.contains('1')]
OV_DAXX_select = OV[OV['OV_Delet_Mut_DAXX'].str.contains('1')]
PRAD_DAXX_select = PRAD[PRAD['PRAD_Delet_Mut_DAXX'].str.contains('1')]
SARC_DAXX_select = SARC[SARC['SARC_Delet_Mut_DAXX'].str.contains('1')]
SKCM_DAXX_select = SKCM[SKCM['SKCM_Delet_Mut_DAXX'].str.contains('1')]
STAD_DAXX_select = STAD[STAD['STAD_Delet_Mut_DAXX'].str.contains('1')]
THCA_DAXX_select = THCA[THCA['THCA_Delet_Mut_DAXX'].str.contains('1')]
UCEC_DAXX_select = UCEC[UCEC['UCEC_Delet_Mut_DAXX'].str.contains('1')]

print('BRCA',BRCA_ATRX_select.shape)
print('BLCA',BLCA_ATRX_select.shape)
print('CESC', CESC_ATRX_select.shape)
print('GBM',GBM_ATRX_select.shape)
print('HNSC',HNSC_ATRX_select.shape)
print('KIRC',KIRC_ATRX_select.shape)
print('KIRP',KIRP_ATRX_select.shape)
print('LIHC',LIHC_ATRX_select.shape)
print('LUAD',LUAD_ATRX_select.shape)
print('LUSC',LUSC_ATRX_select.shape)
print('OV',OV_ATRX_select.shape)
print('PRAD',PRAD_ATRX_select.shape)
print('SARC',SARC_ATRX_select.shape)
print('SKCM',SKCM_ATRX_select.shape)
print('STAD',STAD_ATRX_select.shape)
print('THCA',THCA_ATRX_select.shape)
print('UCEC',UCEC_ATRX_select.shape)

BRCA_DAXX_select = BRCA[BRCA['BRCA_Delet_Mut_DAXX'].str.contains('1')]
BLCA_DAXX_select = BLCA[BLCA['BLCA_Delet_Mut_DAXX'].str.contains('1')]
CESC_DAXX_select = CESC[CESC['CESC_Delet_Mut_DAXX'].str.contains('1')]
GBM_DAXX_select = GBM[GBM['GBM_Delet_Mut_DAXX'].str.contains('1')]
HNSC_DAXX_select = HNSC[HNSC['HNSC_Delet_Mut_DAXX'].str.contains('1')]
KIRC_DAXX_select = KIRC[KIRC['KIRC_Delet_Mut_DAXX'].str.contains('1')]
KIRP_DAXX_select = KIRP[KIRP['KIRP_Delet_Mut_DAXX'].str.contains('1')]
LIHC_DAXX_select = LIHC[LIHC['LIHC_Delet_Mut_DAXX'].str.contains('1')]
LUAD_DAXX_select = LUAD[LUAD['LUAD_Delet_Mut_DAXX'].str.contains('1')]
LUSC_DAXX_select = LUSC[LUSC['LUSC_Delet_Mut_DAXX'].str.contains('1')]
OV_DAXX_select = OV[OV['OV_Delet_Mut_DAXX'].str.contains('1')]
PRAD_DAXX_select = PRAD[PRAD['PRAD_Delet_Mut_DAXX'].str.contains('1')]
SARC_DAXX_select = SARC[SARC['SARC_Delet_Mut_DAXX'].str.contains('1')]
SKCM_DAXX_select = SKCM[SKCM['SKCM_Delet_Mut_DAXX'].str.contains('1')]
STAD_DAXX_select = STAD[STAD['STAD_Delet_Mut_DAXX'].str.contains('1')]
THCA_DAXX_select = THCA[THCA['THCA_Delet_Mut_DAXX'].str.contains('1')]
UCEC_DAXX_select = UCEC[UCEC['UCEC_Delet_Mut_DAXX'].str.contains('1')]

print('BRCA',BRCA_DAXX_select.shape)
print('BLCA',BLCA_DAXX_select.shape)
print('CESC', CESC_DAXX_select.shape)
print('GBM',GBM_DAXX_select.shape)
print('HNSC',HNSC_DAXX_select.shape)
print('KIRC',KIRC_DAXX_select.shape)
print('KIRP',KIRP_DAXX_select.shape)
print('LIHC',LIHC_DAXX_select.shape)
print('LUAD',LUAD_DAXX_select.shape)
print('LUSC',LUSC_DAXX_select.shape)
print('OV',OV_DAXX_select.shape)
print('PRAD',PRAD_DAXX_select.shape)
print('SARC',SARC_DAXX_select.shape)
print('SKCM',SKCM_DAXX_select.shape)
print('STAD',STAD_DAXX_select.shape)
print('THCA',THCA_DAXX_select.shape)
print('UCEC',UCEC_DAXX_select.shape)

# These are the tissue types that contain deleterious DAXX or ATRX mutation
BLCA_ATRX_select_count = BLCA_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
BRCA_ATRX_select_count = BRCA_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
CESC_ATRX_select_count = CESC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
GBM_ATRX_select_count = GBM_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
HNSC_ATRX_select_count = HNSC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
KIRC_ATRX_select_count = KIRC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
KIRP_ATRX_select_count = KIRP_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
LIHC_ATRX_select_count = LIHC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
LUAD_ATRX_select_count = LUAD_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
LUSC_ATRX_select_count = LUSC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
PRAD_ATRX_select_count = PRAD_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
SARC_ATRX_select_count = SARC_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
SKCM_ATRX_select_count = SKCM_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
STAD_ATRX_select_count = STAD_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])
THCA_ATRX_select_count = THCA_ATRX_select.groupby(['Samples'], as_index=False).agg(['count'])

BLCA_DAXX_select_count = BLCA_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
GBM_DAXX_select_count = GBM_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
HNSC_DAXX_select_count = HNSC_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
KIRC_DAXX_select_count = KIRC_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
LIHC_DAXX_select_count = LIHC_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
LUAD_DAXX_select_count = LUAD_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
LUSC_DAXX_select_count = LUSC_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
SKCM_DAXX_select_count = SKCM_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])
STAD_DAXX_select_count = STAD_DAXX_select.groupby(['Samples'], as_index=False).agg(['count'])

BLCA_ATRX_select_count.reset_index(inplace=True)
BRCA_ATRX_select_count.reset_index(inplace=True)
CESC_ATRX_select_count.reset_index(inplace=True)
GBM_ATRX_select_count.reset_index(inplace=True)
HNSC_ATRX_select_count.reset_index(inplace=True)
KIRC_ATRX_select_count.reset_index(inplace=True)
KIRP_ATRX_select_count.reset_index(inplace=True)
LIHC_ATRX_select_count.reset_index(inplace=True)
LUAD_ATRX_select_count.reset_index(inplace=True)
LUSC_ATRX_select_count.reset_index(inplace=True)
PRAD_ATRX_select_count.reset_index(inplace=True)
SARC_ATRX_select_count.reset_index(inplace=True)
SKCM_ATRX_select_count.reset_index(inplace=True)
STAD_ATRX_select_count.reset_index(inplace=True)
THCA_ATRX_select_count.reset_index(inplace=True)
BLCA_DAXX_select_count.reset_index(inplace=True)
GBM_DAXX_select_count.reset_index(inplace=True)
HNSC_DAXX_select_count.reset_index(inplace=True)
KIRC_DAXX_select_count.reset_index(inplace=True)
LIHC_DAXX_select_count.reset_index(inplace=True)
LUAD_DAXX_select_count.reset_index(inplace=True)
LUSC_DAXX_select_count.reset_index(inplace=True)
SKCM_DAXX_select_count.reset_index(inplace=True)
STAD_DAXX_select_count.reset_index(inplace=True)

BLCA_ATRX_select_count.columns = BLCA_ATRX_select_count.columns.droplevel(1)
BRCA_ATRX_select_count.columns = BRCA_ATRX_select_count.columns.droplevel(1)
CESC_ATRX_select_count.columns = CESC_ATRX_select_count.columns.droplevel(1)
GBM_ATRX_select_count.columns = GBM_ATRX_select_count.columns.droplevel(1)
HNSC_ATRX_select_count.columns = HNSC_ATRX_select_count.columns.droplevel(1)
KIRC_ATRX_select_count.columns = KIRC_ATRX_select_count.columns.droplevel(1)
KIRP_ATRX_select_count.columns = KIRP_ATRX_select_count.columns.droplevel(1)
LIHC_ATRX_select_count.columns = LIHC_ATRX_select_count.columns.droplevel(1)
LUAD_ATRX_select_count.columns = LUAD_ATRX_select_count.columns.droplevel(1)
LUSC_ATRX_select_count.columns = LUSC_ATRX_select_count.columns.droplevel(1)
PRAD_ATRX_select_count.columns = PRAD_ATRX_select_count.columns.droplevel(1)
SARC_ATRX_select_count.columns = SARC_ATRX_select_count.columns.droplevel(1)
SKCM_ATRX_select_count.columns = SKCM_ATRX_select_count.columns.droplevel(1)
STAD_ATRX_select_count.columns = STAD_ATRX_select_count.columns.droplevel(1)
THCA_ATRX_select_count.columns = THCA_ATRX_select_count.columns.droplevel(1)
BLCA_DAXX_select_count.columns = BLCA_DAXX_select_count.columns.droplevel(1)
GBM_DAXX_select_count.columns = GBM_DAXX_select_count.columns.droplevel(1)
HNSC_DAXX_select_count.columns = HNSC_DAXX_select_count.columns.droplevel(1)
KIRC_DAXX_select_count.columns = KIRC_DAXX_select_count.columns.droplevel(1)
LIHC_DAXX_select_count.columns = LIHC_DAXX_select_count.columns.droplevel(1)
LUAD_DAXX_select_count.columns = LUAD_DAXX_select_count.columns.droplevel(1)
LUSC_DAXX_select_count.columns = LUSC_DAXX_select_count.columns.droplevel(1)
SKCM_DAXX_select_count.columns = SKCM_DAXX_select_count.columns.droplevel(1)
STAD_DAXX_select_count.columns = STAD_DAXX_select_count.columns.droplevel(1)

BRCA_ATRX_select_count = BRCA_ATRX_select_count[['Samples','Hugo_Symbol']]
BLCA_ATRX_select_count = BLCA_ATRX_select_count[['Samples','Hugo_Symbol']]
CESC_ATRX_select_count = CESC_ATRX_select_count[['Samples','Hugo_Symbol']]
GBM_ATRX_select_count = GBM_ATRX_select_count[['Samples','Hugo_Symbol']]
HNSC_ATRX_select_count = HNSC_ATRX_select_count[['Samples','Hugo_Symbol']]
KIRC_ATRX_select_count = KIRC_ATRX_select_count[['Samples','Hugo_Symbol']]
KIRP_ATRX_select_count = KIRP_ATRX_select_count[['Samples','Hugo_Symbol']]
LIHC_ATRX_select_count = LIHC_ATRX_select_count[['Samples','Hugo_Symbol']]
LUAD_ATRX_select_count = LUAD_ATRX_select_count[['Samples','Hugo_Symbol']]
LUSC_ATRX_select_count = LUSC_ATRX_select_count[['Samples','Hugo_Symbol']]
PRAD_ATRX_select_count = PRAD_ATRX_select_count[['Samples','Hugo_Symbol']]
SARC_ATRX_select_count = SARC_ATRX_select_count[['Samples','Hugo_Symbol']]
SKCM_ATRX_select_count = SKCM_ATRX_select_count[['Samples','Hugo_Symbol']]
STAD_ATRX_select_count = STAD_ATRX_select_count[['Samples','Hugo_Symbol']]
THCA_ATRX_select_count = THCA_ATRX_select_count[['Samples','Hugo_Symbol']]

GBM_DAXX_select_count = GBM_DAXX_select_count[['Samples','Hugo_Symbol']]
BLCA_DAXX_select_count = BLCA_DAXX_select_count[['Samples','Hugo_Symbol']]
HNSC_DAXX_select_count = HNSC_DAXX_select_count[['Samples','Hugo_Symbol']]
KIRC_DAXX_select_count = KIRC_DAXX_select_count[['Samples','Hugo_Symbol']]
LIHC_DAXX_select_count = LIHC_DAXX_select_count[['Samples','Hugo_Symbol']]
LUAD_DAXX_select_count = LUAD_DAXX_select_count[['Samples','Hugo_Symbol']]
LUSC_DAXX_select_count = LUSC_DAXX_select_count[['Samples','Hugo_Symbol']]
SKCM_DAXX_select_count = SKCM_DAXX_select_count[['Samples','Hugo_Symbol']]
STAD_DAXX_select_count = STAD_DAXX_select_count[['Samples','Hugo_Symbol']]

BRCA_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
BLCA_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
CESC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
GBM_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
HNSC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
KIRC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
KIRP_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LIHC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LUAD_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LUSC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
PRAD_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
SARC_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
SKCM_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
STAD_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
THCA_ATRX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)

BLCA_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
GBM_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
HNSC_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
KIRC_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LIHC_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LUAD_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
LUSC_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
SKCM_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)
STAD_DAXX_select_count.rename(columns={'Hugo_Symbol':'Count'}, inplace=True)

print(STAD_DAXX_select_count)
print(HNSC_ATRX_select_count)

# Find ATRX and DAXX comutation
BLCA_DAXX_ATRX = pd.merge(BLCA_ATRX_select_count, BLCA_DAXX_select_count, on='Samples', how='left')
GBM_DAXX_ATRX = pd.merge(GBM_ATRX_select_count, GBM_DAXX_select_count, on='Samples', how='left')
HNSC_DAXX_ATRX = pd.merge(HNSC_ATRX_select_count, HNSC_DAXX_select_count, on='Samples', how='left')
KIRC_DAXX_ATRX = pd.merge(KIRC_ATRX_select_count, KIRC_DAXX_select_count, on='Samples', how='left')
LIHC_DAXX_ATRX = pd.merge(LIHC_ATRX_select_count, LIHC_DAXX_select_count, on='Samples', how='left')
LUAD_DAXX_ATRX = pd.merge(LUAD_ATRX_select_count, LUAD_DAXX_select_count, on='Samples', how='left')
LUSC_DAXX_ATRX = pd.merge(LUSC_ATRX_select_count, LUSC_DAXX_select_count, on='Samples', how='left')
SKCM_DAXX_ATRX = pd.merge(SKCM_ATRX_select_count, SKCM_DAXX_select_count, on='Samples', how='left')
STAD_DAXX_ATRX = pd.merge(STAD_ATRX_select_count, STAD_DAXX_select_count, on='Samples', how='left')

GBM_DAXX_ATRX = GBM_DAXX_ATRX.fillna(0)
BLCA_DAXX_ATRX = BLCA_DAXX_ATRX.fillna(0)
HNSC_DAXX_ATRX = HNSC_DAXX_ATRX.fillna(0)
KIRC_DAXX_ATRX = KIRC_DAXX_ATRX.fillna(0)
LIHC_DAXX_ATRX = LIHC_DAXX_ATRX.fillna(0)
LUAD_DAXX_ATRX = LUAD_DAXX_ATRX.fillna(0)
LUSC_DAXX_ATRX = LUSC_DAXX_ATRX.fillna(0)
SKCM_DAXX_ATRX = SKCM_DAXX_ATRX.fillna(0)
STAD_DAXX_ATRX = STAD_DAXX_ATRX.fillna(0)

GBM_DAXX_ATRX['Count_All'] = GBM_DAXX_ATRX['Count_x'] + GBM_DAXX_ATRX['Count_y']
BLCA_DAXX_ATRX['Count_All'] = BLCA_DAXX_ATRX['Count_x'] + BLCA_DAXX_ATRX['Count_y']
HNSC_DAXX_ATRX['Count_All'] = HNSC_DAXX_ATRX['Count_x'] + HNSC_DAXX_ATRX['Count_y']
KIRC_DAXX_ATRX['Count_All'] = KIRC_DAXX_ATRX['Count_x'] + KIRC_DAXX_ATRX['Count_y']
LIHC_DAXX_ATRX['Count_All'] = LIHC_DAXX_ATRX['Count_x'] + LIHC_DAXX_ATRX['Count_y']
LUAD_DAXX_ATRX['Count_All'] = LUAD_DAXX_ATRX['Count_x'] + LUAD_DAXX_ATRX['Count_y']
LUSC_DAXX_ATRX['Count_All'] = LUSC_DAXX_ATRX['Count_x'] + LUSC_DAXX_ATRX['Count_y']
SKCM_DAXX_ATRX['Count_All'] = SKCM_DAXX_ATRX['Count_x'] + SKCM_DAXX_ATRX['Count_y']
STAD_DAXX_ATRX['Count_All'] = STAD_DAXX_ATRX['Count_x'] + STAD_DAXX_ATRX['Count_y']

GBM_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(GBM_DAXX_ATRX['Count_All'] > 0, 1, 0)
BLCA_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(BLCA_DAXX_ATRX['Count_All'] > 0, 1, 0)
HNSC_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(HNSC_DAXX_ATRX['Count_All'] > 0, 1, 0)
KIRC_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(KIRC_DAXX_ATRX['Count_All'] > 0, 1, 0)
LIHC_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(LIHC_DAXX_ATRX['Count_All'] > 0, 1, 0)
LUAD_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(LUAD_DAXX_ATRX['Count_All'] > 0, 1, 0)
LUSC_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(LUSC_DAXX_ATRX['Count_All'] > 0, 1, 0)
SKCM_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(SKCM_DAXX_ATRX['Count_All'] > 0, 1, 0)
STAD_DAXX_ATRX['ATRX_DAXX_Tally'] = np.where(STAD_DAXX_ATRX['Count_All'] > 0, 1, 0)

GBM_DAXX_ATRX_total = GBM_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
BLCA_DAXX_ATRX_total = BLCA_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
HNSC_DAXX_ATRX_total = HNSC_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
KIRC_DAXX_ATRX_total = KIRC_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
LIHC_DAXX_ATRX_total = LIHC_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
LUAD_DAXX_ATRX_total = LUAD_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
LUSC_DAXX_ATRX_total = LUSC_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
SKCM_DAXX_ATRX_total = SKCM_DAXX_ATRX['ATRX_DAXX_Tally'].sum()
STAD_DAXX_ATRX_total = STAD_DAXX_ATRX['ATRX_DAXX_Tally'].sum()

#ATRX and DAXX frequency
GBM_DAXX_ATRX_freq = GBM_DAXX_ATRX_total/GBM_total_samples
BLCA_DAXX_ATRX_freq = BLCA_DAXX_ATRX_total/BLCA_total_samples
HNSC_DAXX_ATRX_freq = HNSC_DAXX_ATRX_total/HNSC_total_samples
KIRC_DAXX_ATRX_freq = KIRC_DAXX_ATRX_total/KIRC_total_samples
LIHC_DAXX_ATRX_freq = LIHC_DAXX_ATRX_total/LIHC_total_samples
LUAD_DAXX_ATRX_freq = LUAD_DAXX_ATRX_total/LUAD_total_samples
LUSC_DAXX_ATRX_freq = LUSC_DAXX_ATRX_total/LUSC_total_samples
SKCM_DAXX_ATRX_freq = SKCM_DAXX_ATRX_total/SKCM_total_samples
STAD_DAXX_ATRX_freq = STAD_DAXX_ATRX_total/STAD_total_samples


print(HNSC_DAXX_ATRX)


BLCA_ATRX_select_mut_count = BLCA_ATRX_select_count['Samples'].nunique()
BRCA_ATRX_select_mut_count = BRCA_ATRX_select_count['Samples'].nunique()
CESC_ATRX_select_mut_count = CESC_ATRX_select_count['Samples'].nunique()
GBM_ATRX_select_mut_count = GBM_ATRX_select_count['Samples'].nunique()
HNSC_ATRX_select_mut_count = HNSC_ATRX_select_count['Samples'].nunique()
KIRC_ATRX_select_mut_count = KIRC_ATRX_select_count['Samples'].nunique()
KIRP_ATRX_select_mut_count = KIRP_ATRX_select_count['Samples'].nunique()
LIHC_ATRX_select_mut_count = LIHC_ATRX_select_count['Samples'].nunique()
LUAD_ATRX_select_mut_count = LUAD_ATRX_select_count['Samples'].nunique()
LUSC_ATRX_select_mut_count = LUSC_ATRX_select_count['Samples'].nunique()
PRAD_ATRX_select_mut_count = PRAD_ATRX_select_count['Samples'].nunique()
SARC_ATRX_select_mut_count = SARC_ATRX_select_count['Samples'].nunique()
SKCM_ATRX_select_mut_count = SKCM_ATRX_select_count['Samples'].nunique()
STAD_ATRX_select_mut_count = STAD_ATRX_select_count['Samples'].nunique()
THCA_ATRX_select_mut_count = THCA_ATRX_select_count['Samples'].nunique()
BLCA_DAXX_select_mut_count = BLCA_DAXX_select_count['Samples'].nunique()
GBM_DAXX_select_mut_count = GBM_DAXX_select_count['Samples'].nunique()
HNSC_DAXX_select_mut_count = HNSC_DAXX_select_count['Samples'].nunique()
KIRC_DAXX_select_mut_count = KIRC_DAXX_select_count['Samples'].nunique()
LIHC_DAXX_select_mut_count = LIHC_DAXX_select_count['Samples'].nunique()
LUAD_DAXX_select_mut_count = LUAD_DAXX_select_count['Samples'].nunique()
LUSC_DAXX_select_mut_count = LUSC_DAXX_select_count['Samples'].nunique()
SKCM_DAXX_select_mut_count = SKCM_DAXX_select_count['Samples'].nunique()
STAD_DAXX_select_mut_count = STAD_DAXX_select_count['Samples'].nunique()

BRCA_mut_freq_ATRX = BRCA_ATRX_select_mut_count/BRCA_total_samples
BLCA_mut_freq_ATRX = BLCA_ATRX_select_mut_count/BLCA_total_samples
CESC_mut_freq_ATRX = CESC_ATRX_select_mut_count/CESC_total_samples
GBM_mut_freq_ATRX = GBM_ATRX_select_mut_count/GBM_total_samples
HNSC_mut_freq_ATRX = HNSC_ATRX_select_mut_count/HNSC_total_samples
KIRC_mut_freq_ATRX = KIRC_ATRX_select_mut_count/KIRC_total_samples
KIRP_mut_freq_ATRX = KIRP_ATRX_select_mut_count/KIRP_total_samples
LIHC_mut_freq_ATRX = LIHC_ATRX_select_mut_count/LIHC_total_samples
LUAD_mut_freq_ATRX = LUAD_ATRX_select_mut_count/LUAD_total_samples
LUSC_mut_freq_ATRX = LUSC_ATRX_select_mut_count/LUSC_total_samples
PRAD_mut_freq_ATRX = PRAD_ATRX_select_mut_count/PRAD_total_samples
SARC_mut_freq_ATRX = SARC_ATRX_select_mut_count/SARC_total_samples
SKCM_mut_freq_ATRX = SKCM_ATRX_select_mut_count/SKCM_total_samples
STAD_mut_freq_ATRX = STAD_ATRX_select_mut_count/STAD_total_samples
THCA_mut_freq_ATRX = THCA_ATRX_select_mut_count/THCA_total_samples

GBM_mut_freq_DAXX = GBM_DAXX_select_mut_count/GBM_total_samples
BLCA_mut_freq_DAXX = BLCA_DAXX_select_mut_count/BLCA_total_samples
HNSC_mut_freq_DAXX = HNSC_DAXX_select_mut_count/HNSC_total_samples
KIRC_mut_freq_DAXX = KIRC_DAXX_select_mut_count/KIRC_total_samples
LIHC_mut_freq_DAXX = LIHC_DAXX_select_mut_count/LIHC_total_samples
LUAD_mut_freq_DAXX = LUAD_DAXX_select_mut_count/LUAD_total_samples
LUSC_mut_freq_DAXX = LUSC_DAXX_select_mut_count/LUSC_total_samples
SKCM_mut_freq_DAXX = SKCM_DAXX_select_mut_count/SKCM_total_samples
STAD_mut_freq_DAXX = STAD_DAXX_select_mut_count/STAD_total_samples

# For ATRX and DAXX co-mut
BRCA_DAXX_ATRX_freq = BRCA_ATRX_select_mut_count/BRCA_total_samples
CESC_DAXX_ATRX_freq = CESC_ATRX_select_mut_count/CESC_total_samples
KIRP_DAXX_ATRX_freq = KIRP_ATRX_select_mut_count/KIRP_total_samples
PRAD_DAXX_ATRX_freq = PRAD_ATRX_select_mut_count/PRAD_total_samples
SARC_DAXX_ATRX_freq = SARC_ATRX_select_mut_count/SARC_total_samples
THCA_DAXX_ATRX_freq = THCA_ATRX_select_mut_count/THCA_total_samples


merged_df = pd.DataFrame({'Cancer Type': ['BRCA'],
	'Mut_Freq':BRCA_mut_freq_ATRX,
	'Count_Samples_Mut':BRCA_ATRX_select_mut_count,
	'Total_Num_Samples_Tissue':BRCA_total_samples,
                   'Mutation':['ATRX']})

merged_df.loc[1] = ['CESC', CESC_mut_freq_ATRX, CESC_ATRX_select_mut_count, CESC_total_samples, 'ATRX']
merged_df.loc[2] = ['GBM', GBM_mut_freq_ATRX, GBM_ATRX_select_mut_count, GBM_total_samples, 'ATRX']
merged_df.loc[3] = ['HNSC', HNSC_mut_freq_ATRX, HNSC_ATRX_select_mut_count, HNSC_total_samples, 'ATRX']
merged_df.loc[4] = ['KIRC', KIRC_mut_freq_ATRX, KIRC_ATRX_select_mut_count, KIRC_total_samples, 'ATRX']
merged_df.loc[5] = ['KIRP', KIRP_mut_freq_ATRX, KIRP_ATRX_select_mut_count, KIRP_total_samples, 'ATRX']
merged_df.loc[6] = ['LIHC', LIHC_mut_freq_ATRX, LIHC_ATRX_select_mut_count, LIHC_total_samples, 'ATRX']
merged_df.loc[7] = ['LUAD', LUAD_mut_freq_ATRX, LUAD_ATRX_select_mut_count, LUAD_total_samples, 'ATRX']
merged_df.loc[8] = ['LUSC', LUSC_mut_freq_ATRX, LUSC_ATRX_select_mut_count, LUSC_total_samples, 'ATRX']
merged_df.loc[9] = ['PRAD', PRAD_mut_freq_ATRX, PRAD_ATRX_select_mut_count, PRAD_total_samples, 'ATRX']
merged_df.loc[10] = ['SARC', SARC_mut_freq_ATRX, SARC_ATRX_select_mut_count, SARC_total_samples, 'ATRX']
merged_df.loc[11] = ['SKCM', SKCM_mut_freq_ATRX, SKCM_ATRX_select_mut_count, SKCM_total_samples, 'ATRX']
merged_df.loc[12] = ['STAD', STAD_mut_freq_ATRX, STAD_ATRX_select_mut_count, STAD_total_samples, 'ATRX']
merged_df.loc[13] = ['THCA', THCA_mut_freq_ATRX,THCA_ATRX_select_mut_count, THCA_total_samples, 'ATRX'] 
merged_df.loc[14] = ['BLCA', BLCA_mut_freq_ATRX, BLCA_ATRX_select_mut_count, BLCA_total_samples, 'ATRX'] 

merged_df.loc[15] = ['GBM', GBM_mut_freq_DAXX, GBM_DAXX_select_mut_count, GBM_total_samples, 'DAXX']
merged_df.loc[16] = ['HNSC', HNSC_mut_freq_DAXX, HNSC_DAXX_select_mut_count, HNSC_total_samples, 'DAXX']
merged_df.loc[17] = ['KIRC', KIRC_mut_freq_DAXX, KIRC_DAXX_select_mut_count, KIRC_total_samples, 'DAXX']
merged_df.loc[18] = ['LIHC', LIHC_mut_freq_DAXX, LIHC_DAXX_select_mut_count, LIHC_total_samples, 'DAXX']
merged_df.loc[19] = ['LUAD', LUAD_mut_freq_DAXX, LUAD_DAXX_select_mut_count, LUAD_total_samples, 'DAXX']
merged_df.loc[20] = ['LUSC', LUSC_mut_freq_DAXX, LUSC_DAXX_select_mut_count, LUSC_total_samples, 'DAXX']
merged_df.loc[21] = ['SKCM', SKCM_mut_freq_DAXX, SKCM_DAXX_select_mut_count, SKCM_total_samples, 'DAXX']
merged_df.loc[22] = ['STAD', STAD_mut_freq_DAXX, STAD_DAXX_select_mut_count, STAD_total_samples, 'DAXX']
merged_df.loc[23] = ['BLCA', BLCA_mut_freq_ATRX, BLCA_ATRX_select_mut_count, BLCA_total_samples, 'ATRX']

merged_df.loc[24] = ['BRCA', BRCA_DAXX_ATRX_freq, BRCA_ATRX_select_mut_count, BRCA_total_samples, 'ATRX_DAXX']
merged_df.loc[25] = ['CESC', CESC_DAXX_ATRX_freq, CESC_ATRX_select_mut_count, CESC_total_samples, 'ATRX_DAXX']
merged_df.loc[26] = ['KIRP', KIRP_DAXX_ATRX_freq, KIRP_ATRX_select_mut_count, KIRP_total_samples, 'ATRX_DAXX']
merged_df.loc[27] = ['PRAD', PRAD_DAXX_ATRX_freq, PRAD_ATRX_select_mut_count, PRAD_total_samples, 'ATRX_DAXX']
merged_df.loc[28] = ['THCA', THCA_DAXX_ATRX_freq, THCA_ATRX_select_mut_count, THCA_total_samples, 'ATRX_DAXX']
merged_df.loc[29] = ['BRCA', BRCA_DAXX_ATRX_freq, BRCA_ATRX_select_mut_count, BRCA_total_samples, 'ATRX_DAXX']
merged_df.loc[30] = ['CESC', CESC_DAXX_ATRX_freq, CESC_ATRX_select_mut_count, CESC_total_samples, 'ATRX_DAXX']
merged_df.loc[31] = ['KIRP', KIRP_DAXX_ATRX_freq, KIRP_ATRX_select_mut_count, KIRP_total_samples, 'ATRX_DAXX']
merged_df.loc[32] = ['PRAD', PRAD_DAXX_ATRX_freq, PRAD_ATRX_select_mut_count, PRAD_total_samples, 'ATRX_DAXX']
merged_df.loc[33] = ['GBM', GBM_DAXX_ATRX_freq, GBM_ATRX_select_mut_count, GBM_total_samples, 'ATRX_DAXX']
merged_df.loc[34] = ['BLCA', BLCA_DAXX_ATRX_freq, BLCA_ATRX_select_mut_count, BLCA_total_samples, 'ATRX_DAXX']
merged_df.loc[35] = ['HNSC', HNSC_DAXX_ATRX_freq, HNSC_ATRX_select_mut_count, HNSC_total_samples, 'ATRX_DAXX']
merged_df.loc[36] = ['KIRC', KIRC_DAXX_ATRX_freq, KIRC_ATRX_select_mut_count, KIRC_total_samples, 'ATRX_DAXX']
merged_df.loc[37] = ['LIHC', LIHC_DAXX_ATRX_freq, LIHC_ATRX_select_mut_count, LIHC_total_samples, 'ATRX_DAXX']
merged_df.loc[38] = ['LUAD', LUAD_DAXX_ATRX_freq, LUAD_ATRX_select_mut_count, LUAD_total_samples, 'ATRX_DAXX']
merged_df.loc[39] = ['SKCM', SKCM_DAXX_ATRX_freq, SKCM_ATRX_select_mut_count, SKCM_total_samples, 'ATRX_DAXX']
merged_df.loc[40] = ['STAD', STAD_DAXX_ATRX_freq, STAD_ATRX_select_mut_count, STAD_total_samples, 'ATRX_DAXX']
merged_df.loc[41] = ['LUSC', LUSC_DAXX_ATRX_freq, LUSC_ATRX_select_mut_count, LUSC_total_samples, 'ATRX_DAXX']

merged_df.to_csv('/Users/chapmanlm/Desktop/Projects/ATRx_Project/data/output_data/MutFrequency_TumorTissue.csv',index=False)



