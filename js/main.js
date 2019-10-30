var c00= '#1f77b4', c01= '#ff7f0e', c02= '#2ca02c', c03= '#d62728', c04= '#9467bd';
var c05= '#8c564b', c06= '#e377c2', c07= '#7f7f7f', c08= '#bcbd22', c09= '#17becf';
var c10= '#aec7e8', c11= '#ffbb78', c12= '#98df8a', c13= '#ff9896', c14= '#c5b0d5';
var c15= '#c49c94', c16= '#f7b6d2', c17= '#c7c7c7', c18= '#dbdb8d', c19= '#9edae5';

function plot(canvasid, plotdata) {
  var ctx = document.getElementById(canvasid);
  var myChart = new Chart(ctx, plotdata);
}
plotdata = {
  type: 'bar',
  data: {
      labels: ["Android Studio", "Atom", "Coda", "Eclipse", "Emacs", "IPython / Jupyter", "IntelliJ", "Komodo", "Light Table", "NetBeans", "Notepad++", "PHPStorm", "PyCharm", "RStudio", "RubyMine", "Sublime Text", "TextMate", "Vim", "Visual Studio", "Visual Studio Code", "Xcode", "Zend"],
      datasets: [{
          label: 'Counts',
          data: [14787, 11636, 578, 12591, 3922, 8317, 22166, 368, 178, 5121, 26621, 6645, 11724, 2940, 1202, 20424, 805, 22163, 27490, 44311, 8239, 307],
          backgroundColor: c10,
          borderColor: c00,
          borderWidth: 1
      },
    ]
  },
  options: {
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      }
  }
}

plot('c01', plotdata)
