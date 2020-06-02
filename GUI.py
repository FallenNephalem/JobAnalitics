import matplotlib as mpl
import matplotlib.pyplot as plt
import platform


def drawPieDiagram(data_names, data_values, your_request):
    dpi = 100
    fig = plt.figure(dpi = dpi, figsize = (1080 / dpi, 1920 / dpi) )
    mpl.rcParams.update({'font.size': 9.5})
    plt.title('Result of analisys for request: {0}'.format(your_request),fontdict = {'fontsize' : 16}, y=1.11)
    plt.pie(data_values, autopct='%.1f%%', radius = 1.45)
    plt.legend(bbox_to_anchor = (-0.75, -0.14), loc = 'lower left', labels = data_names)
    mng = plt.get_current_fig_manager()
    if platform.system() == 'Windows':
        mng.window.state('zoomed')
    if platform.system() == 'Linux':
        mng.resize(*mng.window.maxsize())
    plt.show()
