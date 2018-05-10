import os
from app import app
from flask import render_template, redirect, request, session
from javalang.parser import JavaSyntaxError
from utils.file_uploader import upload_file, InvalidFileError
from utils.zip_extract import process_zip

@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(e):
    '''goes back to the home page on standard errors'''
    return redirect('/index')

@app.route('/')
@app.route('/index')
def home_page():
    '''returns the home page for uploading a zip file'''
    error = None
    if session.get('error') is not None:
        error = session['error']

    return render_template('home.html', error=error)

@app.route('/upload', methods=['POST'])
def upload_zip():
    '''uploads a zip file to the server'''
    if request.method == 'POST':
        try:
            filename = upload_file()
            depgraph, coupling = process_zip(filename)
        except InvalidFileError as e:
            session['error'] = 'Invalid file supplied'
            return redirect('/index')
        except JavaSyntaxError as e:
            # javalang unfortunately does not supply particularly robust
            # syntax error information, so this basic error message will have
            # to do for now
            session['error'] = 'Source code contains a syntax error'
            return redirect('/index')

        # successful upload, so deactivate the error message when going back to
        # the home page
        session['error'] = None
        
        session['depgraph'] = depgraph.toJSON()
        session['coupling'] = coupling
        return redirect('analysis')

@app.route('/analysis')
def analysis():
    '''displays the code analysis'''
    # redirect to the home page if the user has not uploaded a file
    if not session.get('depgraph') or not session.get('coupling'):
        return redirect('/index')

    depgraph = session['depgraph']
    nodes = {}
    edges = {}

    # vis.js expects nodes and edges to be referenced by a numeric id, so here
    # the nodes and edges and converted into id's, and stored in a map for easy
    # access
    type_id = 1
    for type, deps in depgraph.iteritems():
        nodes[type] = type_id
        type_id += 1

    for type, deps in depgraph.iteritems():
        type_id  = nodes[type]
        edges[type_id] = [nodes[dep] for dep in deps]

    return render_template('analysis.html',
                    nodes=nodes,
                    edges=edges,
                    coupling=session['coupling'])
