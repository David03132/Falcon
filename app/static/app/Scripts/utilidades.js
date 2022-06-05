function checkRut(rut) {
    // Despejar Puntos
    var valor = rut.value.replace('.', '');
    // Despejar Guión
    valor = valor.replace('-', '');

    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();

    // Formatear RUN
    rut.value = cuerpo + '-' + dv

    // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 7) {
        rut.setCustomValidity("RUT Incompleto");
        return false;
    }

    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;

    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {

        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);

        // Sumar al Contador General
        suma = suma + index;

        // Consolidar Múltiplo dentro del rango [2,7]
        if (multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

    }

    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);

    // Casos Especiales (0 y K)
    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;

    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) {
        /*rut.setCustomValidity("RUT Inválido");*/
        document.getElementById("hrut").innerHTML = "⛔Rut no válido"
        return false;
    }
    else {
        document.getElementById("hrut").innerHTML = "✔ Rut correcto";
        document.getElementById("hrut").className = "text-success";
        rut.setCustomValidity('');
    }

    // Si todo sale bien, eliminar errores (decretar que es válido)

}

function sololetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    especiales = [8, 37, 39, 46];

    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if(letras.indexOf(tecla) == -1 && !tecla_especial)
        return false;
}

function solonumeros(e){

    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key);
    numeros = "0123456789";
    especiales = [8, 37, 39, 46];
    
    tecla_especial = false;
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if(numeros.indexOf(tecla) == -1 && !tecla_especial)
        return false;
}

function ValidarTelefono(fono) {
    if (fono.value.length < 9) {
        document.getElementById("ntel").innerHTML = "Debe ingresar 9 dígitos xd"
        document.getElementById("ntel").className = "form-text text-warning";
        return false;
    }
    if (fono.value.length > 9) {
        document.getElementById("ntel").innerHTML = "Debe ingresar 9 dígitos"
        document.getElementById("ntel").className = "form-text text-warning";
        return false;
    }
    else {
        document.getElementById("ntel").innerHTML = "Longitud correcta";
        document.getElementById("ntel").className = "form-text text-success";
    }
}

function validarpass() {

    var p2 = document.getElementById("psw2").value;
    var p1 = document.getElementById("psw1").value;

    if (p1 != p2) {

        document.getElementById("helpconf").innerHTML = "⚠ No coinciden las contraseñas";
        document.getElementById("helpconf").className = "form-text text-warning";


    }

    else {
        document.getElementById("helpconf").innerHTML = "✔ Contraseñas correctas";
        document.getElementById("helpconf").className = "form-text text-success";


    }

}

function validaremail() {

    var p2 = document.getElementById("email2").value;
    var p1 = document.getElementById("email1").value;

    if (p1 != p2) {

        document.getElementById("helpemail").innerHTML = "⚠ Los e-mails no coinciden";
        document.getElementById("helpemail").className = "form-text text-warning";


    }

    else {
        document.getElementById("helpemail").innerHTML = "✔ e-mail correcto";
        document.getElementById("helpemail").className = "form-text text-success";


    }

}


function validar() {

    p1 = document.getElementById("psw1").value;
    p2 = document.getElementById("psw2").value;
    var obj = document.getElementById("psw2");
    if (p1 != p2) {
        //alert("No");

        obj.setCustomValidity('Las contraseñas deben ser iguales');
        return false;
    }
    else {
        //alert("Si");
        obj.setCustomValidity('');
        return true;
    }
}

function validar2() {

    p1 = document.getElementById("email1").value;
    p2 = document.getElementById("email2").value;
    var obj = document.getElementById("email2");
    if (p1 != p2) {
        //alert("No");

        obj.setCustomValidity('Los e-mails deben ser iguales');
        return false;
    }
    else {
        //alert("Si");
        obj.setCustomValidity('');
        return true;
    }
}

    function FormatoEmail(mail) {
        if (mail.value.indexOf("@") == -1) {
            document.getElementById("mail").innerHTML = "⚠ E-mail incorrecto";
        }
        else {
            document.getElementById("mail").innerHTML = "E-mail correcto";
        }
}























