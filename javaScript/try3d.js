c
// Exemplo de uso:
const lambda = 1; // valor de exemplo   
const beta = 45; // valor de exemplo
const x = 10; // valor de exemplo
const y = 5; // valor de exemplo
//resultado 3.79
console.log("Resultado = " + calculate(lambda, beta, x, y));


function teste(){
        fetch('http://127.0.0.1:5000/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na requisição: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Mostra o resultado no elemento <pre>
            document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            document.getElementById("resultado").textContent = 'Erro: ' + error.message;
        });
    
}
