function enviarTexto() {
    var inputElement = document.getElementById("outputR");
    var texto = inputElement.value;

    // Llama a la función que deseas con el texto como argumento
    miFuncion(texto);
}
function miFuncion(mensaje) {
    alert("Texto recibido: " + mensaje);
}