$(document).ready(function () {
  $("#btn_translate").on("click", function () {
    let lang = $("#language_code").val();

    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?`,
      method: "GET",
      data: {
        lang: lang,
      },
      success: function (res) {
        $("#hello").text(res.hello);
      },
    });
  });
  $("#language_code").on("keyup", function (event) {
    if (event.key == "Enter") {
      let lang = $("#language_code").val();

      $.ajax({
        url: `https://hellosalut.stefanbohacek.dev/?`,
        method: "GET",
        data: {
          lang: lang,
        },
        success: function (res) {
          $("#hello").text(res.hello);
        },
      });
    }
  });
});
