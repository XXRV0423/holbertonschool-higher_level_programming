fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        var list = document .querySelector('#list_movies');
        data.results.forEach(function(movie) {
            var listItem = document.createElement('li');
            listItem.textContent = movie.title;
            list.appendChild(listItem);
        });
    })
    .catch(function(error) {
        console.log(error);
    });
