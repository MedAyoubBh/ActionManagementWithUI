function show(){
    if (document.getElementById('periode').checked){
        document.querySelector('.timeInterval').style.display = "block";
    }else{
        document.querySelector('.timeInterval').style.display = "none";
    }
}

function selectAll(){
    if (document.getElementById('tousResp').checked){
        document.querySelector('.resp').style.display = "none";
    }else{
        document.querySelector('.resp').style.display = "block";
    }
}