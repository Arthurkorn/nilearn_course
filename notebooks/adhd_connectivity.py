from nilearn import datasets
atlas_img, labels = datasets.load_harvard_oxford('cort-maxprob-thr25-2mm')

from nilearn.input_data import NiftiLabelsMasker

masker = NiftiLabelsMasker(labels_img=atlas_img, standardize=True,
                           memory='/tmp/nilearn_course', verbose=5)

from matplotlib import pyplot as plt
data = datasets.fetch_adhd(n_subjects=1)

time_series = masker.fit_transform(data.func[0],
                                   confounds=data.confounds)

import numpy as np
correlation = np.corrcoef(time_series.T)
plt.figure(figsize=(10, 10))
plt.imshow(correlation, interpolation="nearest")
x_ticks = plt.xticks(range(len(labels) - 1), labels[1:], rotation=90)
y_ticks = plt.yticks(range(len(labels) - 1), labels[1:])
