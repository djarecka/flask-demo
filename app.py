import data_stock as ds
from flask import Flask, render_template, request, redirect
import pdb
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
app = Flask(__name__)

app.vars={}

@app.route('/index',methods=['GET','POST'])
def index():
  #pdb.set_trace()
  if request.method == 'GET':
    return render_template('questions.html')
  else:
    # reading data provided by an user
    app.vars['ticker'] = request.form['ticker']
    app.vars['features'] = request.form.getlist("features")
    # reading requested data from quandl website
    app.vars['data'] = ds.monthly_data(app.vars['ticker'], var_list=app.vars['features'])

    # plotting data using bokeh
    plot = figure(title="data from Quandl WIKI", x_axis_label='date', x_axis_type="datetime")
    colors = ["red", "blue", "green"]
    for i, var in enumerate(app.vars['features']):
      plot.line(app.vars['data']["time"], app.vars['data'][var], color=colors[i], legend=var)
    app.vars["html"] = file_html(plot, CDN, "my_plot")

    return redirect('/ploting')


@app.route('/ploting')
def ploting():
  return render_template("plot.html", skrypt=app.vars["html"], name=app.vars["ticker"])

if __name__ == '__main__':
  app.run(port=33507,debug=True)
