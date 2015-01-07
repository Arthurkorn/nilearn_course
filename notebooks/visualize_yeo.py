from nilearn import datasets, plotting

data = datasets.fetch_yeo_2011_atlas()
plotting.plot_roi(data.liberal_7, title="7 clusters")
plotting.plot_roi(data.liberal_17, title="17 clusters")

