#!/Users/tomar/Anaconda3/python.exe
"""
Created on Thu Dec 15 23:37:54 2016
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import cgi
'''
this makes you click a google sign-in button.
if you successfully log in, it posts your id and name to gLogin.py
it also forwards along the name of the referring srcApp
NEED TO TEST ONFAILURE!!!!
'''
form = cgi.FieldStorage() # instantiate only once!
srcApp = form.getfirst('srcApp', '')
print("Content-type: text/html \n")
print(''' 
<html><head><title>ToMarLogin</title>
<script src="https://apis.google.com/js/platform.js?onload=renderButton" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
<div id="my-signin2"></div>
<script>
    function onSuccess(googleUser) 
	{
		document.gForm.gId.value = googleUser.getBasicProfile().getId();
		document.gForm.gName.value = googleUser.getBasicProfile().getName();
		document.gForm.submit();
    }
    function onFailure(error) 
	{
      console.log(error);
    }
    function renderButton() 
	{
      gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 240,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
      });
    }
</script>
<form name="gForm" method="POST" action="gAccReq.py">
<input type="hidden" name="gId">
<input type="hidden" name="gName">
<input type="hidden" name="srcApp" value="%s">
</form>
</head>
<body>
<p>
Hello, this is an experimental area of ToMarGames.<br>
Log in with google.<br>
</p>
</body>
<html>
''' % srcApp)
