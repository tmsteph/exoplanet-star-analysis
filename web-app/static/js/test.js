Plotly.d3.csv("/../../planets.csv").then((data) => {
	// Create Traces
	var trace1 = {
	x: data.sy_pnum,
	y: data.sy_dist		
	};

	//create the data array for plot
	var data = [trace1];

	//define layout

	var layout = {
		title: "title"
	}
})



