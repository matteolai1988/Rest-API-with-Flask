#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


# In[2]:
@app.route("/")
def automation_bot():
    return "Automation Bot"




@app.route('/bot/<botname>')
def show_bot_profile(botname):
    return f'User {escape(botname)}'

with app.test_request_context():
    print(url_for('automation_bot'))
    print(url_for('automation_bot', next='/'))
    print(url_for('show_bot_profile', botname='TestBot'))

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)


# In[ ]:


# In[ ]:




