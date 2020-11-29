import matplotlib.pyplot as plt



def graph_data(dataFrame, param):
    """# Data for plotting
    fig, ax = plt.subplots()
    ax.plot(years, data)

    ax.set(xlabel='Años', ylabel='Temperatura MAX(°C)')
    ax.grid()

    #fig.savefig("test.png")"""
    dataFrame.plot(x='FECHA', y=param)
    plt.show()