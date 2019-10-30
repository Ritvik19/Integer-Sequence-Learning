function plot(canvasid, plotdata) {
  var ctx = document.getElementById(canvasid);
  var myChart = new Chart(ctx, plotdata);
}

main = document.getElementById('main')
postlist = document.getElementById('postlist')

for (i=0; i < plotdata_.length; i++){
  content = '<div class="w3-card-4 w3-margin w3-white">' +
              '<div class="w3-container">' +
                '<h3><b>'+titles[i]+'</b></h3>' +
              '</div>' +
              '<canvas id="c'+(i)+'"></canvas>' +
            '</div>'
  main.innerHTML += content
  postlist.innerHTML += '<li class="w3-padding-16"><span class="w3-large">'+titles[i]+'</span><br></li>'
  plot('c'+(i), plotdata_[i]);
}
