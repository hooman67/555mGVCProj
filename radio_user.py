import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection

import weights_barchart
import scenarioAB_Processing
# pylint: disable-msg=C0103


def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    # rotate theta such that the first axis is at the top
    theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        # unit circle centered on (0.5, 0.5)
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('unknown value for `frame`: %s' % frame)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1
        # define draw_frame method
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            """Override fill so that line is closed by default"""
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)
            # The following is a hack to get the spines (i.e. the axes frame)
            # to draw correctly for a polygon frame.

            # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            # close off polygon by repeating first vertex
            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):
    """Return vertices of polygon for subplot axes.

    This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
    """
    x0, y0, r = [0.5] * 3
    verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
    return verts


def example_data(n):

    '''data = [
        ['Language', 'Database', 'Data Format', 'Deploy Target', 'Backend', 'Web Server', 'Learning Curve', 'Adaptability'],
        ('Basecase', [
            [0.80, 0.50, 0.40, 0.15, 0.75, 0.75, 0.60, 0.20],
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00],
            [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00],
            [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00]])
    ]'''
    if n == 'Ann':
      data = [
          ['Pool', 'Internet', 'Location'],
          ('Basecase', [
            [0, 0.8, 0],
            [0, 0.4, 0.2],
            [0, 0, 0.2],
          ])
      ]
    elif n == 'Bob':
      data = [
          ['Pool', 'Internet', 'Location'],
          ('Basecase', [
              [0, 0, 1],
              [0, 0, 0],
              [0, 0, 0],
          ])
      ]
    elif n == 'Carol':
      data = [
          ['Pool', 'Internet', 'Location'],
          ('Basecase', [
              [0.3, 0.3, 0.4],
              [0.3, 0.21, 0],
              [0, 0, 0],
          ])
      ]
    elif n == 'Emily':
      data = [
          ['Pool', 'Internet', 'Location'],
          ('Basecase', [
              [0.61, 0.065, 0],
              [0.61, 0, 0.27],
              [0, 0.11, 0.27],
          ])
      ]
    return data




def main(alts, users, user_data, name_of_user):
    data = scenarioAB_Processing.get_criteria_scores_one_user_multi_alts(user_data, alts, name_of_user)
    spoke_labels = []
    for i in alts.iterkeys():
        for a in alts[i].iterkeys():
            spoke_labels.append(a)
        break

    alt_names = []
    for i in alts.iterkeys():
        alt_names.append(i)    

    N = len(spoke_labels)
    theta = radar_factory(N, frame='circle')
    
    
    fig = plt.figure(figsize=(9, 9))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['r', 'g', 'b', 'c', 'w']
    ax = fig.add_subplot(111, projection='radar')
    

    for i in range(len(data)): 
        ax.plot(theta, data[i], color=colors[i], alpha=0.25)
        ax.fill(theta, data[i], facecolor=colors[i], alpha=0.25, label = users[i])
    '''ax.plot(theta, data[0], color=colors[0], alpha=0.25)
    ax.fill(theta, data[0], facecolor=colors[0], alpha=0.25, label = alt_names[0])
    ax.plot(theta, data[1], color=colors[1])
    ax.fill(theta, data[1], facecolor=colors[1], alpha=0.25, label = alt_names[1])
    ax.plot(theta, data[2], color=colors[2])
    ax.fill(theta, data[2], facecolor=colors[2], alpha=0.25, label = alt_names[2])'''


    ax.set_varlabels(spoke_labels)
    for label in ax.get_xticklabels():  # make the xtick labels pickable
        label.set_picker(True)

    def onpick(event):
        legline = event.artist
        weights_barchart.draw_bar(str(legline.get_text()))

    # Plot the four cases from the example data on separate axes
    '''for ax, (title, case_data) in zip(axes.flatten(), data):
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)'''



    # add legend relative to top-left plot
    #####ax = axes[0, 0]



    '''labels = ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
    legend = ax.legend(labels, loc=(0.9, .95),
                       labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
             horizontalalignment='center', color='black', weight='bold',
             size='large')'''

    fig.canvas.mpl_connect('pick_event', onpick)

    leg = ax.legend(loc="upper left", bbox_to_anchor=[0, 1.2],
           ncol=2, shadow=True, title="Legend", fancybox=True)

    #plt.title('The Ritz', loc='right')

    plt.show()



if __name__ == '__main__':
    main()