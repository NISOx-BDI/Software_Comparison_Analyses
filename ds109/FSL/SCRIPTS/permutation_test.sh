cd /storage/essicd/data/NIDM-Ex/BIDS_Data/RESULTS/SOFTWARE_COMPARISON/ds109/FSL/LEVEL2/permutation_test

fslmerge -t contrasts /storage/essicd/data/NIDM-Ex/BIDS_Data/RESULTS/SOFTWARE_COMPARISON/ds109/FSL/LEVEL1/sub-*/combined.gfeat/cope1.feat/stats/cope1.nii.gz
randomise -i contrasts -o OneSampT_pos -1 -x -c `ptoz 0.005` -n 10000
fslmaths OneSampT_pos_clustere_corrp_tstat1 -thr 0.95 -bin -mul OneSampT_pos_tstat1 05FWECorrected_OneSampT_pos_exc_set

fslmaths contrasts.nii.gz -mul -1 negative_contrasts
randomise -i negative_contrasts -o OneSampT_neg -1 -x -c `ptoz 0.005` -n 10000 
fslmaths OneSampT_neg_clustere_corrp_tstat1 -thr 0.95 -bin -mul OneSampT_neg_tstat1 -mul -1 05FWECorrected_OneSampT_neg_exc_set 
