'''
This is the main file that runs the interactive Streamlit application.
'''
import streamlit as st
import pandas as pd
from clustering import Clustering
def main():
    st.title("Interactive Clustering Application")
    # Input Dataset
    file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    if file is not None:
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
        st.write("Preview of the dataset:")
        st.dataframe(df.head())
        # Column Selection
        selected_columns = st.multiselect("Select columns for clustering", df.columns)
        statistical_columns = st.multiselect("Select columns for statistical analysis (optional)", df.columns)
        index_column = st.selectbox("Select index column (optional)", df.columns)
        nclusters = st.selectbox("Select numer of clusters", list(range(3, 15)))

        # Clustering
        clustering = Clustering(df, selected_columns, index_column, nclusters)
        clustering.run_kmeans()
        st.write("2D t-SNE chart:")
        st.pyplot(clustering.plot_tsne())
        # Statistics
        if statistical_columns:
            st.write("Cluster statistics:")
            st.dataframe(clustering.compute_statistics(statistical_columns))
        # Export
        export_format = st.selectbox("Select export format", ["Excel", "CSV"])
        if st.button("Export clustered dataset and cluster statistics"):
            clustering.export_data(export_format)
if __name__ == "__main__":
    main()