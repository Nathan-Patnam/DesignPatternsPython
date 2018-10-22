from matplotlib import pyplot as plt


def create_line_graph():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    # create line graph
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # add axis
    plt.ylabel("Billions of $")
    plt.show()


def create_bar_graph():
    movies = ["West World", "Game Of Thrones",
              "X-Men", "DareDevil", "Spiderman"]
    frequency = [123, 1235, 2525, 6354, 213]
    xs = [i+.3 for i, _ in enumerate(movies)]
    plt.bar(xs, frequency)
    plt.ylabel("# of Daily Viewers")
    plt.title("My favorite TV Shows")

    plt.xticks([i+.3 for i, _ in enumerate(movies)], movies)
    plt.show()


def main():
    create_bar_graph()


main()
