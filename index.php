<!-- Set height and width with CSS -->
<?php
//here we get the input keyword from user
$str = " ";
$sample = "haha";
if (isset($_POST['keyword']))
{
	$query = $_POST['keyword'];
	$response['keyword'] = $query;
    //keyword count + accidents + weather info
    //REALLY SLOW!!! (need to cache data)
	$str = exec('python ./keyword-search_complete.py ' . $query );
    //causes
    //Fatal error: Maximum execution time of 30 seconds exceeded ....
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
    array_push($allItems, $currentItem);
} 

$response['posts'] = $allItems;

$fp = fopen('results.json', 'w');
fwrite($fp, json_encode($response));
fclose($fp);
// now pass this data to another page <- scratch this
//or for now, just pass signal -> this is good enough
//redirect to mapping.php
// redirection should be enough signal, because we have the results in the .json file

if (!empty($_POST['keyword']))
	$show = true;
else
	$show = false;
	  
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
	<!--script src="https://rawgit.com/nmccready/google-maps-utility-library-v3-markerwithlabel/master/dist/markerwithlabel.js"></script-->
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
      <a class="navbar-brand" href="#">Salamanders</a>
    </div>
  </div>
</nav>


<!-------- FORM ------------------------------>
<div class="jumbotron text-center">
  <h1>Salamanders</h1> 
  <p>Pick a keyword and see how frequently it is used in the map!!!</p> 
   <!--form class="form-inline" action="index.php" method="POST"-->
  <form class="form-inline" action="index.php" method="POST">
    <input type="text" class="form-control" size="50" name="keyword" id="keyword" placeholder="good,bad"
		value="<?php if (isset($_POST['keyword']))
		{echo $_POST['keyword']; } ?>"
	/>
    <button type="submit" class="btn btn-success" name="search" id="search">Search keyword</button>
  </form>

    <img src="yelp_powered_btn_dark@2x.png" alt="powered by Yelp" />
  
</div>

<!------------ PHP to JS ------------>
<!-- snip -->
<div id="dom-target" style="display: none;">
    <?php
		if (isset($allProducts))
			  $submitted = "TRUE";
		else
		  echo "somethings wrong";
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
<div id="data"></div>
<div id="scratch"></div>

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

                        //console.log(jsonData);

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
            <!-- ############## GOOGLE MAPS ########################## -->
            <script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyBztqRH0IXenFXQ8S-jWdA1dabJ6Py_H1c"></script>
            <script>
                // call function
                getResults();
                // get HTML5 storage item stored
                var dataStored = JSON.parse(localStorage.getItem("searchResults"));
                // parse to an object array
                datas = JSON.parse(dataStored);
                //print HTML table of obtained location tuples
                htmlString = "<table border='1'>";
               
                for (x=0; x < datas.posts.length; x++)
                {
                    if (datas.posts[x] != null)
                    {
                        htmlString += "<tr><td>" + datas.posts[x].Area + "</td><td>" + datas.posts[x].Count + "</td><td>" + datas.posts[x].Lat + "</td><td>" + datas.posts[x].Long + "</td><td>" + datas.posts[x].Name + "</td></tr>"	;
                    }
                }
                htmlString += "</table>";

                //document.getElementById("scratch").innerHTML = "=====================================" + htmlString;

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
					
					// init. marker array
                    var markers = [];

                    // loop through locations, get their Lat ang Long then make markers for each
                    for (x=0; x < datas.posts.length; x++)
                    {
                        if (datas.posts[x] != null)
                        {
                            //customize label based on number of keywords
                            //unfortunately, only 1 char is allowed to display in marker label
                            if (datas.posts[x].Count == 0)
                            {    
								label = '0' ;
								continue;
							}
                            else
							{
								//label = '☺';
								label = '' + datas.posts[x].Count;							
							}
                               

                            // new marker
                            var myLatLng2 = {lat: datas.posts[x].Lat, lng: datas.posts[x].Long};
							
							/*
                            var marker2 = new google.maps.MarkerWithLabel({
                                position: myLatLng2,
                                map: map,
                                //title: datas.posts[x].Name,
                                labelContent: label,
								labelAnchor: new google.maps.Point(15, 65),
								labelClass: "labels",
								icon: pinSymbol('red'),
                                html: '<div>Keyword count:' +  datas.posts[x].Count  + '<br />Area: ' +  datas.posts[x].Area   + '<br />' +  datas.posts[x].Name + '<br />Accidents:' +  datas.posts[x].Accidents + '<br />Temperature:' +  datas.posts[x].Weather    + '</div>'
                            });*/
                            var marker2 = new google.maps.Marker({
                                position: myLatLng2,
                                map: map,
                                title: datas.posts[x].Name,
                                label: label,
                                html: '<div>Keyword count:' +  datas.posts[x].Count  + '<br />Area: ' +  datas.posts[x].Area   + '<br />' +  datas.posts[x].Name + '<br />Accidents:' +  datas.posts[x].Accidents + '<br />Temperature:' +  datas.posts[x].Weather    + '</div>'
                            });
							
							
							markers.push(marker2);		
							
                            //string for info window
                            var infowindow = new google.maps.InfoWindow({
                                content: "hehe"
                            });

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

				
				
				function pinSymbol(color) {
					return {
						path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
						fillColor: color,
						fillOpacity: 1,
						strokeColor: '#000',
						strokeWeight: 2,
						scale: 2
					};
				}
				
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

                // new marker
                var myLatLng = {lat: 45.5370, lng: -73.59605};
                var marker1 = new google.maps.Marker({
                        position: myLatLng,
                        //map: map,
                        title: 'Hello World!'
                    }
                );
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