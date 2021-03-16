#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### login.py
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name')
    if username == 'grace':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")

