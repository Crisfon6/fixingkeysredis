async function onSubmit(){
    let address  = document.getElementById("address").value;
    let port = document.getElementById("port").value;
    let dbsc = document.getElementById("dbSc").value;
    let dbdest = document.getElementById("dbDest").value;
    let dbdestwrong = document.getElementById("dbDestWrong").value;
    await eel.transform(address,port,dbsc,dbdest,dbdestwrong)
}
eel.expose(working);
function working(work){
    if(work==1){
        alert("Working...")
    }
    if(work==0){
        alert("Finish!")
    }
}
eel.expose(error)
function error(err){
    alert(err)
}