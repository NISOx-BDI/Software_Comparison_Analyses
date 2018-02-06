import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

class FixedOrderFormatter(ScalarFormatter):
    """Formats axis ticks using scientific notation with a constant order of 
    magnitude"""
    def __init__(self, order_of_mag=0, useOffset=True, useMathText=False):
        self._order_of_mag = order_of_mag
        ScalarFormatter.__init__(self, useOffset=useOffset, 
                                 useMathText=useMathText)
    def _set_orderOfMagnitude(self, range):
        """Over-riding this to avoid having orderOfMagnitude reset elsewhere"""
        self.orderOfMagnitude = self._order_of_mag

def scatter_plot(data1, data2, *args, **kwargs):
    in_mask_indices = np.logical_not(np.logical_or(
    np.logical_or(np.isnan(data1), np.absolute(data1) == 0),
    np.logical_or(np.isnan(data2), np.absolute(data2) == 0)))

    data1 = data1[in_mask_indices]
    data2 = data2[in_mask_indices]

    #UNCOMMENT TO GET RID OF AFNI ds109 OUTLIERS
    #non_outlier_indices = np.logical_and(abs(data1) < 10, abs(data2) < 7)
    #data1 = data1[non_outlier_indices]
    #data2 = data2[non_outlier_indices]
    
    return data1, data2

