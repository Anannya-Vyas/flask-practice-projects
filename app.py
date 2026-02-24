from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render_template_index():  
     return render_template('index.html', name='Flask')
     


@app.route('/about')
def render_template_about():
     return render_template('about.html', name='Flask')                    



if __name__ == '__main__':
    app.run(debug=True)