function plot(i) {
  document.getElementById('head').innerHTML = titles[i];
  var xhttp = new XMLHttpRequest();
  var filepath = 'data/data.json'
  console.log(filepath)
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     plotdata = JSON.parse(this.responseText)[i];
     var mychart = new Chart(document.getElementById('chart'), plotdata);
    }
  };
  xhttp.open("GET", filepath, true);
  xhttp.send();

}

main = document.getElementById('main')
postlist = document.getElementById('postlist')

for (i=0; i < titles.length; i++)
{
  postlist.innerHTML += '<li class="w3-padding-16" onclick="plot('+i+')"><span class="w3-large">'+titles[i]+'</span><br></li>';
}
