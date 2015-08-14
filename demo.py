from pitchplotter.plotter import Plotter

__author__ = 'ola'

if __name__ == '__main__':
    plotter = Plotter("Demo")

    demo_arr = [
        [25, 50, 'Event 1', 34],
        [35, 41, 'Event 2', 14],
        [20, 33, 'Event 3', 23],
        [10, 52, 'Event 4', 56],
        [45, 60, 'Event 5', 9]
    ]

    plotter.add_events(demo_arr, "Demo events")

    plotter.plot()