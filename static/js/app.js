function makePrediction() {
    const data = {
        age: parseFloat(document.getElementById('age').value),
        sex: parseInt(document.getElementById('sex').value),
        cp: parseInt(document.getElementById('cp').value),
        trestbps: parseFloat(document.getElementById('trestbps').value),
        chol: parseFloat(document.getElementById('chol').value),
        fbs: parseInt(document.getElementById('fbs').value),
        restecg: parseInt(document.getElementById('restecg').value),
        thalach: parseFloat(document.getElementById('thalach').value),
        exang: parseInt(document.getElementById('exang').value),
        oldpeak: parseFloat(document.getElementById('oldpeak').value),
        slope: parseInt(document.getElementById('slope').value),
        ca: parseInt(document.getElementById('ca').value),
        thal: parseInt(document.getElementById('thal').value),
    };

    fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `<strong>${data.message}</strong>`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = `<span style='color: red;'>Error: ${error.message}</span>`;
        });
}
