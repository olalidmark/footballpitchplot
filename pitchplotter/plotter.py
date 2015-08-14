import plotly.plotly as py
from plotly.graph_objs import *

__author__ = 'ola'


class Plotter:
    def add_events(self, arr, title):
        xvals, yvals, names, size = zip(*arr)

        trace = Scatter(
            x=xvals,
            y=yvals,
            text=names,
            mode='markers',
            name=title,
            marker=Marker(
                color=u"Black",
                size=size,
                line=Line(width=2, color='white')
            )
        )

        self.traces.append(trace)

    def __init__(self, plot_title):
        self.traces = []

        trace1 = Scatter(
            showlegend=False,
            x=[50, 50],
            y=[100, 0],
            mode='lines',
            line=Line(width=2, color='white')
        )
        self.traces.append(trace1)
        trace2 = Scatter(
            showlegend=False,
            x=[0, 16, 16, 0],
            y=[80, 80, 20, 20],
            mode='lines',
            line=Line(width=2, color='white'),

        )
        self.traces.append(trace2)
        trace3 = Scatter(
            showlegend=False,
            x=[100, 84, 84, 100],
            y=[80, 80, 20, 20],
            mode='lines',
            line=Line(width=2, color='white')
        )
        self.traces.append(trace3)

        self.layout = Layout(
            title=plot_title,
            hovermode='closest',
            autosize=True,
            width=1000,
            height=850,
            plot_bgcolor='green',
            xaxis=XAxis(
                range=[0, 100],
                showgrid=False,
                showticklabels=False
            ),
            yaxis=YAxis(
                range=[0, 100],
                showgrid=False,
                showticklabels=False
            ),
            annotations=Annotations([
                Annotation(
                    x=0,
                    y=0,
                    xref='x',
                    yref='y',
                    xanchor='left',
                    yanchor='top',
                    text='generated with help from: stryktipsetisistastund.se',
                    showarrow=False

                )
            ])
        )

    def plot(self):
        fig = Figure(data=self.traces, layout=self.layout)
        unique_url = py.plot(fig)