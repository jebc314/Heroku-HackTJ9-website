function call_puzzle(data) {
    console.log(data);
    const Http = new XMLHttpRequest();
       
    const url = '/puzzle?data' + data; 
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        output = Http.responseText;//JSON.parse(Http.responseText);
        console.log(output);
    }
}