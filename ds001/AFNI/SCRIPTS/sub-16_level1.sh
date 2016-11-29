#!/usr/bin/env tcsh

# created by uber_subject.py: version 0.39 (March 21, 2016)
# creation date: Tue Sep 13 15:59:22 2016

# run afni_proc.py to create a single subject processing script
afni_proc.py -subj_id sub16                                                  \
        -script proc.sub16 -scr_overwrite                                    \
        -blocks tshift align tlrc volreg blur mask scale regress             \
        -copy_anat /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/PREPROCESSING/ANATOMICAL/sub-16_T1w.nii                                    \
        -tcat_remove_first_trs 2                                             \
        -dsets                                                               \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/PREPROCESSING/FUNCTIONAL/sub-16_task-balloonanalogrisktask_run-01_bold.nii.gz     \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/PREPROCESSING/FUNCTIONAL/sub-16_task-balloonanalogrisktask_run-02_bold.nii.gz     \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/PREPROCESSING/FUNCTIONAL/sub-16_task-balloonanalogrisktask_run-03_bold.nii.gz     \
        -volreg_align_to third                                               \
        -volreg_align_e2a                                                    \
        -volreg_tlrc_warp                                                    \
        -blur_size 5.0                                                       \
        -regress_stim_times                                                  \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_cash_demean_afni.1d      \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_cash_RT_afni.1d              \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_control_pumps_demean_afni.1d \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_control_pumps_RT_afni.1d     \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_explode_demean_afni.1d   \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_pumps_demean_afni.1d     \
            /Users/cmaumet/Projects/Data_sharing/dev/Software_Comparison/ds001/AFNI/ONSETS/sub-16_combined_pumps_RT_afni.1d             \
        -regress_stim_labels                                                 \
            cash_demean cash_RT control_pumps_demean                         \
            control_pumps_RT explode_demean pumps_demean                     \
            pumps_RT                                                         \
        -regress_basis_multi                                                 \
            'BLOCK(0.772,1)' 'dmBLOCK' 'BLOCK(0.772,1)' 'dmBLOCK'            \
        'BLOCK(0.772,1)' 'BLOCK(0.772,1)' 'dmBLOCK'                          \
        -regress_stim_types                                                  \
            AM2 AM1 AM2 AM1 AM2 AM2 AM1                                      \
        -regress_censor_motion 0.3                                           \
        -regress_opts_3dD                                                    \
            -gltsym 'SYM: pumps_demean -control_pumps_demean'    \
        -glt_label 1 pumps_demean_vs_ctrl_demean                             \
        -regress_make_ideal_sum sum_ideal.1D                                 \
        -regress_est_blur_epits                                              \
        -regress_est_blur_errts

