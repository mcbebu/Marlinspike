import webview
from GIS import createhtml

Exsimilar = {
    'x': [-6.215555671220000],
    'y': [106.22891070606781],
    'desc': ["Additional Infomation"]}
Exlocation = (-6.215555671198995, 106.28891070606781)

createhtml(Exlocation, Exsimilar)
with open('App UI.html', 'r') as thehtml:
    thetext = thehtml.read()
    print(thetext)
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
        }
      </script>
<form onsubmit="download(this['name'].value, this['text'].value)">
      <textarea rows=3 cols=50 name="text">Ninja Advice. </textarea>
      <input type="submit" value="Download">
    </form></body>''')
    thetext="".join(textlist)
with open('App UI.html', 'w') as thehtml:
    thehtml.write(thetext)

webview.create_window("MAP", 'App UI.html')
webview.start()