<!-- Set height and width with CSS -->
<?php
//here we get the input keyword from user
$str = " ";
$sample = "haha";
if (isset($_POST['keyword']))
{
	$query = $_POST['keyword'];
    //keyword count + accidents + weather info
    //REALLY SLOW!!! (need to cache data)
	$str = exec('python ./keyword-search_complete.py ' . $query );
    //causes
    //Fatal error: Maximum execution time of 30 seconds exceeded in C:\xampp2\htdocs\python\index.php on line 15
    //just keyword count
    //$str = exec('python ./keyword-search.py ' . $query );
    //echo $str;
}
	//decode the JSON $JSONresult
	$JSONresult = $str;
	$JSONresult = trim($JSONresult, '[');       //remove the extra brackets
	$JSONresult = trim($JSONresult, ']');
    $JSONresult = str_replace("}, {", "}==x=={" ,$JSONresult );
   $itemArray = explode("==x==", $JSONresult);
   //print_r( $itemArray);
	$allProducts = array();
	
  foreach ($itemArray as $value) {
      
     // echo $value;
      //\xa0 is actually non-breaking space in Latin1 (ISO 8859-1), also chr(160). You should replace it with a space.
       $itemExplode = str_replace('\xa0', ' ', $value );
        $itemExplode = str_replace("'", '"' ,$itemExplode);                  //replace single quotes with double quotes
        array_push($allProducts, $itemExplode );
        //echo $itemExplode;
        //var_dump(json_decode($itemExplode));
  }
  $allItems = array();

    //print_r($allProducts);
for ($x = 0; $x < count($allProducts); $x++) {

    $currentItem = json_decode($allProducts[$x], true);
    //print_r( $currentItem);
    array_push($allItems, $currentItem);
     //echo $currentItem["Area"]  ;
     //echo  $currentItem["Long"] ;
     //echo  $currentItem["Lat"]  ;
     // echo  $currentItem["Count"]  ;
} //	echo $result;
	  //print JSON to file
	 
	  $response['posts'] = $allItems;
      $response['keyword'] = $query;
	  $fp = fopen('results.json', 'w');
	  fwrite($fp, json_encode($response));
	  fclose($fp);
	  // now pass this data to another page <- scratch this
	  //or for now, just pass signal -> this is good enough
	  //redirect to mapping.php
	  // redirection should be enough signal, because we have the results in the .json file

	if (!empty($_POST['keyword']))
	{
		//redirect
		//header('Location: mapping.php');

        //set a variable, use as a check to show map or not
        $show = true;
	}
    else
    {
        $show = false;
    }
	  
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Salamanders 2.0</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="css/salamander.css">

</head>


<body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="60">

<!---- TOP NAVBAR ----->
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span> 
      </button>
      <a class="navbar-brand" href="#">Logo</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#about">ABOUT</a></li>
        <li><a href="#services">KEYWORDS</a></li>
        <li><a href="#portfolio">PORTFOLIO</a></li>
        <li><a href="#pricing">OPTIONS</a></li>
        <li><a href="#contact">YELP</a></li>
      </ul>
    </div>
  </div>
</nav>


<!-------- FORM ------------------------------>
<div class="jumbotron text-center">
  <h1>Salamanders</h1> 
  <p>Pick a keyword and see how frequently it is used in the map!!!</p> 
  button
   <!--form class="form-inline" action="index.php" method="POST"-->
  <form class="form-inline" action="index.php" method="POST">
    <input type="text" class="form-control" size="50" name="keyword" id="keyword" placeholder="good,bad">
    <button type="submit" class="btn btn-success" name="search" id="search">Search keyword</button>
  </form>

    <img src="yelp_powered_btn_dark@2x.png" alt="powered by Yelp" />
  
</div>

<!------------ PHP to JS ------------>
<!-- snip -->
<div id="dom-target" style="display: none;">
    <?php

		if (isset($allProducts))
		{
			  $submitted = "TRUE";
			  //echo htmlspecialchars($submitted);
            /* You have to escape because the result
			 will not be valid HTML otherwise. */
		}
		else
		{
		  echo "somethings wrong";
		}
	?>
