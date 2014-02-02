function energy_flot(url){
  console.info("Flot from "+url);

  var options = {
    xaxis: {
      mode: "time",
      minTickSize: [1, "month"],
      timeformat: "%m/%Y",
    },
    "lines": {"show": "true"},
    clickable:true,
    hoverable: true
  };

  $.ajax({
    url: url,
    type: "GET",
    dataType: "json",
    success: function(data){
      $.plot("#placeholder", data, options);
    }
  });


}

function energy_graph(url){
  var time = new Rickshaw.Fixtures.Time();
  var days = time.unit('month');

  var graph = new Rickshaw.Graph.Ajax( {
    element: document.getElementById('chart'),
    renderer: 'line',
    dataURL: url,
    onData: function(d) {
      Rickshaw.Series.zeroFill(d);
      return d;
    },
  } );
  graph.render();

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

}
