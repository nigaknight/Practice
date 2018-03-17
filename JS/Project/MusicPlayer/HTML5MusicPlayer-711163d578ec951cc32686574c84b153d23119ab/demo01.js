var musicControl = document.getElementById("music-stop");
var player = document.getElementById("player");
var fileElement = document.getElementById("file");
musicControl.addEventListener("click", function () {
    if (player.paused) {
        player.play();
    } else {
        player.pause();
    }
});
fileElement.addEventListener("change", function (event) {
    getURL();
});
function getURL() {
    var file = fileElement.files[0];
    var url = URL.createObjectURL(file);
    player.src = url;
    player.play();
}