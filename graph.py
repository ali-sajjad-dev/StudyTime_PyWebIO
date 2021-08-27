from pyg2plot import Plot
from pywebio.output import put_html

data = [
  { "year": '2013', "value": 3.7},
  { "year": '2014', "value": 3.1},
  { "year": '2015', "value": 3.5},
  { "year": '2016', "value": 3.2},
  { "year": '2017', "value": 3.6},
  { "year": '2018', "value": 2.9},
  { "year": '2019', "value": 3.1},
  { "year": '2020', "value": 2.9},
  { "year": '2021', "value": 2.7},
]

line = Plot("Line")

line.set_options({
  "appendPadding": 32,
  "data": data,
  "xField": "year",
  "yField": "value",
  "label": {},
  "smooth": True,
  "lineStyle": {
    "lineWidth": 3,
  },
  "point": {
    "size": 5,
    "shape": 'diamond',
    "style": {
      "fill": "white",
      "stroke": "#5B8FF9",
      "lineWidth": 2,
    }
  }
})

put_html(line.render_notebook())