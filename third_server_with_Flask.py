#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request


# In[ ]:


app = Flask(__name__)

@app.route('/automation_bot', methods=['GET', 'POST'])
def automation_bot():
    if request.method == 'POST':
        return "Doing the automation"
    else:
        return "I can do the automations"
    
if __name__ =='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