</div>
<script>
  
  // Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.

} else {
  alert('The File APIs are not fully supported in this browser.');
}


  /*
    var div = document.getElementById("dom-target");
   // var signalFromPHP = div.textContent;
	//if (signalFromPHP == "TRUE") {

  	  //put into map, read values from file
	  //first plan is create markers for each loaded location from file
	  
	  //1. open text file - geo.json
	  //2. read location per location, get lat ang long, plus the count
	  //3. show in map - by creating markers or loading

	var mapMarkers = [];
	//var myLatLng = {lat: 45.5370, lng: -73.59605};
    }
    */
</script>


<div id="results"></div>

<div id="googleMap" style="height:400px;width:100%;"></div>
<!-- load data here -->
<div id="data"></div>
<!-- scratch -->
<div id="scratch"></div>


<!-- ------- do some work ------ -->
<div id="about" class="container-fluid">
  <div class="row">
    <div class="col-sm-8">
      <h2>Testing Python</h2>
      <h4>--------------</h4> 
      <p> 
          <?php
					//use PHP to run Python script
		  
               // $str = exec('python ./yelp-python/yelp.py');
                //echo $str;
          ?>
      </p>
      <!--button class="btn btn-default btn-lg">Get in Touch</button-->
    </div>
    <!--div class="col-sm-4">
      <span class="glyphicon glyphicon-signal logo slideanim"></span>
    </div-->
  </div>
</div>
<!------------------------->



<!--########### sample data visualization #############-->
<div>
<script src="//d3js.org/d3.v3.min.js"></script>
<script>

// Generate a Bates distribution of 10 random variables.
var values = d3.range(1000).map(d3.random.bates(10));

// A formatter for counts.
var formatCount = d3.format(",.0f");

var margin = {top: 10, right: 30, bottom: 30, left: 30},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .domain([0, 1])
    .range([0, width]);

// Generate a histogram using twenty uniformly-spaced bins.
var data = d3.layout.histogram()
    .bins(x.ticks(20))
    (values);

var y = d3.scale.linear()
    .domain([0, d3.max(data, function(d) { return d.y; })])
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var bar = svg.selectAll(".bar")
    .data(data)
  .enter().append("g")
    .attr("class", "bar")
    .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

bar.append("rect")
    .attr("x", 1)
    .attr("width", x(data[0].dx) - 1)
    .attr("height", function(d) { return height - y(d.y); });

