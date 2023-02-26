import webview
from GIS import createhtml
from time import sleep
import os

Exsimilar = {
    'longitude': [-6.215555671198995],
    'latitude': [106.22891070606781],
    'description': ["Additional Infomation"]}
Exlocation = (-6.216555671198995, 106.23091070606781)
def app(location, similar):
    class Api:
        def __init__(self):
            self._window = None
        def set_window(self, window):
            self._window = window
        def destroy(self):
            print('Destroying window...')
            sleep(3)
            self._window.destroy()
            print('Destroyed!')

    createhtml(location, similar)
    with open('main.html', 'r') as thehtml:
        thetext = thehtml.read()
        textlist = thetext.split("</body>")
        textlist.insert(1, '''<script language="Javascript" >
            function download(filename, text) {
              var pom = document.createElement('a');
              pom.setAttribute('href', 'data:text/plain;charset=utf-8,' +
            encodeURIComponent(text));
              pom.setAttribute('download', filename);
              pom.style.display = 'none';
              document.body.appendChild(pom);
              pom.click();
              document.body.removeChild(pom);
              pywebview.api.destroy();
            }
          </script>
    <form onsubmit="download(this['name'].value, this['text'].value)">
          <textarea rows=3 cols=50 name="text">Ninja Advice. </textarea>
          <input type="submit" value="Download">
        </form></body>''')
        thetext="".join(textlist)
    with open('main.html', 'w') as thehtml:
        thehtml.write(thetext)
    api = Api()
    window = webview.create_window("MAP", 'main.html', js_api=api,)
    api.set_window(window)
    webview.start()
    returnobject = ""
    with open('C:\\Users\\Georgie\\Downloads\\undefined.txt', 'r') as response:
        returnobject = response.read()
    os.remove("C:\\Users\\Georgie\\Downloads\\undefined.txt")
    return returnobject