import eel

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('web')

@eel.expose
def transform(address,port,dbsc,dbdest):
    

eel.start('main.html',size=(650, 612))             # Start (this blocks and enters loop)