bar.append("text")
    .attr("dy", ".75em")
    .attr("y", 6)
    .attr("x", x(data[0].dx) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return formatCount(d.y); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

</script>

</div>

<!--####################################-->



<!-------- EXTRAS ---------->

<div id="about" class="container-fluid">
  <div class="row">
    <div class="col-sm-8">
      <h2>About Company Page</h2>
      <h4>Lorem ipsum..</h4> 
      <p>Lorem ipsum..</p>
      <button class="btn btn-default btn-lg">Get in Touch</button>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-signal logo slideanim"></span>
    </div>
  </div>
</div>

<div class="container-fluid bg-grey">
  <div class="row">
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-globe logo slideanim"></span> 
    </div>
    <div class="col-sm-8">
      <h2>Our Values</h2>
      <h4><strong>MISSION:</strong> Our mission lorem ipsum..</h4> 
      <p><strong>VISION:</strong> Our vision Lorem ipsum..</p>
    </div>
  </div>
</div>

<div id="services" class="container-fluid text-center">
  <h2>SERVICES</h2>
  <h4>What we offer</h4>
  <br>
  <div class="row slideanim">
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-off"></span>
      <h4>POWER</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-heart"></span>
      <h4>LOVE</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-lock"></span>
      <h4>JOB DONE</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
    </div>
    <br><br>
  <div class="row slideanim">
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-leaf"></span>
      <h4>GREEN</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-certificate"></span>
      <h4>CERTIFIED</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
    <div class="col-sm-4">
      <span class="glyphicon glyphicon-wrench"></span>
      <h4>HARD WORK</h4>
      <p>Lorem ipsum dolor sit amet..</p>
    </div>
  </div>
</div>

<div id="portfolio" class="container-fluid text-center bg-grey">
  <h2>Portfolio</h2>
  <h4>What we have created</h4>
  <div class="row text-center slideanim">
    <div class="col-sm-4">
      <div class="thumbnail">
        <!--img src="stuff1.jpg" alt="Paris"-->
        <p><strong>Stuff1</strong></p>
        <p>Stuff the stuff</p>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="thumbnail">
        <!--img src="stuff2.jpg" alt="New York"-->
        <p><strong>Stuff2</strong></p>
        <p>Stuff the stuff</p>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="thumbnail">
        <!--img src="sanfran.jpg" alt="San Francisco"-->
        <p><strong>Stuff3</strong></p>
        <p>Stuff the stuff</p>
      </div>
    </div>
  </div>



<h2>What our customers say</h2>
<div id="myCarousel" class="carousel slide text-center" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
    <li data-target="#myCarousel" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
    <h4>"This company is the best. I am so happy with the result!"<br><span style="font-style:normal;">Michael Roe, Vice President, Comment Box</span></h4>
    </div>
    <div class="item">
      <h4>"One word... WOW!!"<br><span style="font-style:normal;">John Doe, Salesman, Rep Inc</span></h4>
    </div>
    <div class="item">
      <h4>"Could I... BE any more happy with this company?"<br><span style="font-style:normal;">Chandler Bing, Actor, FriendsAlot</span></h4>
    </div>
  </div>

  <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>



<div class="container-fluid bg-grey">
  <h2 id="contact" class="text-center">CONTACT</h2>
  <div class="row">
    <div class="col-sm-5">
      <p>Contact us and we'll get back to you within 24 hours.</p>
      <p><span class="glyphicon glyphicon-map-marker"></span> Montreal, QC</p>
      <p><span class="glyphicon glyphicon-phone"></span> +1234 5678</p>
      <p><span class="glyphicon glyphicon-envelope"></span>salamanders@yackathon2016</p> 
    </div>
    <div class="col-sm-7 slideanim">
      <div class="row">
        <div class="col-sm-6 form-group">
          <input class="form-control" id="name" name="name" placeholder="Name" type="text" required>
        </div>
        <div class="col-sm-6 form-group">
          <input class="form-control" id="email" name="email" placeholder="Email" type="email" required>
        </div>
      </div>
      <textarea class="form-control" id="comments" name="comments" placeholder="Comment" rows="5"></textarea><br>
      <div class="row">
        <div class="col-sm-12 form-group">
          <button class="btn btn-default pull-right" type="submit">Send</button>
        </div>
      </div> 
    </div>
  </div>
</div>



</div>


<?php
if ($show) {
    ?>
    <div>

        <!-- directly embedded getResults() AJAX function instead -->
        <script>

            function getResults() {

                //document.write('hello');

                var xhttp = new XMLHttpRequest();

                xhttp.onreadystatechange = function() {
                    if (xhttp.readyState == 4 && xhttp.status == 200) {

                        //## xhttp.responseText holds the server responseText ##
                        //document.getElementById("data").innerHTML = xhttp.responseText;

                        jsonData = xhttp.responseText;

                        document.getElementById("data").innerHTML = jsonData;

                        //SHOULD SEE EVERYTING HERE - TESTING
                        //----> console.log(jsonData);

                        //JSON data includes a []

                        /*
                         1. decode json - can probably use a function
                         2. put it in array
                         3. put Google Maps script here, easier to load vars from json to google markers
                         -coz were in Javascript!!!!
                         */

                        //console.log(typeof(jsonData));
                        //obj = JSON.parse(jsonData);

                        //convert to a string to be able to store in HTML localStorage

                        console.log(jsonData);

                        obj = JSON.stringify(jsonData);
                        localStorage.setItem("searchResults", obj);

                        //console.log(obj);
                        //console.log(obj.length);
                        //console.log(parseJSON($jsonData));

                        /*
                         htmlString = "<table border='1'>";

                         for (x=0; x < objCount; x++)
                         {
                         htmlString += "<tr><td>" + obj[x].Area + "</td><td>" + obj[x].Count + "</td><td>" + obj[x].Lat + "</td><td>" + obj[x].Long + "</td><td>" + obj[x].Name + "</td></tr>"	;
                         }
                         htmlString += "</table>";
                         //document.getElementById("scratch").innerHTML = "=====================================" + htmlString;

                         */

                        //console.log(obj.toString());
                    }
                };

                xhttp.open("GET", "results.json", true);
                xhttp.send();

            }		//end getResults() function

            // could also call getResults() from here
            // getResults()
            //document.write(getResults());

        </script>


        <div id="maps">
            <!-- ############## MAPS ########################## -->

            <!-- Add Google Maps -->
            <script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyBztqRH0IXenFXQ8S-jWdA1dabJ6Py_H1c"></script>
            <script>

                console.log("here");

                // call function
                getResults();

                // get HTML5 storage item stored
                var dataStored = JSON.parse(localStorage.getItem("searchResults"));

                //console.log(dataStored);
                //window.alert(dataStored);
                //console.log(dataStored.length);
                //console.log(typeof(dataStored));

                // parse to an object array
                datas = JSON.parse(dataStored);


                //console.log(datas);

                //console.log(datas.posts[0]);
                //console.log(datas.posts[1]);
                //console.log(datas.posts[1] == null);
                //console.log(datas.keyword);

                //console.log("count" + datas.posts.length);

                //console.log(datas.posts[0].Area);

                //console.log("length:" + datas.posts.length);

                //print HTML table of obtained location tuples
                htmlString = "<table border='1'>";
                //for (x=0; x < datas.length; x++)
                for (x=0; x < datas.posts.length; x++)
                {
                    //htmlString += "<tr><td>" + datas[x].Area + "</td><td>" + datas[x].Count + "</td><td>" + datas[x].Lat + "</td><td>" + datas[x].Long + "</td><td>" + datas[x].Name + "</td></tr>"	;

                    //console.log( datas.posts[x].Area);
                    //console.log( datas.posts[x].Count);
                    //console.log( datas.posts[x].Lat);
                    //console.log( datas.posts[x].Long);
                    //console.log( datas.posts[x].Name);

                    //console.log(datas.posts[x].Area == null);

                    if (datas.posts[x] == null)
                    {
                        //console.log("null object");
                    }
                    else
                    {
                        htmlString += "<tr><td>" + datas.posts[x].Area + "</td><td>" + datas.posts[x].Count + "</td><td>" + datas.posts[x].Lat + "</td><td>" + datas.posts[x].Long + "</td><td>" + datas.posts[x].Name + "</td></tr>"	;
                    }

                }
                htmlString += "</table>";

                //console.log(JSON.parse(dataStored));
                document.getElementById("scratch").innerHTML = "=====================================" + htmlString;

                //console.log(htmlString);

                //use center location as the center
                var myCenter = new google.maps.LatLng(45.52605, -73.59505);

                //https://developers.google.com/maps/documentation/javascript/examples/marker-labels
                //initialize google maps
                function initialize() {

                    // set up map, scrollable and draggable
                    var mapProp = {
                        center: myCenter,
                        zoom:12,
                        scrollwheel:true,
                        draggable:true,
                        mapTypeId:google.maps.MapTypeId.ROADMAP
                    };

                    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);


                    //###############################################
                    //setup one marker at center
                    var marker = new google.maps.Marker({
                        position:myCenter
                    });

                    marker.setMap(map);
                    //#############################################


                    var markers = [];

                    // loop through locations, get their Lat ang Long then make markers for each
                    for (x=0; x < datas.posts.length; x++)
                    {

                        if (datas.posts[x] == null)
                        {
                            //console.log("FUCK NULL" + x);
                        }
                        else
                        {
                            //console.log(datas.posts[x]);

                            //customize label based on number of keywords
                            //unfortunately, only 1 char is allowed to display in marker label
                            if (datas.posts[x].Count == 0)
                                label = '0' ;
                            else
                               label = '☺';


                            // new marker
                            var myLatLng2 = {lat: datas.posts[x].Lat, lng: datas.posts[x].Long};
                            var marker2 = new google.maps.Marker({
                                position: myLatLng2,
                                map: map,
                                title: datas.posts[x].Name,
                                label: label,
                                html: '<div>Keyword count:' +  datas.posts[x].Count  + '<br />Area: ' +  datas.posts[x].Area   + '<br />' +  datas.posts[x].Name + '<br />Accidents:' +  datas.posts[x].Accidents + '<br />Temperature:' +  datas.posts[x].Weather    + '</div>'
                            });
							

								//add to markers array
								markers.push(marker2);

							
							
                            //string for info window
                            var infowindow = new google.maps.InfoWindow({
                                content: "hehe"
                            });

                            console.log(markers[x]);

                            /*
                             //BUGGY: only applies html to last one
                             markers[x].addListener('click', function() {
                             infowindow.setContent(markers[x].html);
                             infowindow.open(map, markers[x]);
                             });
                             */

                            //this one works - puts a listener to this current marker
                            google.maps.event.addListener(marker2,'click', function() {

                                infowindow.setContent(this.html);
                                infowindow.open(map, this);
                            });
                            //same as setting the map attrib in marker def
                            //marker2.setMap(map);
                        }
                    } // #END FOR
                }	//end of GoogleMaps init()

                google.maps.event.addDomListener(window, 'load', initialize);

            </script>

            <!------------------------------------------------->
            <script>
                $(document).ready(function(){
                    // Add smooth scrolling to all links in navbar + footer link
                    $(".navbar a, footer a[href='#myPage']").on('click', function(event) {

                        // Prevent default anchor click behavior
                        event.preventDefault();

                        // Store hash
                        var hash = this.hash;

                        // Using jQuery's animate() method to add smooth page scroll
                        // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
                        $('html, body').animate({
                            scrollTop: $(hash).offset().top
                        }, 900, function(){

                            // Add hash (#) to URL when done scrolling (default click behavior)
                            window.location.hash = hash;
                        });
                    });
                })

                $(window).scroll(function() {
                    $(".slideanim").each(function(){
                        var pos = $(this).offset().top;

                        var winTop = $(window).scrollTop();
                        if (pos < winTop + 600) {
                            $(this).addClass("slide");
                        }
                    });
                });
            </script>
        </div>



    </div>
    <?php
}
else {
    ?>
    <div id="maps">

        <!-- ############## MAPS ########################## -->

        <!-- Add Google Maps -->
        <script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyBztqRH0IXenFXQ8S-jWdA1dabJ6Py_H1c"></script>
        <script>


            var myCenter = new google.maps.LatLng(45.52605, -73.59505);


            function initialize() {
                var mapProp = {
                    center: myCenter,
                    zoom: 12,
                    scrollwheel: false,
                    draggable: false,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };

                var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

                var marker = new google.maps.Marker({
                    position: myCenter,
                });

                //marker.setMap(map);


                // new marker
                var myLatLng = {lat: 45.5370, lng: -73.59605};
                var marker1 = new google.maps.Marker({
                        position: myLatLng,
                        //map: map,
                        title: 'Hello World!'
                    }
                );

                //marker1.setMap(map);


                /*var infowindow = new google.maps.InfoWindow({
                 content: 'Latitude: ' + myLatLng.lat() + '<br>Longitude: ' + myLatLng.lng()
                 });
                 infowindow.open(map,marker1);*/


            }

            google.maps.event.addDomListener(window, 'load', initialize);

        </script>


        <!------------------------------------------------->


        <script>
            $(document).ready(function () {
                // Add smooth scrolling to all links in navbar + footer link
                $(".navbar a, footer a[href='#myPage']").on('click', function (event) {

                    // Prevent default anchor click behavior
                    event.preventDefault();

                    // Store hash
                    var hash = this.hash;

                    // Using jQuery's animate() method to add smooth page scroll
                    // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
                    $('html, body').animate({
                        scrollTop: $(hash).offset().top
                    }, 900, function () {

                        // Add hash (#) to URL when done scrolling (default click behavior)
                        window.location.hash = hash;
                    });
                });
            })

            $(window).scroll(function () {
                $(".slideanim").each(function () {
                    var pos = $(this).offset().top;

                    var winTop = $(window).scrollTop();
                    if (pos < winTop + 600) {
                        $(this).addClass("slide");
                    }
                });
            });
        </script>

    </div>
    <?php
}

?>


</body>
</html>