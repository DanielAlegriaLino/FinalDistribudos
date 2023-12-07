const runbtn = document.querySelector(".run")
const output = document.querySelector(".output")
const host = 'http://127.0.0.1:8000/microservicio?code='

let codeBlock = document.querySelector('.editor') 
let editor = ace.edit(codeBlock);
editor.setOptions({autoScrollEditorIntoView: true})
    editor.setTheme('ace/theme/chaos')
    editor.session.setMode("ace/mode/javascript");
    editor.setValue('console.log("Hola, Sigma Coders!");')

runbtn.addEventListener('click', () => {
    let code = editor.getValue();
    let encoded = encodeURIComponent(code);
    console.log(encoded)
    fetch(`${host}${encoded}`)
    .then(response => {
        return response.text();
    })
    .then(text => {
        console.log(text)
        output.textContent = text
    })
})