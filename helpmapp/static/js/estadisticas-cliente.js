

// entrada = $(".datosOcultos");
//     datos = entrada.attr("value");
//     lista = datos.split("-");
//     console.log(lista);

//     comida=parseInt(lista[0]);
//     ropa=parseInt(lista[1]);
//     agua=parseInt(lista[2]);
//     lista2=[comida,ropa,agua];
//     var employees = [
//   {dept: 'comida', age :comida},
//   {dept: 'ropa', age : ropa},
//   {dept: 'agua', age : agua},
 

// ];

// console.log(employees);

// var svgHeight = 400;
// var svgWidth = 400;
// var maxAge = Math.max.apply(Math,lista2);
// //var maxAge=500;
// maxAge+=10; // You can also compute this from the data
// var barSpacing = 1; // The amount of space you want to keep between the bars
// var padding = {
//     left: 20, right: 0,
//     top: 20, bottom: 20
// };

function animateBarsUp() {
    
   console.log("accedí a la función!") // sanity check
    $.ajax({
        url : "http://127.0.0.1:8000/datos/", // the endpoint
        type:"get",

        // handle a successful response
        success : function(json) {
            
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
   
        
  var employees=json["cantidad_ropa"]
  var svgHeight = 400;
    var svgWidth = 400;
    var maxAge = json["max_ropa"]


    maxAge+=10; // You can also compute this from the data
    var barSpacing = 1; // The amount of space you want to keep between the bars
    var padding = {
    left: 20, right: 0,
    top: 20, bottom: 20
    };

    var maxWidth = svgWidth - padding.left - padding.right;
    var maxHeight = svgHeight - padding.top - padding.bottom;

  // Define your conversion functions
  var convert = {    
    x: d3.scale.ordinal(),
    y: d3.scale.linear()
  };

  // Define your axis
  var axis = {
    x: d3.svg.axis().orient('bottom'),
    y: d3.svg.axis().orient('left')
  };
    
  // Define the conversion function for the axis points
  axis.x.scale(convert.x);
  axis.y.scale(convert.y);

  // Define the output range of your conversion functions
  convert.y.range([maxHeight, 0]);
  convert.x.rangeRoundBands([0, maxWidth]);
    
  // Once you get your data, compute the domains
  convert.x.domain(employees.map(function (d) {
      return d.dept;
    })
  );
  convert.y.domain([0, maxAge]);

  // Setup the markup for your SVG
  var svg = d3.select('.chart')
    .attr({
        width: svgWidth,
        height: svgHeight
    });
  
  // The group node that will contain all the other nodes
  // that render your chart
  var chart = svg.append('g')
    .attr({
        transform: function (d, i) {
          return 'translate(' + 29 + ',' + 20 + ')';
        }
      });
    
  chart.append('g') // Container for the axis
    .attr({
      class: 'x axis',
      transform: 'translate(0,' + maxHeight + ')'
    })
    .call(axis.x); // Insert an axis inside this node

  chart.append('g') // Container for the axis
    .attr({
      class: 'y axis',
      height: maxHeight
    })
    .call(axis.y); // Insert an axis inside this node

  var bars = chart
    .selectAll('g.bar-group')
    .data(employees)
    .enter()
    .append('g') // Container for the each bar
    .attr({
      transform: function (d, i) {
        return 'translate(' + convert.x(d.dept) + ', 0)';
      },
      class: 'bar-group'
    });

  bars.append('rect')
        .attr({
        y: maxHeight,
        height: 0,
        width: function(d) {return convert.x.rangeBand(d) - 1;},
        class: 'bar'
    })
    .transition()
    .duration(1500)
    .attr({
      y: function (d, i) {
        return convert.y(d.age);
      },
      height: function (d, i) {
        console.log(d.age);
        return maxHeight - convert.y(d.age);

      }
    });



       
  var employees=json["cantidad_comida"]
  var svgHeight = 400;
  var svgWidth = 400;
  var maxAge = json["max_comida"]


    maxAge+=10; // You can also compute this from the data
    var barSpacing = 1; // The amount of space you want to keep between the bars
    var padding = {
    left: 20, right: 0,
    top: 20, bottom: 20
    };

    var maxWidth = svgWidth - padding.left - padding.right;
    var maxHeight = svgHeight - padding.top - padding.bottom;

  // Define your conversion functions
  var convert = {    
    x: d3.scale.ordinal(),
    y: d3.scale.linear()
  };

  // Define your axis
  var axis = {
    x: d3.svg.axis().orient('bottom'),
    y: d3.svg.axis().orient('left')
  };
    
  // Define the conversion function for the axis points
  axis.x.scale(convert.x);
  axis.y.scale(convert.y);

  // Define the output range of your conversion functions
  convert.y.range([maxHeight, 0]);
  convert.x.rangeRoundBands([0, maxWidth]);
    
  // Once you get your data, compute the domains
  convert.x.domain(employees.map(function (d) {
      return d.dept;
    })
  );
  convert.y.domain([0, maxAge]);

  // Setup the markup for your SVG
  var svg = d3.select('.chart2')
    .attr({
        width: svgWidth,
        height: svgHeight
    });
  
  // The group node that will contain all the other nodes
  // that render your chart
  var chart = svg.append('g')
    .attr({
        transform: function (d, i) {
          return 'translate(' + 40 + ',' + 19 + ')';
        }
      });
    
  chart.append('g') // Container for the axis
    .attr({
      class: 'x axis',
      transform: 'translate(0,' + maxHeight + ')'
    })
    .call(axis.x); // Insert an axis inside this node

  chart.append('g') // Container for the axis
    .attr({
      class: 'y axis',
      height: maxHeight
    })
    .call(axis.y); // Insert an axis inside this node

  var bars = chart
    .selectAll('g.bar-group')
    .data(employees)
    .enter()
    .append('g') // Container for the each bar
    .attr({
      transform: function (d, i) {
        return 'translate(' + convert.x(d.dept) + ', 0)';
      },
      class: 'bar-group'
    });

  bars.append('rect')
        .attr({
        y: maxHeight,
        height: 0,
        width: function(d) {return convert.x.rangeBand(d) - 1;},
        class: 'bar'
    })
    .transition()
    .duration(1500)
    .attr({
      y: function (d, i) {
        return convert.y(d.age);
      },
      height: function (d, i) {
        console.log(d.age);
        return maxHeight - convert.y(d.age);

      }
    });


// GRAFICA PARA AGUA POR CANTOOOOOOOOOON
  
  var employees=json["agua_canton"]
  var svgHeight = 400;
  var svgWidth = 400;
  var maxAge = json["max_agua"]


    maxAge+=10; // You can also compute this from the data
    var barSpacing = 1; // The amount of space you want to keep between the bars
    var padding = {
    left: 20, right: 0,
    top: 20, bottom: 20
    };

    var maxWidth = svgWidth - padding.left - padding.right;
    var maxHeight = svgHeight - padding.top - padding.bottom;

  // Define your conversion functions
  var convert = {    
    x: d3.scale.ordinal(),
    y: d3.scale.linear()
  };

  // Define your axis
  var axis = {
    x: d3.svg.axis().orient('bottom'),
    y: d3.svg.axis().orient('left')
  };
    
  // Define the conversion function for the axis points
  axis.x.scale(convert.x);
  axis.y.scale(convert.y);

  // Define the output range of your conversion functions
  convert.y.range([maxHeight, 0]);
  convert.x.rangeRoundBands([0, maxWidth]);
    
  // Once you get your data, compute the domains
  convert.x.domain(employees.map(function (d) {
      return d.dept;
    })
  );
  convert.y.domain([0, maxAge]);
  var svg = d3.select('.chart3')
    .attr({
        width: svgWidth,
        height: svgHeight
    });
  
  // The group node that will contain all the other nodes
  // that render your chart
  var chart = svg.append('g')
    .attr({
        transform: function (d, i) {
          return 'translate(' + 40 + ',' + 19 + ')';
        }
      });
    
  chart.append('g') // Container for the axis
    .attr({
      class: 'x axis',
      transform: 'translate(0,' + maxHeight + ')'
    })
    .call(axis.x); // Insert an axis inside this node

  chart.append('g') // Container for the axis
    .attr({
      class: 'y axis',
      height: maxHeight
    })
    .call(axis.y); // Insert an axis inside this node

  var bars = chart
    .selectAll('g.bar-group')
    .data(employees)
    .enter()
    .append('g') // Container for the each bar
    .attr({
      transform: function (d, i) {
        return 'translate(' + convert.x(d.dept) + ', 0)';
      },
      class: 'bar-group'
    });

  bars.append('rect')
        .attr({
        y: maxHeight,

        height: 0,
        width: function(d) {return convert.x.rangeBand(d) - 1;},
        class: 'bar'
    })
    .transition()
    .duration(1500)
    .attr({
      y: function (d, i) {
        return convert.y(d.age);
      },
      height: function (d, i) {
        console.log(d.age);
        return maxHeight - convert.y(d.age);

      }
    });
   
        },

        // handle a non-successful response
        error : function(data) {
            
            console.log("oh no :("); // provide a bit more info about the error to the console
        }
    });
  
}




$(window).load(function() {
  animateBarsUp();

});