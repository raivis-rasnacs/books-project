
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
        clearTable();
        putNewData(data);
    })
}

function clearTable() {
    const bookRows = document.getElementsByClassName("bookRow");

    while (bookRows.length > 0) {
        bookRows[0].remove();
    }
}

function putNewData(data) {
    const books = data["response"]["books"];

    for (let i = 0; i < books.length; i++) {
        const rinda = document.createElement("tr");
        rinda.classList.add("bookRow");
        const lauksNosaukumam = document.createElement("td");
        lauksNosaukumam.innerHTML = books[i]["book_name"];
        const lauksAutoram = document.createElement("td");
        lauksAutoram.innerHTML = books[i]["author"];
        const lauksLappusem = document.createElement("td");
        lauksLappusem.innerHTML = books[i]["pages"];
        const lauksZanram = document.createElement("td");
        lauksZanram.innerHTML = books[i]["genre_name"];
        const lauksNovertesanai = document.createElement("td");
        lauksNovertesanai.insertAdjacentHTML(
            "beforeend",
            `<div class="stars">
            <a 
                href="/set_rating?book_id=${books[i]["book_id"]}&value=1"
                class="bi bi-star"
                onmouseover="animate_stars(this, this.parentElement);"
                onmouseleave="hide_animation(this.parentElement);">
            </a>
            <a 
                href="/set_rating?book_id=${books[i]["book_id"]}&value=2"
                class="bi bi-star"
                onmouseover="animate_stars(this, this.parentElement);"
                onmouseleave="hide_animation(this.parentElement);">
            </a>
            <a 
                href="/set_rating?book_id=${books[i]["book_id"]}&value=3"
                class="bi bi-star"
                onmouseover="animate_stars(this, this.parentElement);"
                onmouseleave="hide_animation(this.parentElement);">
            </a>
            <a 
                href="/set_rating?book_id=${books[i]["book_id"]}&value=4"
                class="bi bi-star"
                onmouseover="animate_stars(this, this.parentElement);"
                onmouseleave="hide_animation(this.parentElement);">
            </a>
            <a 
                href="/set_rating?book_id=${books[i]["book_id"]}&value=5"
                class="bi bi-star"
                onmouseover="animate_stars(this, this.parentElement);"
                onmouseleave="hide_animation(this.parentElement);">
            </a>
        </div>`
        );
        const lauksReitingam = document.createElement("td");
        lauksReitingam.innerHTML = books[i]["average_rating"].toFixed(1);
        rinda.append(
            lauksNosaukumam,
            lauksAutoram,
            lauksLappusem,
            lauksZanram,
            lauksNovertesanai,
            lauksReitingam
        );
        const tabula = document.getElementById("gramatuTabula");
        const tbody = tabula.getElementsByTagName("tbody")[0];
        tbody.append(rinda);
    }
}