import streamlit as st
import os
from PIL import Image

# App Title
st.title("Dimensionality Reduction for MNIST Image Data")

# Visualization Directory
output_dir = "visualizations"

# Section 1: Introduction
st.header("Impact of Dimensionality Reduction on Data Visualization")
st.write("""
Dimensionality reduction techniques like *PCA (Principal Component Analysis)* and *t-SNE (t-Distributed Stochastic Neighbor Embedding)* are applied to high-dimensional MNIST image data. These techniques allow us to visualize the data in a 2D space.
""")

# Load and Display PCA Visualization
st.subheader("PCA Visualization")
pca_image_path = os.path.join(output_dir, "pca_visualization.png")
if os.path.exists(pca_image_path):
    st.image(Image.open(pca_image_path), caption="PCA Visualization (Reduced to 2D)", use_container_width=True)
else:
    st.warning("PCA visualization image not found!")

# Load and Display t-SNE Visualization
st.subheader("t-SNE Visualization")
tsne_image_path = os.path.join(output_dir, "tsne_visualization.png")
if os.path.exists(tsne_image_path):
    st.image(Image.open(tsne_image_path), caption="t-SNE Visualization (Reduced to 2D)", use_container_width=True)
else:
    st.warning("t-SNE visualization image not found!")

# Section 2: Trade-Off Analysis
st.header("Trade-Off: Information Loss vs Computational Efficiency")
st.write("""
Dimensionality reduction reduces the number of features (dimensions) in the dataset, which makes the data easier to process and visualize. However, this comes with a trade-off:
- *More components* retain more information but increase computational cost.
- *Fewer components* reduce computational requirements but may lose important information.
""")

# Load and Display Variance Analysis Plot
st.subheader("Variance Analysis")
variance_plot_path = os.path.join(output_dir, "variance_plot.png")
if os.path.exists(variance_plot_path):
    st.image(Image.open(variance_plot_path), caption="Cumulative Explained Variance by PCA Components", use_container_width=True)
else:
    st.warning("Variance plot image not found!")

# Load and Display Variance Analysis Text
variance_text_path = os.path.join(output_dir, "variance_analysis.txt")
if os.path.exists(variance_text_path):
    st.subheader("Variance Analysis Summary")
    with open(variance_text_path, "r") as f:
        variance_content = f.read()
    st.text(variance_content)
else:
    st.warning("Variance analysis text not found!")

# Section 3: Reconstructed Images
st.header("Effectiveness of Dimensionality Reduction for Image Data")
st.write("""
Here, we observe the *original images* versus the *reconstructed images* after applying PCA with 100 components. This helps us analyze how well PCA can approximate the original data.
""")

# Load and Display Original vs Reconstructed Image Comparison
st.subheader("Original vs Reconstructed Images")
reconstruction_image_path = os.path.join(output_dir, "reconstruction_comparison.png")
if os.path.exists(reconstruction_image_path):
    st.image(Image.open(reconstruction_image_path), caption="Original (Top) vs Reconstructed (Bottom) Images", use_container_width=True)
else:
    st.warning("Reconstruction comparison image not found!")

# Section 4: Conclusion
st.header("Conclusion")
st.write("""
- *PCA* provides a linear, efficient method for reducing dimensionality while retaining as much variance as possible.
- *t-SNE* is effective for visualizing complex, non-linear relationships in data.
- The trade-off between *information retention* and *computational efficiency* must be carefully balanced based on the task.
- For MNIST image data, dimensionality reduction techniques demonstrate their effectiveness in simplifying data for analysis and visualization without significant information loss.

These techniques are powerful tools for analyzing high-dimensional datasets like images.
""")

# Footer
st.markdown("---")
st.write("Created with Streamlit. Visualizations generated from MNIST dataset.")
