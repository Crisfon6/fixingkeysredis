function onSubmit(){
    let address  = document.getElementById("Address").value;
    let port = document.getElementById("port").value;
    let dbsc = document.getElementById("dbSc").value;
    let dbdest = document.getElementById("dbDest").value;
    eel.transform(address,port,dbsc,dbdest)
}