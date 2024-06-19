from flask import Flask, render_template
import inspect
import warnings

# Compatibility layer for inspect.getargspec()
if not hasattr(inspect, 'getargspec'):
    def getargspec(func):
        warnings.warn(
            "inspect.getargspec() is deprecated, use inspect.getfullargspec() instead",
            DeprecationWarning,
            stacklevel=2
        )
        return inspect.getfullargspec(func)

    inspect.getargspec = getargspec

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/Payments')
def Pricing():
    return render_template('Payments.html')

if __name__ == '__main__':
    app.run(debug=True)
