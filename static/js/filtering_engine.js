
function showFiltered(column) {
    fetch("/filter",
    {
        headers : {
            'Content-Type' : 'application/json'
        },
        "method":"POST",
        "body": JSON.stringify({
            "parameter":column
        })
})
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
}