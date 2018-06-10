google.charts.load('current', {packages: ['corechart', 'bar']});
        google.charts.setOnLoadCallback(drawAxisTickColors);

        function drawAxisTickColors(red = 0, green = 0, blue = 0) {

           var data = google.visualization.arrayToDataTable([
             ['Element', 'Density', { role: 'style' } ],
             ['Red', red, 'red' ],
             ['Green', green, 'green' ],
             ['Blue', blue, 'blue' ]
          ]);

          var options = {
            titlePosition: 'none',
            hAxis: {
              title: 'Channel',
              viewWindow: {
                min: [0, 30, 0],
                max: [3, 30, 0]
              }
            },
            vAxis: {
              title: 'Value'
            },
            axisTitlesPosition: 'none',
            vAxis: {
                textPosition: 'none',
            },
            hAxis: {
                textPosition: 'none',
            },
            legend: {
                position: 'none',
            },
          };

            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));

            chart.draw(data, options);
        }

        function point_it(event){
            var width = document.getElementById("image_result").width;
            var height = document.getElementById("image_result").height;
            var pos_x = event.offsetX;
            var pos_y = event.offsetY;

            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "http://127.0.0.1:5000/API?x="+pos_x+"&y="+pos_y+"&width="+width+"&height="+height, true);
            xhttp.setRequestHeader("Content-type", "application/json");

            xhttp.onreadystatechange = function () {
                if(xhttp.readyState === 4 && xhttp.status === 200) {
                    var answer = JSON.parse(xhttp.responseText);

                    var sr = parseFloat(answer.red.value).toFixed(2);
                    var sg = parseFloat(answer.blue.value).toFixed(2);
                    var sb = parseFloat(answer.green.value).toFixed(2);

                    $('#red').html(sr);
                    $('#blue').html(sg);
                    $('#green').html(sb);

                    r = (parseInt(sr) - answer.red.min) / (answer.red.max - answer.red.min);
                    g = (parseInt(sg) - answer.green.min) / (answer.green.max - answer.green.min);;
                    b = (parseInt(sb) - answer.blue.min) / (answer.blue.max - answer.blue.min);;

                    drawAxisTickColors(r, g, b);
                }
            };

            xhttp.send();
        }
