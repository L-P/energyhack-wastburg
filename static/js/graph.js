function energy_graph(url){
  var time = new Rickshaw.Fixtures.Time();
  var days = time.unit('month');

  var graph = new Rickshaw.Graph.Ajax( {
    element: document.getElementById('graph'),
    renderer: 'line',
    stroke : true,
    dataURL: url,
    onData: function(d) {
      Rickshaw.Series.zeroFill(d);
      return d;
    },
  } );

  new Rickshaw.Graph.Axis.Time({
    graph: graph
  });


  var hoverDetail = new Rickshaw.Graph.HoverDetail( {
    graph: graph
  } );

  var legend = new Rickshaw.Graph.Legend( {
    graph: graph,
    element: document.getElementById('legend')
  } );

  var shelving = new Rickshaw.Graph.Behavior.Series.Toggle( {
    graph: graph,
    legend: legend
  } );

  var axes = new Rickshaw.Graph.Axis.Time( {
    graph: graph
  } );
  axes.render();

  graph.render();
}
