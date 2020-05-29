import matplotlib as mpl
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import datetime as dt
# import csv


def drawPieDiagram(data_names, data_values, your_request):
    dpi = 100
    fig = plt.figure(dpi = dpi, figsize = (1080 / dpi, 1920 / dpi) )
    mpl.rcParams.update({'font.size': 9})
    plt.title('Result of analisys for request: {0}'.format(your_request))
    plt.pie(data_values, autopct='%.1f%%', radius = 1.5)
    plt.legend(bbox_to_anchor = (-0.7, -0.14), loc = 'lower left', labels = data_names)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()