def scatter(Title, afni_stat_file, spm_stat_file,
                 afni_reslice_spm, afni_spm_reslice, AFNI_SPM_title, AFNI_FSL_title=None, FSL_SPM_title=None,
                 fsl_stat_file=None, fsl_reslice_spm=None,
                 afni_fsl_reslice=None, afni_reslice_fsl=None, fsl_spm_reslice=None):
    plt.style.use('seaborn-colorblind')
    
    # Get data from stat images
    afni_dat = nib.load(afni_stat_file).get_data()
    spm_dat = nib.load(spm_stat_file).get_data()
    if fsl_stat_file is not None:
        fsl_dat = nib.load(fsl_stat_file).get_data()

    # Get data from resliced images   
    afni_res_spm_dat = nib.load(afni_reslice_spm).get_data()
    afni_spm_res_dat = nib.load(afni_spm_reslice).get_data()
    if fsl_stat_file is not None:
        afni_res_fsl_dat = nib.load(afni_reslice_fsl).get_data()
        fsl_res_spm_dat = nib.load(fsl_reslice_spm).get_data()
        afni_fsl_res_dat = nib.load(afni_fsl_reslice).get_data()
        fsl_spm_res_dat = nib.load(fsl_spm_reslice).get_data()
    
    # Reshape to 1-dimension
    afni_1d = np.reshape(afni_dat, -1)
    spm_1d = np.reshape(spm_dat, -1)
    afni_res_spm_1d = np.reshape(afni_res_spm_dat, -1)
    afni_spm_res_1d = np.reshape(afni_spm_res_dat, -1)
    if fsl_stat_file is not None:
        fsl_1d = np.reshape(fsl_dat, -1)
        afni_res_fsl_1d = np.reshape(afni_res_fsl_dat, -1)
        afni_fsl_res_1d = np.reshape(afni_fsl_res_dat, -1)
        fsl_res_spm_1d = np.reshape(fsl_res_spm_dat, -1)
        fsl_spm_res_1d = np.reshape(fsl_spm_res_dat, -1)
    
    # Create Scatter plots
    # AFNI/FSL B-A plots
    if fsl_stat_file is not None:
        f = plt.figure(figsize=(13, 5))
        
        f.suptitle(Title, fontsize=20, x=0.47, y=1.00)
        
        gs0 = gridspec.GridSpec(1, 2)
        
        gs00 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[0], hspace=0.50, wspace=1.3)
        
        ax1 = f.add_subplot(gs00[:-1, 1:5])
        data1, data2 = scatter_plot(afni_res_fsl_1d, fsl_1d)
        hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
        # Plot the line y=x
        lineStart = data1.min()
        lineEnd = data2.max()
        ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
        # Make the axes equal scale
        lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
        ]
        ax1.set_aspect('equal')
        ax1.set_xlim(lims)
        ax1.set_ylim(lims)
        ax1.set_title(AFNI_FSL_title)
        ax2 = f.add_subplot(gs00[:-1, 0], xticklabels=[], sharey=ax1)
        ax2.hist(data2, 100, histtype='stepfilled',
                    orientation='horizontal', color='gray')
        ax2.invert_xaxis()
        ax2.set_ylabel('FSL T-stat')
        ax3 = f.add_subplot(gs00[-1, 1:5], yticklabels=[], sharex=ax1)
        ax3.hist(data1, 100, histtype='stepfilled',
                    orientation='vertical', color='gray')
        ax3.invert_yaxis()
        ax3.set_xlabel('AFNI T-stat')
        ax4 = f.add_subplot(gs00[:-1,5])
        ax4.set_aspect(20)
        pos1 = ax4.get_position()
        ax4.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
        cb = f.colorbar(hb, cax=ax4)
        cb.set_label('log10(N)')
        
        gs01 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[1], hspace=0.50, wspace=1.3)
        
        ax5 = f.add_subplot(gs01[:-1, 1:5])
        data1, data2 = scatter_plot(afni_1d, afni_fsl_res_1d)
        hb = ax5.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
        # Plot the line y=x
        lineStart = data1.min()
        lineEnd = data2.max()
        ax5.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
        # Make the axes equal scale
        lims = [
            np.min([ax5.get_xlim(), ax5.get_ylim()]),  # min of both axes
            np.max([ax5.get_xlim(), ax5.get_ylim()]),  # max of both axes
        ]
        ax5.set_aspect('equal')
        ax5.set_xlim(lims)
        ax5.set_ylim(lims)
        ax5.set_title('FSL reslice on AFNI Scatter')
        ax6 = f.add_subplot(gs01[:-1, 0], xticklabels=[], sharey=ax5)
        ax6.hist(data2, 100, histtype='stepfilled',
                    orientation='horizontal', color='gray')
        ax6.invert_xaxis()
        ax6.set_ylabel('FSL T-stat')
        ax7 = f.add_subplot(gs01[-1, 1:5], yticklabels=[], sharex=ax5)
        ax7.hist(data1, 100, histtype='stepfilled',
                    orientation='vertical', color='gray')
        ax7.invert_yaxis()
        ax7.set_xlabel('AFNI T-stat')
        ax8 = f.add_subplot(gs01[:-1,5])
        ax8.set_aspect(20)
        pos1 = ax8.get_position()
        ax8.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
        cb = f.colorbar(hb, cax=ax8)
        cb.set_label('log10(N)')
        
        plt.show()

    # AFNI/SPM B-A plots
    f = plt.figure(figsize=(13, 5))
    
    if fsl_stat_file is None:
        f.suptitle(Title, fontsize=20, x=0.47, y=1.00)

    gs0 = gridspec.GridSpec(1, 2)

    gs00 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[0], hspace=0.50, wspace=1.3)

    ax1 = f.add_subplot(gs00[:-1, 1:5])
    data1, data2 = scatter_plot(afni_res_spm_1d, spm_1d)
    hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
    # Plot the line y=x
    lineStart = data1.min()
    lineEnd = data2.max()
    ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
    # Make the axes equal scale
    lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
    ]
    ax1.set_aspect('equal')
    ax1.set_xlim(lims)
    ax1.set_ylim(lims)
    ax1.set_title(AFNI_SPM_title)
    ax2 = f.add_subplot(gs00[:-1, 0], xticklabels=[], sharey=ax1)
    ax2.hist(data2, 100, histtype='stepfilled',
             orientation='horizontal', color='gray')
    ax2.invert_xaxis()
    ax2.set_ylabel('SPM T-stat')
    ax3 = f.add_subplot(gs00[-1, 1:5], yticklabels=[], sharex=ax1)
    ax3.hist(data1, 100, histtype='stepfilled',
             orientation='vertical', color='gray')
    ax3.invert_yaxis()
    if fsl_stat_file is None:
        ax3.set_xlabel('AFNI F-Stat')
    else:
        ax3.set_xlabel('AFNI T-Stat')     
    ax4 = f.add_subplot(gs00[:-1,5])
    ax4.set_aspect(20)
    pos1 = ax4.get_position()
    ax4.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
    cb = f.colorbar(hb, cax=ax4)
    cb.set_label('log10(N)')

    gs01 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[1], hspace=0.50, wspace=1.3)

    ax5 = f.add_subplot(gs01[:-1, 1:5])
    data1, data2 = scatter_plot(afni_1d, afni_spm_res_1d)
    hb = ax5.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
    # Plot the line y=x
    lineStart = data1.min()
    lineEnd = data2.max()
    ax5.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
    # Make the axes equal scale
    lims = [
        np.min([ax5.get_xlim(), ax5.get_ylim()]),  # min of both axes
        np.max([ax5.get_xlim(), ax5.get_ylim()]),  # max of both axes
    ]
    ax5.set_aspect('equal')
    ax5.set_xlim(lims)
    ax5.set_ylim(lims)
    ax5.set_title('SPM reslice on AFNI Scatter')
    ax6 = f.add_subplot(gs01[:-1, 0], xticklabels=[], sharey=ax5)
    ax6.hist(data2, 100, histtype='stepfilled',
             orientation='horizontal', color='gray')
    ax6.invert_xaxis()
    ax6.set_ylabel('SPM T-stat')
    ax7 = f.add_subplot(gs01[-1, 1:5], yticklabels=[], sharex=ax5)
    ax7.hist(data1, 100, histtype='stepfilled',
             orientation='vertical', color='gray')
    ax7.invert_yaxis()
    ax7.set_xlabel('AFNI T-Stat')
    ax8 = f.add_subplot(gs01[:-1,5])
    ax8.set_aspect(20)
    pos1 = ax8.get_position()
    ax8.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
    cb = f.colorbar(hb, cax=ax8)
    cb.set_label('log10(N)')

    plt.show()

    # FSL/SPM B-A plots
    if fsl_stat_file is not None:
        f = plt.figure(figsize=(13, 5))

        gs0 = gridspec.GridSpec(1, 2)

        gs00 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[0], hspace=0.50, wspace=1.3)

        ax1 = f.add_subplot(gs00[:-1, 1:5])
        data1, data2 = scatter_plot(fsl_res_spm_1d, spm_1d)
        hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
        # Plot the line y=x
        lineStart = data1.min()
        lineEnd = data2.max()
        ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
        # Make the axes equal scale
        lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
        ]
        ax1.set_aspect('equal')
        ax1.set_xlim(lims)
        ax1.set_ylim(lims)
        ax1.set_title(FSL_SPM_title)
        ax2 = f.add_subplot(gs00[:-1, 0], xticklabels=[], sharey=ax1)
        ax2.hist(data2, 100, histtype='stepfilled',
                 orientation='horizontal', color='gray')
        ax2.invert_xaxis()
        ax2.set_ylabel('SPM T-stat')
        ax3 = f.add_subplot(gs00[-1, 1:5], yticklabels=[], sharex=ax1)
        ax3.hist(data1, 100, histtype='stepfilled',
                 orientation='vertical', color='gray')
        ax3.invert_yaxis()
        ax3.set_xlabel('FSL T-stat')
        ax4 = f.add_subplot(gs00[:-1,5])
        ax4.set_aspect(20)
        pos1 = ax4.get_position()
        ax4.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
        cb = f.colorbar(hb, cax=ax4)
        cb.set_label('log10(N)')

        gs01 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[1], hspace=0.50, wspace=1.3)

        ax5 = f.add_subplot(gs01[:-1, 1:5])
        data1, data2 = scatter_plot(fsl_1d, fsl_spm_res_1d)
        hb = ax5.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
        # Plot the line y=x
        lineStart = data1.min()
        lineEnd = data2.max()
        ax5.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
        # Make the axes equal scale
        lims = [
        np.min([ax5.get_xlim(), ax5.get_ylim()]),  # min of both axes
        np.max([ax5.get_xlim(), ax5.get_ylim()]),  # max of both axes
        ]
        ax5.set_aspect('equal')
        ax5.set_xlim(lims)
        ax5.set_ylim(lims)
        ax5.set_title('SPM reslice on FSL Bland-Altman')
        ax6 = f.add_subplot(gs01[:-1, 0], xticklabels=[], sharey=ax5)
        ax6.hist(data2, 100, histtype='stepfilled',
                 orientation='horizontal', color='gray')
        ax6.invert_xaxis()
        ax6.set_ylabel('SPM T-stat')
        ax7 = f.add_subplot(gs01[-1, 1:5], yticklabels=[], sharex=ax5)
        ax7.hist(data1, 100, histtype='stepfilled',
                 orientation='vertical', color='gray')
        ax7.invert_yaxis()
        ax7.set_xlabel('FSL T-stat')
        ax8 = f.add_subplot(gs01[:-1,5])
        ax8.set_aspect(20)
        pos1 = ax8.get_position()
        ax8.set_position([pos1.x0 - 0.025, pos1.y0, pos1.width, pos1.height])
        cb = f.colorbar(hb, cax=ax8)
        cb.set_label('log10(N)')

        plt.show()

