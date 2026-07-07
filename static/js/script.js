// ===========================================================
// MovieRec AI
// ===========================================================

const movieInput = document.getElementById("movie");
const recommendBtn = document.getElementById("recommendBtn");

const suggestionBox = document.getElementById("suggestions");

const recommendationContainer =
document.getElementById("recommendationContainer");

const loading =
document.getElementById("loading");

// ==============================================
// SEARCH SUGGESTIONS
// ==============================================

movieInput.addEventListener("input", async () => {

    const query = movieInput.value.trim();

    suggestionBox.innerHTML = "";

    if(query.length < 2)
        return;

    try{

        const response = await fetch(

            `/search?q=${encodeURIComponent(query)}`

        );

        const movies = await response.json();

        movies.forEach(movie=>{

            const div=document.createElement("div");

            div.className="suggestion";

            div.textContent=movie;

            div.onclick=()=>{

                movieInput.value=movie;

                suggestionBox.innerHTML="";

            }

            suggestionBox.appendChild(div);

        });

    }

    catch(error){

        console.log(error);

    }

});

// ==============================================
// ENTER KEY
// ==============================================

movieInput.addEventListener(

"keydown",

function(e){

    if(e.key==="Enter"){

        e.preventDefault();

        recommend();

    }

}

);

// ==============================================
// BUTTON
// ==============================================

recommendBtn.addEventListener(

"click",

recommend

);

// ==============================================
// RECOMMEND
// ==============================================

async function recommend(){

    const movie=movieInput.value.trim();

    if(movie===""){

        alert("Enter a movie name.");

        return;

    }

    loading.style.display="block";

    recommendationContainer.innerHTML="";

    const formData=new FormData();

    formData.append(

        "movie",

        movie

    );

    try{

        const response=

        await fetch(

        "/recommend",

        {

            method:"POST",

            body:formData

        }

        );

        const data=

        await response.json();

        loading.style.display="none";

        if(data.status==="error"){

            alert(data.message);

            return;

        }

        renderMovies(

            data.recommendations

        );

        document.getElementById("recommendations")

            .scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

    }

    catch(error){

        loading.style.display="none";

        console.log(error);

        alert("Something went wrong.");

    }

}

// ==============================================
// RENDER MOVIES
// ==============================================

function renderMovies(movies){

    recommendationContainer.innerHTML="";

    movies.forEach(movie=>{

        recommendationContainer.appendChild(

            createCard(movie)

        );

    });

}

// ==============================================
// CARD
// ==============================================

function createCard(movie){

    const card=document.createElement("div");

    card.className="movie-card";

    const score=Math.round(movie.score*100);

    const overview=

    movie.overview.length>180

    ?

    movie.overview.substring(0,180)+"..."

    :

    movie.overview;

    let genres="";

    if(Array.isArray(movie.genres)){

        movie.genres.slice(0,3).forEach(g=>{

            genres+=

            `<span class="badge">${g}</span>`;

        });

    }

    card.innerHTML=`

<div class="poster-placeholder">

    <div class="poster-icon">🎬</div>

    <div class="poster-title">
        ${movie.title}
    </div>

</div>

<div class="movie-info">

<h3>

${movie.title}

</h3>

<div class="badges">

${genres}

</div>

<div class="meta">

<div class="rating">

⭐ ${movie.vote_average}

</div>

<div class="director">

🎬 ${movie.director}

</div>

</div>

<div class="overview">

${overview}

</div>

<div class="score-bar">

<div

class="score-fill"

style="width:${score}%">

</div>

</div>

<div class="score-text">

${score}% Match

</div>

<div class="card-buttons">

<button

class="card-btn primary-btn">

More Info

</button>

<button

class="card-btn secondary-btn">

❤ Save

</button>

</div>

</div>

`;

    return card;

}

// ==============================================
// HIDE SUGGESTIONS
// ==============================================

document.addEventListener(

"click",

function(e){

    if(e.target!==movieInput)

        suggestionBox.innerHTML="";

}

);

async function loadTrending(){

    const response = await fetch("/trending");

    const movies = await response.json();

    const row = document.querySelector(".poster-row");

    row.innerHTML="";

    movies.forEach(movie=>{

        row.innerHTML+=`

        <div class="poster-placeholder">

            <div class="poster-icon">

            🎬

            </div>

            <div class="poster-title">

            ${movie.title}

            </div>

            <div style="margin-top:15px">

            ⭐ ${movie.rating}

            </div>

        </div>

        `;

    });

}

loadTrending();