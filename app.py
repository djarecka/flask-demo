import data_stock as ds
from flask import Flask, render_template, request, redirect
import pdb
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components, file_html
from bokeh.io import output_file, save
app = Flask(__name__)

app.vars={}

@app.route('/index',methods=['GET','POST'])
def index():
  #pdb.set_trace()
  if request.method == 'GET':
    return render_template('questions.html')
  else:
    #request was a POST                                                            

    app.vars['ticker'] = request.form['ticker']
    app.vars['cos'] = ds.monthly_data(app.vars['ticker'])
    #pdb.set_trace()
    f = open('test.txt', 'w')
    f.write('Name: %s\n'%(app.vars['ticker']))
    f.close()

    plot = figure(title="plot testowy", x_axis_label='x', y_axis_label='y')
    plot.line([1,2], [3,4])
    app.vars["html"] = file_html(plot, CDN, "my_plot")
    #f_t = open('templates/plot_test.html', 'w')
    #f_t.write(html)
    #f_t.close()

    output_file("templates/plot_test.html", title='My Plot')
    save(plot)

    #app.vars["script"], div = components(plot)
    #return render_template('index.html')
    return redirect('/ploting')

#@app.route('/')
#def main():
#  return redirect('/index')

@app.route('/ploting')
def ploting():
  #pdb.set_trace()
  return render_template("plot.html", skrypt=app.vars["html"], name=app.vars["ticker"]+str(app.vars['cos']))

if __name__ == '__main__':
  app.run(port=33507,debug=True)
