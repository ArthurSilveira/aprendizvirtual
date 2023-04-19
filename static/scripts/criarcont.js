function gerarblocotxt() {
    var nameatual = Number(document.getElementById("txtquant").value) + Number(document.getElementById("imgquant").value);
    var novalabel = document.createElement("label");
    novalabel.setAttribute("name", "label"+nameatual);
    novalabel.setAttribute("for", "inputtxt"+nameatual);
    novalabel.innerText = "Texto:";

    var novoinput = document.createElement('textarea');
    novoinput.setAttribute("name", "inputtxt"+nameatual);
    novoinput.setAttribute("type", "text");
    novoinput.classList.add("barratexto2");

    nameatual++;
    var novadiv = document.createElement('div');
    novadiv.appendChild(novoinput);
    novadiv.classList.add("div-barratexto");
    var criador = document.getElementById("adicionarbloco");
    document.getElementById("formcriador").insertBefore(novalabel, criador);
    document.getElementById("formcriador").insertBefore(novadiv, criador);
    attordem("txt");
    attquant("txt");
};

function gerarblocoimg() {
    var nameatual = Number(document.getElementById("txtquant").value) + Number(document.getElementById("imgquant").value);
    var novalabel = document.createElement("label");
    novalabel.setAttribute("name", "label"+nameatual);
    novalabel.setAttribute("for", "inputimg"+nameatual);
    novalabel.innerText = "Caminho da imagem:";

    var novoinput = document.createElement('input');
    novoinput.setAttribute("name", "inputimg"+nameatual);
    novoinput.setAttribute("type", "file");
    novoinput.setAttribute("accept","image/png, image/jpeg")
    novoinput.innerText = "Selecionar imagem"
    
    var novadiv = document.createElement('div');
    novadiv.appendChild(novalabel);
    novadiv.appendChild(novoinput);
    
    var criador = document.getElementById("adicionarbloco");
    document.getElementById("formcriador").insertBefore(novalabel, criador);
    document.getElementById("formcriador").insertBefore(novadiv, criador);
    attordem("img");
    attquant("img");
};

function attquant(type) {
    var quant = document.getElementById(type+"quant");
    quant.value++;
};

function attordem(type) {
    var num = Number(document.getElementById("txtquant").value) + Number(document.getElementById("imgquant").value);
    var ordem = document.getElementById(type+"ordem");
    ordem.value += num;
    ordem.value += ";";
}
