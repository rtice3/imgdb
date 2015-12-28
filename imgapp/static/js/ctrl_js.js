function get_image(id) {
    alert(id);
};

function sortby() {

};

$("#unpbut").click(function() {
    var url = "unprocessed=" + $("#unptxt").val() + "/serial_search/";
    document.location.href = url;
});

$("#pbut").click(function() {
    var url = "processed=" + $("#ptxt").val() + "/serial_search/";
    document.location.href = url;
});