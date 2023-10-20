# Interactive Clustering Application User Manual
* App and documentation created using ChatDev/Gen AI - https://github.com/OpenBMB/ChatDev *
<img src='' width=400>

## Introduction
The Interactive Clustering Application is a Streamlit-based Python application that allows users to perform clustering and statistical analysis on a dataset with a variable number of columns. The application provides an interactive interface for selecting columns, running clustering algorithms, visualizing clusters, computing statistics, and exporting the clustered dataset and cluster statistics.

## Installation
To use the Interactive Clustering Application, follow these steps:

1. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

2. Download the source code files from the provided repository.

3. Open a terminal or command prompt and navigate to the directory where the source code files are located.

4. Run the following command to start the application:
   ```
   streamlit run main.py
   ```

5. The application will start running and a local server will be launched. You can access the application by opening a web browser and entering the URL provided in the terminal or command prompt.

## Usage
Once the application is running, you can use the following steps to perform clustering and statistical analysis on a dataset:

1. Upload Dataset: Click on the "Upload CSV or Excel file" button and select a CSV or Excel file containing the dataset you want to analyze. The application will dynamically detect the number of columns and display a preview of the dataset.

2. Column Selection: Use the multiselect dropdown to select the columns you want to use for clustering. You can also select columns for statistical analysis (optional) and specify an index column (optional).

3. Clustering: The application uses the k-means clustering algorithm by default. Once you have selected the columns, click on the "Run Clustering" button to perform clustering on the selected columns. The application will generate a 2D t-SNE chart to visualize the clusters.

4. Statistics: If you have selected columns for statistical analysis, the application will compute and display statistics for each cluster. The statistics will be shown in a table format.

5. Export: You can export the clustered dataset and cluster statistics by selecting the desired export format (CSV or Excel) from the dropdown and clicking on the "Export" button.

6. Customization: The application provides options for customizing the appearance of the t-SNE chart, such as color-coding clusters. You can use the sliders, dropdowns, or any interactive widgets provided to customize the chart.

7. Error Handling: The application implements proper error handling for invalid inputs or unexpected issues. If any errors occur, appropriate error messages will be displayed.

## Documentation
The Interactive Clustering Application is well-documented to provide clear instructions on how to use the application. The documentation includes information about the clustering algorithm used (k-means), dependencies, and best practices for working with large datasets. You can find the documentation in the repository's README file.

## Conclusion
The Interactive Clustering Application is a powerful tool for performing clustering and statistical analysis on datasets. With its user-friendly interface, interactive widgets, and export functionality, it provides a seamless experience for users to explore and analyze their data.