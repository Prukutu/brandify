import matplotlib.pyplot as plt


def embed_logo(fig, img_file, loc='upper right', bbox=None):
    """ Embed an image to an existing matplotlib figure object. 
        
        Input
        -----
        fig (obj): Matplotlib figure object
        img_file (str): File to be embedded
        loc (str): Location to embed figure. Can be any of the following:
        
                    upper right
                    upper left
                    lower right
                    lower left

        Defaults to "upper right".

        bbox (iter): If a bbox is specified, provide exact location and size of
        image axis to be drawn. when specified, loc keyword argument is
        ignored. Default None. The bbox iterable follows the following
        structure:
            [x_coordinate, y_coordinate, x_length, y_length]

        where all values are in fractional figure units. 
    """

    # Create dictionary of loc argument bbox values

    bbox_dict = {
                 'upper right': [0.8, .9, 0.25, 0.25],
                 'upper left': [0.0, .9, 0.25, 0.25],
                 'lower right': [0.8, -0.33, 0.25, 0.25],
                 'lower left': [0.0, -0.33, 0.25, 0.25]
                }
    # Set the value of bbox_val to the appropriate iterable
    # If bbox is supplied by user, use that instead
    if bbox is None:
        bbox_val = bbox_dict[loc]
    else:
        bbox_val = bbox

    ax = fig.add_axes(bbox_val, 
                      anchor='NE',
                      zorder=1000)
    
    # Create image object into ax obj
    img = plt.imread(img_file)
    ax.imshow(img)
    ax.axis('off')

    return fig


