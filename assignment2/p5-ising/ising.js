let step = function (state, temp) {

    let N1 = state.shape[0];
    let N2 = state.shape[1];

    for (let i = 1; i < N1 - 1; i++) {
        for (let j = 1; j < N2 - 1; j += 2) {
            _update(state, i, j, temp)
        }
    }

    for (let i = 1; i < N1; i++) {
        for (let j = 2; j < N2; j += 2) {
            _update(state, i, j, temp)
        }
    }

    return state;
}

let _update = function (x, i, j, temp) {

    n = x.shape[0];
    m = x.shape[1];
    dE = 2 * x.get(i, j) * (
        x.get((i - 1) % n, (j - 1) % m)
        + x.get((i - 1) % n, j)
        + x.get((i - 1) % n, (j + 1) % m)
        + x.get(i, (j - 1) % m)
        + x.get(i, (j + 1) % m)
        + x.get((i + 1) % n, (j - 1) % m)
        + x.get((i + 1) % n, j)
        + x.get((i + 1) % n, (j + 1) % m)
    )
    if (dE <= 0 || nj.exp(-dE / temp) > nj.random()) { // set T as param
        let value = x.get(i, j);
        x.set(i, j, value * -1);
    }
}

let calc_energy = function (state, J = 1., B = 0.) {

    let spin_neighbor_sum = 0.;
    let spin_sum = 0.;
    for (let row = 1; row < state.shape[0] - 1; row++) {
        for (let col = 1; col < state.shape[1] - 1; col++) {
            spin_neighbor_sum += state.get(row, col) * state.get(row + 1, col);
            spin_neighbor_sum += state.get(row, col) * state.get(row - 1, col);
            spin_neighbor_sum += state.get(row, col) * state.get(row, col + 1);
            spin_neighbor_sum += state.get(row, col) * state.get(row, col - 1);
            spin_sum += state.get(row, col);
        }
    }

    return -J * spin_neighbor_sum - B * spin_sum;

}

let calc_magnetization = function (state, J = 1., B = 0.) {

    let spin_sum = 0.;
    for (let row = 1; row < state.shape[0] - 1; row++) {
        for (let col = 1; col < state.shape[1] - 1; col++) {
            spin_sum += state.get(row, col);
        }
    }

    return spin_sum;

}

let arrow_size = 5;

let Arrow = function (x, y, length) {
    this.x = x;
    this.y = y;
    this.length = length;
    this.update = function (value) {
        push();
        beginShape();
        rotate(0);
        if (value >= 0.5) {
            fill(200, 0, 0);
            translate(this.x, this.y + arrow_size * this.length);
            rotate(-Math.PI / 2);
        } else {
            fill(0, 0, 160);
            translate(this.x, this.y);
            rotate(Math.PI / 2);
        }
        noStroke();
        vertex(0, -this.length);
        vertex(5 * this.length, -this.length);
        vertex(5 * this.length, -3 * this.length);
        vertex(arrow_size * this.length, 0);
        vertex(5 * this.length, 3 * this.length);
        vertex(5 * this.length, this.length);
        vertex(0, this.length);
        endShape(CLOSE);
        pop();
    }
}

let arr = [];
let N = 75;
let lattice = nj.random([N + 2, N + 2])
for (let row = 1; row < N + 1; row++) {
    for (let col = 1; col < N + 1; col++) {
        if (lattice.get(row, col) >= .75) {
            lattice.set(row, col, 0.5);
        } else {
            lattice.set(row, col, -0.5);
        }
    }
}

for (let i = 0; i < N + 2; i++) {
    lattice.set(i, 0, 0);
    lattice.set(0, i, 0);
}

let config;
let config2;
let energyLine;
let magnetizationLine;
let ctxEnergy;
let ctxMagnetization;
let T;

let slider;
let output;


function setup() {

    slider = document.getElementById("myRange");
    output = document.getElementById("demo");

    output.innerHTML = slider.value; // Display the default slider value

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = this.value;
    }

    T = slider.value;

    config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Energy diagram',
                backgroundColor: window.chartColors.red,
                borderColor: window.chartColors.red,
                data: [

                ],
                fill: false,
            }]
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time step'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Energy'
                    }
                }]
            }
        }
    };

    config2 = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Magnetization diagram',
                backgroundColor: window.chartColors.red,
                borderColor: window.chartColors.red,
                data: [

                ],
                fill: false,
            }]
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time step'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Magnetization'
                    }
                }]
            }
        }
    };

    ctxEnergy = document.getElementById('canvasE').getContext('2d');
    ctxMagnetization = document.getElementById('canvasM').getContext('2d');
    energyLine = new Chart(ctxEnergy, config);
    magnetizationLine = new Chart(ctxMagnetization, config2);

    createCanvas(420, 420);
    background(0);

    arr = [];

    for (let row = 1; row < N + 1; row++) {
        for (let col = 1; col < N + 1; col++) {
            arr.push(new Arrow(20 + arrow_size * row, 20 + arrow_size * col, .5));
        }
    }

};

function draw() {

    for (let row = 1; row < N + 1; row++) {
        for (let col = 1; col < N + 1; col++) {
            arr[(row - 1) * N + col - 1].update(lattice.get(row, col));
        }
    }

    update();
};

function update() {
    if (config.data.datasets.length > 0) {
        config.data.labels.push(frameCount);

        config.data.datasets.forEach(function (dataset) {
            dataset.data.push(calc_energy(lattice));
        });

        energyLine.update(0);
    }

    if (config2.data.datasets.length > 0) {
        config2.data.labels.push(frameCount);

        config2.data.datasets.forEach(function (dataset) {
            dataset.data.push(calc_magnetization(lattice));
        });

        magnetizationLine.update(0);
    }

    T = slider.value;

    lattice = step(lattice, T);
};