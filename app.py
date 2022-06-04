#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cloud cannot use ipynb, but can download as py
#backend
#do model which can be satisfied first before doing the front&backend
from textblob import TextBlob


# In[2]:


from flask import Flask


# In[3]:


#throw out html - render template
#request - take data from any website
from flask import render_template, request


# In[4]:


app = Flask (__name__) #usually use app
#in python the underscrollx2 something underscrollx2 means the word is special and we cant use in variable
#to confirm is our program


# In[5]:


@app.route("/",methods=["GET","POST"]) #@sign means that you want to put this object call route (function of the object call route), you wan tot embed inside the function
#before you run the function, you want to do certain action
def index():
    #in general when u run to run an app, name is app.py
    if request.method == "POST": #nwill execute this statament when press enter, then will send text file from front end to back end using post
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment(text)
        return(render_template("index.html",result=r))
    else: #before you press enter wil come here first
        return(render_template("index.html",result="waiting...."))
        


# In[ ]:


if __name__== "__main__":
    app.run() #moment you want to run the program
    #you cant run other's ppl program, to protect cloud from running illegal software


# In[ ]:





# In[ ]:





# In[ ]:




