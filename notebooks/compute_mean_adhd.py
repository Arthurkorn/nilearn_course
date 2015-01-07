from nilearn import datasets, plotting, image

data = datasets.fetch_adhd()

for i in range(4):
    mean_func = image.mean_img(data.func[i])
    plotting.plot_epi(mean_func)

