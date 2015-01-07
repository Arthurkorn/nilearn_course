from nilearn import datasets, plotting
import nibabel

data = datasets.fetch_smith_2009()

rsn10 = nibabel.load(data.rsn10)
rsn10_3 = nibabel.Nifti1Image(rsn10.get_data()[..., 3],
                              rsn10.get_affine())
plotting.plot_stat_map(rsn10_3)

