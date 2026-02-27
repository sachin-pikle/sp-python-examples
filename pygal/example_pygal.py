import pygal
# from IPython.display import SVG, display

chart = pygal.Bar()
chart.add("A", [1, 3, 3, 7])
chart.add("B", [1, 6, 6, 4])
svg = chart.render()
# display(SVG(svg))
chart.render_to_file('out/bar_chart.svg')