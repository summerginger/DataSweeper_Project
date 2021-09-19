function optionChanged(){
  // Fetch new data each time a new sample is selected
  var sample = document.getElementById("myInput").value;
  buildMetadata(sample);
 // buildCharts(newSample);
  
}

// Demographics Panel 
function buildMetadata(sample) {
  d3.json("csvjson.json").then((data) => {
    console.log('step1');
    // Filter the data for the object with the desired sample number
    var resultArray = data.filter(sampleObj => sampleObj.ID == sample);
    console.log(resultArray);
    var result = resultArray[0];
    console.log('step3');
    console.log(result);
    // Use d3 to select the panel with id of `#sample-metadata`
    var PANEL = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    PANEL.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });

  });
}
