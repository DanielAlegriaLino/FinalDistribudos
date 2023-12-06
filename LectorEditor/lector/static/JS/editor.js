const runbtn = document.querySelector(".run")

let codeBlocks = document.querySelectorAll('.editor') 

codeBlocks.forEach(block => {
    let editor = ace.edit(block);
    editor.setOptions({autoScrollEditorIntoView: true})
    editor.setTheme('ace/theme/chaos')
    editor.session.setMode("ace/mode/javascript");
    editor.setValue('console.log("Hola, Sigma Coders!");')
})

function createBlock(){
    
}

function executeCode(){

}

let editor;