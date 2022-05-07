
def plot_clusters_cancer(data, clusters):
    """
    Plots clusters using scatter plot and color them acordingly.

    :param pd.DataFrame data: dataframe with datapoints havig columns "x" and "y"
    :param list of int clusters: cluster label for each of the datapoint
    """
    import seaborn as sns
    # find outliers not belonging to any cluster (only relevant for DBSCAN)
    outlier_indices = clusters == -1

    # plot points and color them by cluster/label
    ax = sns.scatterplot(
        data=data[~outlier_indices],
        x="x",
        y="y",
        hue=clusters[~outlier_indices],
        palette="muted",
        legend=True,
    )

    if outlier_indices.any():
        ax = sns.scatterplot(
            data=data[outlier_indices], x="x", y="y", color="black", ax=ax, hue = 'diagnosis'
        )
    return ax