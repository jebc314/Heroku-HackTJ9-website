function call_puzzle(data) {
    console.log(data);
    const Http = new XMLHttpRequest();
       
    const url = '/puzzle?difficulty='+data['difficulty']+'&piecescount='+data['piecescount']; 
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4 && Http.status == 200) {
            output = JSON.parse(Http.responseText);
            console.log(output);
        }
    }
}