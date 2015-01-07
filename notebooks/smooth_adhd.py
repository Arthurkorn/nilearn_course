from nilearn import datasets, plotting, image

data = datasets.fetch_adhd()

mean_func = image.mean_img(data.func[0])

for smoothing in range(0, 25, 5):
    plotting.plot_epi(image.smooth_img(mean_func, smoothing),
                      title="Smoothing %imm" % smoothing)

