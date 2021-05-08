/** @format */

function createManga(completed_manga) {
    c_manga = JSON.parse(completed_manga);
    console.log(c_manga);
    let container = document.getElementById("manga-container");
    for (manga in c_manga) {
        var img = document.createElement("img");
        var div = document.createElement("div");
        var title = document.createElement("a");

        img.src = `https://mangakakalot.tv/mangaimage/${c_manga[manga]._id}.jpg`;
        // img.width = 200;
        // img.height = 300;

        title.innerHTML = c_manga[manga].manga_title;
        title.className = "title";

        div.className = "manga";

        img.id = manga;
        title.href = `/manga/${c_manga[manga]._id}`;
        div.id = manga;
        img.onclick = (elem) => {
            location.href = `/manga/${c_manga[elem.target.id]._id}`;
        };
        div.appendChild(img);
        div.appendChild(title);
        container.appendChild(div);
    }
}

function mangaPage(manga) {
    manga = JSON.parse(manga);
    console.log(manga);
    let container = document.getElementById("manga-info");

    let img = document.createElement("img");
    let summary = document.createElement("p");
    let div = document.createElement("div");
    let title = document.createElement("h1");
    let ul = document.createElement("ul");

    img.src = `https://mangakakalot.tv/mangaimage/${manga._id}.jpg`;

    title.innerHTML = manga.manga_title;
    title.className = "title";

    summary.innerHTML = manga.summary;

    div.className = "manga-info";

    for (chapter in manga.chapters) {
        let li = document.createElement("li");
        let a = document.createElement("a");

        a.href = "?page=" + chapter;
        a.text = chapter;
        li.appendChild(a);
        ul.appendChild(li);
    }

    img.id = manga._id;
    title.id = manga._id;
    div.id = manga._id;

    div.appendChild(title);
    div.appendChild(img);
    div.appendChild(summary);
    div.appendChild(ul);
    container.appendChild(div);
}

let p = 0;
function displayMangaPages(manga) {
    p = 0;
    manga = JSON.parse(manga);
    console.log(manga.manga_pages);
    // let container = document.getElementById("manga-pages");
    let container = document.getElementById("container");
    let img = document.getElementById("single-page");
    let scrollviewdiv = document.createElement("div");
    scrollviewdiv.id = "scroll-view";

    img.hidden = true;
    scrollviewdiv.hidden = true;

    // let pageCounter = document.createElement("p");
    container.appendChild(scrollviewdiv);

    // Scroll View
    for (page_url in manga.manga_pages) {
        let img = document.createElement("img");
        img.src = manga.manga_pages[page_url];
        scrollviewdiv.appendChild(img);
    }

    // Single View
    img.src = manga.manga_pages[0];
    img.onclick = () => {
        console.log("click");
        p++;
        document.getElementById("single-page").src = manga.manga_pages[p];
    };
}

function toggle() {
    let singleView = document.getElementById("single-page");
    let scrollView = document.getElementById("scroll-view");

    singleView.hidden = !singleView.hidden;
    scrollView.hidden = !scrollView.hidden;
    console.log(singleView.hidden, scrollView.hidden);
}
// function toggleView(){
//     let button =
// }
