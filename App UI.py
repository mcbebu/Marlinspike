import webview
from GIS import createhtml
from time import sleep

Exsimilar = {
    'longitude': [-6.215555671220000],
    'latitude': [106.22891070606781],
    'description': ["Additional Infomation"]}
Exlocation = (-6.215555671198995, 106.28891070606781)
def app(location=Exlocation, similar=Exsimilar):
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
    with open('App UI.html', 'r') as thehtml:
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
    with open('App UI.html', 'w') as thehtml:
        thehtml.write(thetext)
    api = Api()
    window = webview.create_window("MAP", 'App UI.html', js_api=api,)
    api.set_window(window)
    webview.start()
    with open('C:\\Users\\Georgie\\Downloads\\undefined.txt', 'r') as response:
        return response.read()