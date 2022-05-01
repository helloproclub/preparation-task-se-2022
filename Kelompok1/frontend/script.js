
function getArticleId() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const articleId = urlParams.get('id');
    return articleId;
}

// tampil menu

function showAll() {
    fetch('https://preparationtask.herokuapp.com/api/articles')
        .then(response => response.json())
        .then(response => {
            const blog = response.data;
            let cards = '';
            blog.reverse().forEach(b => cards += showCards(b));
            const container = document.querySelector('.flex-container');
            container.innerHTML = cards;
        });
}

function showCards(b) {
    return `<a href="show.html?id=${b.id}" class="menu-container" id="${b.id}" data-id="${b.id}">
                <div class="left">
                    <img src="https://${b.thumbnail}">
                </div>
                <div class="right">
                    <h2>${b.title}</h2>
                    <p>${b.description}</p>
                    <p class="small">Created at ${b.createdAt.substring(0, 17)} by ${b.author}</p>
                </div>
            </a>`
}


function showDetails() {
    var articleId = getArticleId();
    fetch('https://preparationtask.herokuapp.com/api/articles/' + articleId)
        .then(response => response.json())
        .then(response => {
            const show = document.querySelector('.show-wrapper');
            show.innerHTML = showDetail(response.data);
        })
}

function showDetail(b) {
    return `<img src="https://${b.thumbnail}">
            <h1>${b.title}</h1>
            <p class="center">by ${b.author}</p>
            <p>${b.content}</p>`
}