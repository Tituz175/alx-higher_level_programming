$.ajax({
  url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
  method: "GET",
  success: function (res) {
    $("#hello").text(res.hello);
  },
});
