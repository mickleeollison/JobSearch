#-*- coding: utf-8 -*-
from django import forms
	
class DynForm(forms.Form):    
    """
    Dynamic form that allows the user to change and then verify the data that was parsed
    """
    def setFields(self, kwds):
        """
        Set the fields in the form
        """
        keys = kwds.keys()
        keys.sort()
        for k in keys:
            self.fields[k] = kwds[k]
            
    def setData(self, kwds):
        """
        Set the data to include in the form
        """
        keys = kwds.keys()
        keys.sort()
        for k in keys:
            self.data[k] = kwds[k]
            
    def validate(self, post):
        """
        Validate the contents of the form
        """
        for name,field in self.fields.items():
            try:
                field.clean(post[name])
            except:
                print field.clean(post[name]) 
	
