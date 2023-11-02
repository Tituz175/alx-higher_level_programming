$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  method: "GET",
  success: function (res) {
    res.results.forEach((obj) =>
      $("#list_movies").append(`<li>${obj.title}</li>`)
    );
  },
});
