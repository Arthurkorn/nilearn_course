from nilearn import datasets
atlas = datasets.fetch_msdl_atlas()
atlas_img = atlas['maps']
import pandas
labels = pandas.read_csv(atlas['labels'])['name']

from nilearn.input_data import NiftiMapsMasker

masker = NiftiMapsMasker(maps_img=atlas_img, standardize=True,
                           memory='/tmp/nilearn_course', verbose=5)

from matplotlib import pyplot as plt
data = datasets.fetch_adhd(n_subjects=1)

time_series = masker.fit_transform(data.func[0],
                                   confounds=data.confounds)

import numpy as np
correlation = np.corrcoef(time_series.T)
plt.figure(figsize=(10, 10))
plt.imshow(correlation, interpolation="nearest")
x_ticks = plt.xticks(range(len(labels)), labels, rotation=90)
y_ticks = plt.yticks(range(len(labels)), labels)
