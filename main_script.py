import data_base
from flask import Flask, render_template
name_server = 'Script_html'
site = Flask(name_server)

@site.route('/')
def index():
    return render_template('index.html')

@site.route('/execute_script')
def execute_script():
    # Your Python script logic here
    result = "Python script executed!"
    return result

if __name__ == '__main__':
    site.run(debug=True, host='0.0.0.0')
