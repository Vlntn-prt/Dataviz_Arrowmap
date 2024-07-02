def mappa_freccia(gdf, colonna_lunghezze, colore_dx="#2244B3", colore_sx="#CB3332"):

# Calculate centroids for the geometries
    gdf['centroid_geom'] = gdf.geometry.centroid

    # Scale the arrow length according to the plot dimensions
    plot_width = 1098610.5886799996
    plot_height = 1415090.6838199995
    scaling_factor = min(plot_width, plot_height) * 0.01

    # Function to create an arrow patch
    def create_arrow_patch(centroid, length, colore_dx=colore_dx, colore_sx=colore_sx):
        x, y = centroid.x, centroid.y
        dx, dy = length * scaling_factor, 0  # Length along x-axis
        if length>0:
            colore=colore_dx
        else:
            colore=colore_sx #variabile del colore
        return FancyArrowPatch((x, y), (x + dx, y + dy), arrowstyle='->', mutation_scale=5, color=colore)
    # Create a list of arrow patches    
    arrow_patches = [create_arrow_patch(centroid, getattr(row, colonna_lunghezze)) for centroid, row in zip(gdf['centroid_geom'], gdf.itertuples())]
    # Plot the original shapefile
    ax = gdf.plot(color='lightgrey', edgecolor='black', linewidth=0.2, figsize=(11.25, 14.06))

    # Add the arrow patches to the plot
    for arrow_patch in arrow_patches:
        ax.add_patch(arrow_patch)
     #estetica
    plt.box(False)
    plt.xticks([])
    plt.yticks([])
    return plt
