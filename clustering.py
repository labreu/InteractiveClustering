'''
This file contains the Clustering class that performs clustering and computes statistics.
'''
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
class Clustering:
    def __init__(self, df, selected_columns, index_column, nclusters):
        self.df = df
        self.selected_columns = selected_columns
        self.index_column = index_column
        self.cluster_labels = None
        self.nclusters = nclusters

    def run_kmeans(self):
        X = self.df[self.selected_columns].values
        kmeans = KMeans(n_clusters=self.nclusters)  # Change the number of clusters as needed
        self.cluster_labels = kmeans.fit_predict(X)
        self.df['Clusters'] = self.cluster_labels
        
    def plot_tsne(self):
        tsne = TSNE(n_components=2)
        X_embedded = tsne.fit_transform(self.df[self.selected_columns].values)
        fig, ax = plt.subplots()
        ax.scatter(X_embedded[:, 0], X_embedded[:, 1], c=self.cluster_labels)
        ax.set_xlabel("t-SNE Dimension 1")
        ax.set_ylabel("t-SNE Dimension 2")
        ax.set_title("t-SNE Visualization")
        return fig
    def compute_statistics(self, statistical_columns):
        unique_labels = np.unique(self.cluster_labels)
        statistics = pd.DataFrame(index=unique_labels)
        for column in statistical_columns:
            statistics[column + " Avg"] = self.df.groupby(self.cluster_labels)[column].mean()
            statistics[column + " Std"] = self.df.groupby(self.cluster_labels)[column].std()
        return statistics
    def export_data(self, export_format):
        if self.index_column:
            self.df.set_index(self.index_column, inplace=True)
        else:
            self.df.reset_index(drop=True, inplace=True)  # Reset the index if no index column is selected
        if export_format == "CSV":
            self.df.to_csv("clustered_data.csv", index=False)
        elif export_format == "Excel":
            self.df.to_excel("clustered_data.xlsx", index=False)