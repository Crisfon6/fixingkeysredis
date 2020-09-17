import eel
from database import  Database
from  convert import Transform
# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('web')

@eel.expose
def transform(address,port,dbsc,dbdest,dbdestwrong):
    print("inside")    
    eel.working(1)
    try:
        dbnumber = [dbsc,dbdest,dbdestwrong]
        db =  Database(address,port,dbnumber)
        Transform(db)
        eel.working(0)
    except Exception as e:
        eel.error(str(e))
    
    
    

eel.start('main.html',size=(1009, 500))             # Start (this blocks and enters loop)