def scatter_intra(Title, afni_stat_file, afni_perm_file,
                 fsl_stat_file, fsl_perm_file,
                 spm_stat_file, spm_perm_file):
    plt.style.use('seaborn-colorblind')
    
    # Get data from stat images
    afni_stat_dat = nib.load(afni_stat_file).get_data()
    afni_perm_dat = nib.load(afni_perm_file).get_data()
    fsl_stat_dat = nib.load(fsl_stat_file).get_data()
    fsl_perm_dat = nib.load(fsl_perm_file).get_data()
    spm_stat_dat = nib.load(spm_stat_file).get_data()
    spm_perm_dat = nib.load(spm_perm_file).get_data()
    
    # Reshape to 1-dimension
    afni_stat_1d = np.reshape(afni_stat_dat, -1)
    afni_perm_1d = np.reshape(afni_perm_dat, -1)
    fsl_stat_1d = np.reshape(fsl_stat_dat, -1)
    fsl_perm_1d = np.reshape(fsl_perm_dat, -1)
    spm_stat_1d = np.reshape(spm_stat_dat, -1)
    spm_perm_1d = np.reshape(spm_perm_dat, -1)
      
    # AFNI Parametric/AFNI Permutation Bland-Altman
    f = plt.figure(figsize=(6.5, 5))
    
    f.suptitle(Title, fontsize=20, x=0.40, y=3.70)
    f.subplots_adjust(hspace=0.3, top=3.58, bottom=1.0, left=0.1, right=0.8)
    
    gs0 = gridspec.GridSpec(3, 1)
   
    gs00 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[0], hspace=0.50, wspace=0.65)
    ax1 = plt.subplot(gs00[:-1, 1:5])
    data1, data2 = scatter_plot(afni_stat_1d, afni_perm_1d)
    hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
    # Plot the line y=x
    lineStart = data1.min()
    lineEnd = data2.max()
    ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
    # Make the axes equal scale
    lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
    ]
    ax1.set_aspect('equal')
    ax1.set_xlim(lims)
    ax1.set_ylim(lims)
    ax1.set_title('AFNI Para/Perm')
    ax2 = plt.subplot(gs00[:-1, 0], xticklabels=[], sharey=ax1)
    ax2.hist(data2, 100, histtype='stepfilled',
             orientation='horizontal', color='gray')
    ax2.invert_xaxis()
    ax2.set_ylabel('Permutation T-stat')
    ax3 = plt.subplot(gs00[-1, 1:5], yticklabels=[], sharex=ax1)
    ax3.hist(data1, 100, histtype='stepfilled',
             orientation='vertical', color='gray')
    ax3.invert_yaxis()
    ax3.set_xlabel('Parametric T-stat')
    ax4 = plt.subplot(gs00[:-1,5])
    ax4.set_aspect(20)
    pos1 = ax4.get_position()
    ax4.set_position([pos1.x0 - 0.045, pos1.y0, pos1.width, pos1.height])
    cb = f.colorbar(hb, cax=ax4)
    cb.set_label('log10(N)')
    
    
    # FSL Parametric/FSL Permutation Bland-Altman
    gs01 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[1], hspace=0.50, wspace=0.65)
    ax1 = plt.subplot(gs01[:-1, 1:5])
    data1, data2 = scatter_plot(fsl_stat_1d, fsl_perm_1d)
    hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
    # Plot the line y=x
    lineStart = data1.min()
    lineEnd = data2.max()
    ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
    # Make the axes equal scale
    lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
    ]
    ax1.set_aspect('equal')
    ax1.set_xlim(lims)
    ax1.set_ylim(lims)
    ax1.set_title('FSL Para/Perm')
    ax2 = plt.subplot(gs01[:-1, 0], xticklabels=[], sharey=ax1)
    ax2.hist(data2, 100, histtype='stepfilled',
             orientation='horizontal', color='gray')
    ax2.invert_xaxis()
    ax2.set_ylabel('Permutation T-stat')
    ax3 = plt.subplot(gs01[-1, 1:5], yticklabels=[], sharex=ax1)
    ax3.hist(data1, 100, histtype='stepfilled',
             orientation='vertical', color='gray')
    ax3.invert_yaxis()
    ax3.set_xlabel('Parametric T-stat')
    ax4 = plt.subplot(gs01[:-1,5])
    ax4.set_aspect(20)
    pos1 = ax4.get_position()
    ax4.set_position([pos1.x0 - 0.045, pos1.y0, pos1.width, pos1.height])
    cb = f.colorbar(hb, cax=ax4)
    cb.set_label('log10(N)')

    # SPM Parametric/SPM Permutation Bland-Altman
    gs02 = gridspec.GridSpecFromSubplotSpec(5, 6, subplot_spec=gs0[2], hspace=0.50, wspace=1.3)
    ax1 = plt.subplot(gs02[:-1, 1:5])
    
    tick_formatter = ticker.ScalarFormatter(useOffset=False)
    tick_formatter.set_powerlimits((-6, 6))
    ax1.yaxis.set_major_formatter(FixedOrderFormatter(-7))
    
    data1, data2 = scatter_plot(spm_stat_1d, spm_perm_1d)
    hb = ax1.hexbin(data1, data2, bins='log', cmap='viridis', gridsize=50)
    # Plot the line y=x
    lineStart = data1.min()
    lineEnd = data2.max()
    ax1.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
    # Make the axes equal scale
    lims = [
        np.min([ax1.get_xlim(), ax1.get_ylim()]),  # min of both axes
        np.max([ax1.get_xlim(), ax1.get_ylim()]),  # max of both axes
    ]
    ax1.set_aspect('equal')
    ax1.set_xlim(lims)
    ax1.set_ylim(lims)
    ax1.set_title('SPM Para/Perm')
    ax2 = plt.subplot(gs02[:-1, 0], xticklabels=[], sharey=ax1)
    ax2.hist(data2, 100, histtype='stepfilled',
             orientation='horizontal', color='gray')
    ax2.invert_xaxis()
    ax2.set_ylabel('Permutation T-stat')
    ax3 = plt.subplot(gs02[-1, 1:5], yticklabels=[], sharex=ax1)
    ax3.hist(data1, 100, histtype='stepfilled',
             orientation='vertical', color='gray')
    ax3.invert_yaxis()
    ax3.set_xlabel('Parametric T-stat')
    ax4 = plt.subplot(gs02[:-1,5])
    ax4.set_aspect(20)
    pos1 = ax4.get_position()
    ax4.set_position([pos1.x0 - 0.045, pos1.y0, pos1.width, pos1.height])
    cb = f.colorbar(hb, cax=ax4)
    cb.set_label('log10(N)')

    plt.show()