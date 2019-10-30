function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  return result;
}

function plot(canvasid, plotdata) {
  var ctx = document.getElementById(canvasid);
  var myChart = new Chart(ctx, plotdata);
}


main = document.getElementById('main')

for (i=0; i < plotdata_.length; i++){
  content = '<div class="w3-card-4 w3-margin w3-white">' +
              '<div class="w3-container">' +
                '<h3><b>'+titles[i]+'</b></h3>' +
              '</div>' +
              '<canvas id="c'+(i)+'"></canvas>' +
            '</div>'
  main.innerHTML += content
  plot('c'+(i), plotdata_[i]);
}
