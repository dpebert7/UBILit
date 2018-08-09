from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

#ADDED
#from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
import pandas as pd
from collections import defaultdict
from bokeh.plotting import show, figure
from bokeh.models import ColumnDataSource, HoverTool



# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

#from bokeh.plotting import figure
#from bokeh.resources import CDN
#from bokeh.embed import file_html



def ubi_chart(request):
    data = pd.read_csv("3_year_data.csv", index_col = False)
    data = data.dropna()


    data_dict = defaultdict(list)
    for index in list(data.index):
        data_dict["Years"].append([2015, 2016, 2017])
        data_dict["2015"].append([data.ix[index]['2015']])
        data_dict["2016"].append([data.ix[index]['2016']])
        data_dict["2017"].append([data.ix[index]['2017']])
        data_dict["Sold"].append([data.ix[index]['2015'], data.ix[index]['2016'], data.ix[index]['2017']])
        data_dict["Color"].append(['red' if data.ix[index]['Category'] == "Zulu" else 'blue'])
        data_dict["Title"].append([data.ix[index]['Title']])
        data_dict["Category"].append([data.ix[index]['Category']])

    source = ColumnDataSource(data_dict)

    q = figure(plot_height=600, plot_width=1000,
               x_axis_label='Year', y_axis_label="Books sold",
               x_range=(2015, 2017), y_range=(0,1800))
    q.multi_line(xs="Years", ys="Sold", line_width=3, line_color='Color',
                 line_alpha=0.6,
                 hover_line_color='black', hover_line_alpha=1.0,
                 source=source)

    q.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[
        ('Title', '@Title'),
        ('Category', '@Category'),
        ('2015', '@2015'),
        ('2016', '@2016'),
        ('2017', '@2017')
    ]))

    script, div = components(q, CDN)

    return render(request, "ubi_chart.html", {"the_script": script, "the_div": div})
