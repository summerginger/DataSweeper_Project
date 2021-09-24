function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("samples.json").then((data) => {
      var sampleNames = data.names;
  
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      var firstSample = sampleNames[0];
      buildCharts(firstSample);
      buildMetadata(firstSample);
    });
  }
  
  // Initialize the dashboard
  init();
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildMetadata(newSample);
    buildCharts(newSample)
    
  };
  
  // Demographics Panel 
  function buildMetadata(sample) {
    d3.json("samples.json").then((data) => {
      var metadata = data.metadata;
      // Filter the data for the object with the desired sample number
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var result = resultArray[0];
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
  
  // 1. Create the buildCharts function.
  function buildCharts(sample) {
    // 2. Use d3.json to load and retrieve the samples.json file 
    d3.json("samples.json").then((data) => {
      // 3. Create a variable that holds the samples array. 
      var barData = data.samples;
      // 4. Create a variable that filters the samples for the object with the desired sample number.
      var sampleArray = barData.filter (sampleObj => sampleObj.id == sample);

      //  5. Create a variable that holds the first sample in the array.
      var sampleResult = sampleArray[0];
      // 6. Create variables that hold the otu_ids, otu_labels, and sample_values.
      var Ydata = sampleResult.otu_ids;
      var hText = sampleResult.otu_labels;
      var Xdata = sampleResult.sample_values;
      // 7. Create the yticks for the bar chart.
      // Hint: Get the the top 10 otu_ids and map them in descending order  
      //  so the otu_ids with the most bacteria are last. 
  
      var yticks = Ydata.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse();
  
      // 8. Create the trace for the bar chart. 
      var barTrace = [{
        x: Xdata, 
        y: yticks, 
        text: hText,
        type: "bar", orientation: "h"
      }];
        
      // 9. Create the layout for the bar chart. 
      var barLayout = {
        title: "<b> Top10 Bacterial Cultures Found </b>",
        // xaxis: {title: "Sample Values"},  
        yaxis: {autorange: "reversed"}
      };
       
      // 10. Use Plotly to plot the data with the layout. 
      Plotly.newPlot("bar",barTrace,barLayout);
 
    //    1. Create the trace for the bubble chart.
    var bubbleXdata = sampleResult.otu_ids;
    var bubbleYdata = sampleResult.sample_values;
    var bubblehText = sampleResult.otu_labels;

    var bubbleTrace = [{
      x:bubbleXdata, 
      y:bubbleYdata, 
      text:bubblehText,
      mode:"markers", 
      marker:{
        size:bubbleYdata,
        color:bubbleXdata,
        colorscale:"Earth",
      }
    }];

    // 2. Create the layout for the bubble chart.
    var bubbleLayout = {
      title:"Bacteria Cultures Per Sample",
      xaxis: {
        title:"OTUs ID"
      }
    };

    // 3. Use Plotly to plot the data with the layout.
    Plotly.newPlot("bubble",bubbleTrace, bubbleLayout); 

     // 4. Create the trace for the gauge chart.
     var samples = data.metadata;
     var sampleArray = samples.filter(sampleObj => sampleObj.id == sample);
     var result = sampleArray[0];
    var gaugeData = parseInt(result.wfreq);

    var gaugeTrace = {
        type: "indicator",
        mode:"gauge+number",
        value: gaugeData,
        gauge:{
            axis: {range: [null,10],tickwidth:1},
            bar: { color : "#cfd16f"},
            steps: [
              {range: [0,1], color: "#B0C4DE"},
              {range: [1,2], color: "#B0E0E6"},
              {range: [2,3], color: "#87CEEB"},
              {range: [3,4], color: "#87CEFA"},
              {range: [4,5], color: "#00BFFF"},
              {range: [5,6], color: "#1E90FF"},
              {range: [6,7], color: "#0000FF"},
              {range: [7,8], color: "#0000CD"},
              {range: [8,9], color: "#191970"},
              {range: [9,10],color: "#070733"},
            ]        
        }
    };
    // 5. Create the layout for the gauge chart.
    var gaugeLayout = { 
        title: "<b>Belly Button Washing Frequency</b><br>Scrubs per Week",
        // paper_bgcolor: "pink",
        margin: { t: 40, r: 25, l: 25, b: 0 },
        width: 450,
        height: 400,
        font: { color: "dark", family: "Arial" }
};
   

    // 6. Use Plotly to plot the gauge data and layout.
    Plotly.newPlot("gauge", [gaugeTrace],gaugeLayout);

  });
}


