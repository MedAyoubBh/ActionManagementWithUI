function show(c){
    if (c.checked){
        document.querySelector('.timeInterval').style.display = "block";
    }else{
        document.querySelector('.timeInterval').style.display = "none";
    }
}

function selectAll(c){
    if (c.checked){
        document.querySelector('.resp').style.display = "none";
    }else{
        document.querySelector('.resp').style.display = "block";
    }
}