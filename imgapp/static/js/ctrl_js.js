function get_image(id) {
    alert(id);
};

function sortby(glyph, id) {
    var url = document.URL;
    var rgx = /(\w+)!(\w+)!(-?\w*)=([^!]*)!(-?\w*)$/g;
    var params = rgx.exec(url);
    console.log(params);

    var aj = params[1] + "!" + params[2] + "!" + params[3] + "=" + params[4] + "!";
    if(glyph == "glyphicon glyphicon-triangle-top")
        aj += "-";
    aj += id;
    console.log(aj)
    document.location.href = aj;
};

$("#unpbut").click(function() {
    var url = "unprocessed!exact!serial=" + $("#unptxt").val() + "!serial";
    document.location.href = url;
});

$("#pbut").click(function() {
    var url = "processed!exact!serial=" + $("#ptxt").val() + "!serial";
    document.location.href = url;
});

