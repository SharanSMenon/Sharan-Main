var ctx = document.getElementById("myChart").getContext("2d");
var chart = document.getElementById("myChart");
var stackedLine = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["India", "USA", "China", "Brazil", "Japan", "Canada"],
        datasets: dtas1
    },
    options: {
        elements: {
            line: {
                tension: 0, // disables bezier curves
            }
        },
        responsive: false,
        title: {
            display: true,
            text: 'Taste of fruits'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Country'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Taste'
                },
                ticks: {
                    beginAtZero: true,
                    stepSize: 1,
                    max: maxi
                },
            }]
        }
    }
});