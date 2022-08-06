import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm
import numpy as np
import copy

class IndexTracker(object):
    def __init__(self, ax, X, norm=None, title=None):
        self.ax = ax
        title = title or "use scroll wheel to navigate images"
        ax.set_title(title)

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices // 2

        offsets = [X.shape[0]/2, X.shape[1]/2]

        if norm == "log":
            norm = LogNorm()

        cmap = copy.copy(plt.cm.get_cmap('gray')) # copy the default cmap
        cmap.set_bad((0,0,0))
        self.im = ax.imshow(self.X[:, :, self.ind], norm=norm,
                            extent=[0-offsets[0], 0+offsets[0], 0-offsets[1], 0+offsets[1]])
        #self.im.set_clim(0, maxp)
        self.cbar = plt.colorbar(self.im)
        self.update()

    def onscroll(self, event):
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        maxi = np.amax(self.X[:, :, self.ind])
        mini = np.amin(self.X[:, :, self.ind])
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()
        
def showIMG(image_array, norm=None, positions=None):
    # Shows colored img of electron density map
    title = f'Absolute Error between 180 and {positions} positions for the source'

    # Plot Layout
    fig, ax = plt.subplots(1, 1)
    fig.set_tight_layout(True)
    tracker = IndexTracker(ax, image_array, norm=norm, title=title)
    fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
    plt.show()
    