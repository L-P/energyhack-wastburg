function energy_graph(url){
  var ajaxGraph = new Rickshaw.Graph.Ajax( {

    element: document.getElementById("graph"),
    width: 400,
    height: 200,
    renderer: 'line',
    dataURL: url,
    onData: function(d) { d[0].data[0].y = 80; return d },
    series: [
      {
        name: 'New York',
        color: '#c05020',
      }, {
        name: 'London',
        color: '#30c020',
      }, {
        name: 'Tokyo',
        color: '#6060c0'
      }
    ]
  } );
}
