base_dir = '/Users/maullz/Desktop/Software_Comparison';
study = 'ds001';
		
study_dir = fullfile(base_dir, study);
reslice_dir = fullfile(study_dir, 'resliced_images');

if ~isdir(reslice_dir)
    mkdir(reslice_dir) 
end

afni_stat_file = fullfile(study_dir, 'AFNI', 'LEVEL2', '3dMEMA_result_t_stat_masked.nii');
afni_pos_exc_file = fullfile(study_dir, 'AFNI', 'LEVEL2', 'Positive_clustered_t_stat.nii');
afni_neg_exc_file = fullfile(study_dir, 'AFNI', 'LEVEL2', 'Negative_clustered_t_stat.nii');

gunzip(fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'stats', 'tstat1.nii.gz'));
fsl_stat_file = fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'stats', 'tstat1.nii');
gunzip(fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'thresh_zstat1.nii.gz'));
fsl_pos_exc_file = fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'thresh_zstat1.nii');
gunzip(fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'thresh_zstat2.nii.gz'));
fsl_neg_exc_file = fullfile(study_dir, 'FSL', 'LEVEL2', 'group.gfeat', 'cope1.feat', 'thresh_zstat2.nii');



spm_stat_file = fullfile(study_dir, 'SPM', 'LEVEL2', 'spmT_0001.nii');
spm_pos_exc_file = fullfile(study_dir, 'SPM', 'LEVEL2', 'spmT_0001_thresholded.nii');
spm_neg_exc_file = fullfile(study_dir, 'SPM', 'LEVEL2', 'spmT_0002_thresholded.nii');

[afni_stat_dir, ~, ~] = fileparts(afni_stat_file);
[fsl_stat_dir, ~, ~] = fileparts(fsl_stat_file);
[spm_stat_dir, ~, ~] = fileparts(spm_stat_file);


reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_fsl_');
spm_reslice({afni_stat_file, fsl_stat_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_fsl_pos_exc_');
spm_reslice({afni_pos_exc_file, fsl_pos_exc_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_fsl_neg_exc_');
spm_reslice({afni_neg_exc_file, fsl_neg_exc_file}, reslice_flags);



reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_spm_');
spm_reslice({afni_stat_file, spm_stat_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_spm_pos_exc');
spm_reslice({afni_pos_exc_file, spm_pos_exc_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_spm_neg_exc_');
spm_reslice({afni_neg_exc_file, spm_neg_exc_file}, reslice_flags);



reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'fsl_spm_');
spm_reslice({fsl_stat_file, spm_stat_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'fsl_spm_pos_exc');
spm_reslice({fsl_pos_exc_file, spm_pos_exc_file}, reslice_flags);

reslice_flags = struct('mask', false, 'mean', false, 'which', 1, 'wrap', [1 1 0], 'prefix', 'afni_spm_neg_exc_');
spm_reslice({fsl_neg_exc_file, spm_neg_exc_file}, reslice_flags);



movefile(fullfile(fsl_stat_dir, 'afni_fsl_tstat1.nii'), fullfile(reslice_dir, 'afni_fsl_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'afni_fsl_pos_exc_thresh_zstat1.nii.nii'), fullfile(reslice_dir, 'afni_fsl_pos_exc_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'afni_fsl_neg_exc_thresh_zstat2.nii.nii'), fullfile(reslice_dir, 'afni_fsl_neg_exc_reslice.nii'));

movefile(fullfile(spm_stat_dir, 'afni_spm_spmT_0001.nii'), fullfile(reslice_dir, 'afni_spm_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'afni_spm_pos_exc_spmT_0001_thresholded.nii'), fullfile(reslice_dir, 'afni_spm_pos_exc_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'afni_spm_neg_exc_spmT_0002_thresholded.nii'), fullfile(reslice_dir, 'afni_spm_neg_exc_reslice.nii'));


movefile(fullfile(spm_stat_dir, 'fsl_spm_spmT_0001.nii'), fullfile(reslice_dir, 'fsl_spm_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'fsl_spm_pos_exc_spmT_0001_thresholded.nii'), fullfile(reslice_dir, 'fsl_spm_pos_exc_reslice.nii'));
movefile(fullfile(fsl_stat_dir, 'fsl_spm_neg_exc_spmT_0002_thresholded.nii'), fullfile(reslice_dir, 'fsl_spm_neg_exc_reslice.nii'));
