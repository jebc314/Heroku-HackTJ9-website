function call_puzzle(data) {
    // Make they don't try to save before process is finished
    $("#save_button").prop('disabled', true);

    console.log(data);
    const Http = new XMLHttpRequest();
       
    const url = '/puzzle?difficulty='+data['difficulty']+'&piecescount='+data['piecescount']; 
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        if (Http.readyState == 4 && Http.status == 200) {
            output = JSON.parse(Http.responseText);
            console.log(output);
            $("#piece_image").attr("src", '/static/' + output['png'])
            $("#save_button").attr("file_location", '/static/' + output['stl'])
            $("#name_text").text(output['name'])
        }
    }

    var amount = 0;
    var id;

    id = setInterval(function(){
        $('#progress').attr("style", "width: "+ amount + "%");
        $("#progress").attr("aria-valuenow", amount);

        if (amount == 100) {
            $("#save_button").prop('disabled', false);
            clearInterval(id);
        }

        amount += 2;        
    }, 10);
}

function save_stl() {
    const downloadToFile = (file_location, filename, contentType) => {
        const a = document.createElement('a');
        
        a.href= file_location;
        a.download = filename;
        a.click();
        
        URL.revokeObjectURL(a.href);
        };

        file_location = $('#save_button').attr("file_location")
        file_name = file_location.slice(file_location.indexOf("/")+1);

        downloadToFile(file_location, file_name, 'application/STL');
    
}

function load_puzzle(name) {
    $("#piece_image").attr("src", '/static/files/' + name + ".png")
    $("#save_button").attr("file_location", '/static/files/' + name + ".stl")
    $("#name_text").text(name)
    $("#save_button").prop('disabled', false);
}

function search(ele) {
    if(event.key === 'Enter') {
        load_puzzle(ele.value);      
    }
}