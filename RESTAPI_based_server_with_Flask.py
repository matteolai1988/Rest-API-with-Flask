#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)

@app.route("/")
def automation_bot():
    return "<p>Automation Bot!</p>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


# In[ ]:




