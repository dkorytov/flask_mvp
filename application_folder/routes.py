from flask import render_template, request, redirect
from application_folder import flask_instance


@flask_instance.route('/', methods=['POST', 'GET'])
@flask_instance.route('/index', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('lang')
        framework = request.form.get('frame')
        color = request.form.get('color')
        
        #### Model goes here 
        print('Input params:', language, framework, color)


    
        ### model output goes here
        template_dict = {
            'lang' : language,
            'frame' : framework,
            'color' : color,
            'full_string': language+framework+color, 
            }
        return render_template('test_results.html', **template_dict)
    
        # return '''<h1>The language value is: {}</h1>
        #           <h1>The framework value is: {}</h1>
        # <h1>Color selected: {} </h1>'''.format(language, framework, color)

    colors = ['red', 'blue', 'cyan']
    return render_template('test.html', colors=colors)



### OLD stuff here, ignore it

@flask_instance.route('/index_old')
def index():
    user = {'username': 'Dan'}
    # render template assumes the file is in "templates/*given_filename.html*
    colors = {'a', 'b', 'c'}
    return render_template('index.html', title='My own title', user=user, colors=colors)

@flask_instance.route('/index_old2', methods=['POST', 'GET'])
def index2():
    # if request.method == 'POST':
    #     user = request.form['nm']
    #     print(user)
    #     return "hey1"
    # else:
    #     return 
    #     user = request.args.get('nm')
    #     return "hey2"
    user = {'username': 'Dan'}
    # render template assumes the file is in "templates/*given_filename.html*
    colors = {'a', 'b', 'c'}
    x=request.args.get('x')
    y=request.args.get('y')
    return str(int(x)+2+3*int(y))
    print(x)
    return render_template('index2.html', title='My own title', user=user, colors=colors)
