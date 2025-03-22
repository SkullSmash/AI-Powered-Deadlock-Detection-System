document.addEventListener("DOMContentLoaded", function () {
    fetchGraphData();
});

// Function to fetch graph data from the server
function fetchGraphData() {
    fetch("/detect_deadlock")
        .then(response => response.json())
        .then(data => {
            updateGraph(data.graph, data.deadlock, data.cycle);
            updateDeadlockStatus(data.deadlock, data.cycle);
        })
        .catch(error => console.error("Error fetching graph data:", error));
}

// Function to update the deadlock status message
function updateDeadlockStatus(deadlock, cycle) {
    const statusDiv = document.getElementById("deadlock-status");
    if (deadlock) {
        statusDiv.innerHTML = `<span style="color: red; font-weight: bold;">Deadlock Detected! 🔴</span> <br> Cycle: ${cycle.map(edge => `${edge[0]} → ${edge[1]}`).join(" → ")}`;
    } else {
        statusDiv.innerHTML = `<span style="color: green; font-weight: bold;">No Deadlock Detected ✅</span>`;
    }
}

// Function to render the process-resource graph using D3.js
function updateGraph(graphData, deadlock, cycle) {
    // Remove existing graph
    d3.select("#graph-container").selectAll("*").remove();

    const width = 600, height = 400;

    const svg = d3.select("#graph-container")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    const simulation = d3.forceSimulation(graphData.nodes)
        .force("link", d3.forceLink(graphData.links).id(d => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2));

    // Draw links
    const link = svg.selectAll(".link")
        .data(graphData.links)
        .enter().append("line")
        .attr("class", "link")
        .style("stroke", d => (deadlock && cycle.some(edge => edge[0] === d.source.id && edge[1] === d.target.id)) ? "red" : "#888")
        .style("stroke-width", 2);

    // Draw nodes
    const node = svg.selectAll(".node")
        .data(graphData.nodes)
        .enter().append("g")
        .attr("class", "node")
        .call(d3.drag()
            .on("start", dragStart)
            .on("drag", dragged)
            .on("end", dragEnd));

    node.append("circle")
        .attr("r", 20)
        .attr("fill", d => d.id.startsWith("P") ? "#007bff" : "#ffa500")
        .attr("stroke", "#333")
        .attr("stroke-width", 2);

    node.append("text")
        .attr("dy", 5)
        .attr("text-anchor", "middle")
        .style("fill", "#fff")
        .text(d => d.id);

    simulation.nodes(graphData.nodes).on("tick", ticked);
    simulation.force("link").links(graphData.links);

    function ticked() {
        link.attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node.attr("transform", d => `translate(${d.x},${d.y})`);
    }

    function dragStart(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragEnd(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
}
