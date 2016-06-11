<?php
// testing code
print_r($_POST);

/*
 * Modifications
 *
 * 6/5/2016
 *
 * had problems using jQuery JSON parsing
 * used javascript JSON parse
 * stringify to convert to a string - store in local storage
 * get from local storage - JSON parse
 *
 * finally made markers appear in Google Maps
 *
 *
 *
 *
 */



?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Map result</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">


    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>


    <link rel="stylesheet" href="css/salamander.css">


</head>

<!--  ONLOAD, call this function -->
<!-- body onload = "getResults()" -->
<body>

<!---- AJAX ------------->
<!--script type="text/javascript" src= "ajax_read_jsonresult.js" async>
</script-->
<!------------------------->

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

                /*
                 1. decode json - can probably use a function
                 2. put it in array
                 3. put Google Maps script here, easier to load vars from json to google markers
                 -coz were in Javascript!!!!
                 */

                //console.log(typeof(jsonData));
                //obj = JSON.parse(jsonData);

                //convert to a string to be able to store in HTML localStorage
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

                console.log(obj.toString());
            }
        };

        xhttp.open("GET", "results.json", true);
        xhttp.send();

    }		//end getResults() function

    // could also call getResults() from here
    // getResults()
    //document.write(getResults());

</script>

<div id="results"></div>
<div id="googleMap" style="height:400px;width:100%;"></div>

<!-- load data here -->
<div id="data"></div>
<!-- scratch -->
<div id="scratch"></div>



<div id="maps">
    <!-- ############## MAPS ########################## -->

    <!-- Add Google Maps -->
    <script src="http://maps.googleapis.com/maps/api/js"></script>
    <script>

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

        //print HTML table of obtained location tuples
        htmlString = "<table border='1'>";
        for (x=0; x < datas.length; x++)
        {
            htmlString += "<tr><td>" + datas[x].Area + "</td><td>" + datas[x].Count + "</td><td>" + datas[x].Lat + "</td><td>" + datas[x].Long + "</td><td>" + datas[x].Name + "</td></tr>"	;
        }
        htmlString += "</table>";

        //console.log(JSON.parse(dataStored));
        document.getElementById("scratch").innerHTML = "=====================================" + htmlString;


        var myCenter = new google.maps.LatLng(45.52605, -73.59505);

        //initialize google maps
        function initialize() {
            var mapProp = {
                center:myCenter,
                zoom:12,
                scrollwheel:false,
                draggable:false,
                mapTypeId:google.maps.MapTypeId.ROADMAP
            };

            var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

            var marker = new google.maps.Marker({
                position:myCenter,
            });

            marker.setMap(map);

            // loop through locations, get their Lat ang Long then make markers for each
            for (x=0; x < datas.length; x++)
            {
                console.log(datas[x].Lat);
                //window.alert(loc1.Lat);

                // new marker
                var myLatLng2 = {lat: datas[x].Lat, lng:datas[x].Long};
                var marker2 = new google.maps.Marker({
                        position: myLatLng2,
                        //map: map,
                        title: 'Hello World!'
                    }
                );
                marker2.setMap(map);
            }


            /*
             // new marker
             var myLatLng = {lat: 45.5370, lng: -73.59605};
             var marker1 = new google.maps.Marker({
             position: myLatLng,
             //map: map,
             title: 'Hello World!'
             }
             );
             marker1.setMap(map);
             */

            //var infowindow = new google.maps.InfoWindow({
            //content: 'Latitude: ' + myLatLng.lat() + '<br>Longitude: ' + myLatLng.lng()
            //});
            //infowindow.open(map,marker1);

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



<!-- jquery script, upod loading of data to "scratch" div, execute this -->
<script>

    /*
     $( "#scratch" ).click(function() {
     var htmlString = $( this ).html();
     $( this ).text( htmlString );
     });
     */

    $( "#scratch" ).click(function() {
        var htmlString = $( this ).html();
        $( this ).text( htmlString );
    });

</script>

</body>


</html>
