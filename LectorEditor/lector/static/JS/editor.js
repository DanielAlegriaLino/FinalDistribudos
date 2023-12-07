const runbtn = document.querySelector(".run")
const output = document.querySelector(".output")
const analysis = document.getElementById("TextAnalisis")
const host = '/microservicio?code='
const host_analizadorcodigo = "/microservicio/analizar_codigo?code="

let codeBlock = document.querySelector('.editor') 
let editor = ace.edit(codeBlock);
editor.setOptions({autoScrollEditorIntoView: true})
    editor.setTheme('ace/theme/chaos')
    editor.session.setMode("ace/mode/javascript");
    if (document.getElementById('resultado').value == ''){
        editor.setValue('console.log("Hola, Sigma Coders!");')
    }
    else{
        var codigo = document.getElementById('resultado').value;
        var lineas = codigo.split(';');
        var nuevoCodigo = lineas.join(';\n');
        editor.setValue(`${nuevoCodigo}`);
    }

runbtn.addEventListener('click', () => {
    let code = editor.getValue();
    let encoded = encodeURIComponent(code);
    console.log(encoded)
    fetch(`${host}${encoded}`)
    .then(response => {
        return response.text();
    })
    .then(text => {
        if(text.length<100){
            output.textContent = text
            console.log(text)
        }
    })
    analysis.textContent = "Analizando"

    fetch(`${host_analizadorcodigo}${encoded}`)
    .then(response => {
        return response.text();
    })
    .then(text => {
            analysis.textContent=text
            console.log(text)
    })
})

function concatenarSpan() {
    var analisis = editor.getValue();
    document.getElementById('resultado').value = analisis;
}