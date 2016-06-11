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
			
			console.log(typeof(jsonData));
			
			obj = JSON.parse(jsonData);
			
			console.log(obj);
			console.log(obj.length);
			
			objCount = obj.length;
			
			//console.log(parseJSON($jsonData));
			
			htmlString = "<table border='1'>";
			
			for (x=0; x < objCount; x++)
			{
				htmlString += "  \
					<tr>							\
						<td>" + obj[x].Area + "</td>		\
						<td>" + obj[x].Count + "</td>		\
						<td>" + obj[x].Lat + "</td>			\
						<td>" + obj[x].Long + "</td>		\
						<td>" + obj[x].Name + "</td>		\
					</tr>"	;
			}
			
			htmlString += "</table>";
			
			globalString = htmlString;
			
			document.getElementById("scratch").innerHTML = "=====================================" + htmlString;
				
			
			//jQuery.parseJSON($jsonData)
			
			
			//return htmlString;
			window.glob = htmlString;
			
			return window.glob;
			

			
			
		}
	};
	
	xhttp.open("GET", "results.json", true);
	xhttp.send();
	
}