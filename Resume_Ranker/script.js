document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector("table");
    if (!table) return;

    const labels = [];
    const data = [];

    for (let i = 1; i < table.rows.length; i++) {
        labels.push(table.rows[i].cells[0].innerText);
        data.push(parseInt(table.rows[i].cells[1].innerText));
    }

    const ctx = document.getElementById('barChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Resume Score',
                data: data,
                backgroundColor: 'rgba(0, 162, 255, 0.7)'
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true, max: 100 }
            },
            responsive: true,
        }
    });
});
