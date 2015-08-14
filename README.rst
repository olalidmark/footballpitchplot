Football pitch plot
=======================

Python library using Plotly for plotting a football pitch with events. Examples can be found here: http://blog.stryktipsetisistastund.se/tag/plotly/

Installation
-----------------------
Requires the plotly lib to be available and set up. See: https://plot.ly/python/getting-started/

Usage
-----------------------

.. code:: python

    from pitchplotter.plotter import Plotter

    plotter = Plotter("Demo")

    #create array as follows: [xpos, ypos, 'event name', event size]
    demo_arr = [
        [25,50,'Event 1', 34],
        [35,41,'Event 2', 14],
        [20,33,'Event 3', 23],
        [10,52,'Event 4', 56],
        [45,60,'Event 5', 9]
    ]

    plotter.add_events(demo_arr, "Demo events")

    plotter.plot()
