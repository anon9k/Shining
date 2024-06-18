//funciones usadas en la validación
//validar que un string solo contiene letras
function validarSoloLetras(str) 
{
    const letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (let i = 0; i < str.length; i++) 
    {
        if (!letras.includes(str[i])) 
        {
            return false;
        }
    }
    return true;
}

//validar que un string no tiene más de x número de caractéres
function validarMaximoCaracteres(str,max)
{
    if(str.length > max)
        {
            return false;
        }
    return true;
}

function validarNumeros(str, numero)
{
    if (str.length != numero) 
    {
        return false;
    }

    for (let i = 0; i <str.length; i++) 
    {
        if (str[i] < '0' || str[i] > '9')
        {
            return false; 
        }
    }
    return true;
}

function validarEmail(str) 
{
    const partes = str.split('@');
    if (partes.length !== 2) {
        return false;
    }
    return true;
}



//constantes
const validCountrys = ["España","Francia","Alemania","Italia","UK","Portugal"]

//se crea un evento que se activa al hacer click en el botón
//no se hace un método porque de esa manera no funciona
document.getElementById('billing-form').addEventListener('submit', function(event) 
{
    //previene al formulario de su comportamiento habitual evitando que envie los datos
    //esto se hace para evitar problemas con las urls
    event.preventDefault();


    let isValid = true;
    let errors = [];

    const country = document.getElementById('c_country').value;
    const nombre = document.getElementById('c_fname').value.trim();
    const apellido = document.getElementById('c_lname').value.trim();
    const direccion = document.getElementById('c_address').value.trim();
    const ciudad = document.getElementById('c_state_country').value.trim();
    const codigoPostal = document.getElementById('c_postal_zip').value.trim();
    const email = document.getElementById('c_email_address').value.trim();
    const telefono = document.getElementById('c_phone').value.trim();

    //validaciones

    //validar país
    if(!validCountrys.includes(country))
        {
            errors.push("Selecciona un país válido");
            isValid = false;
        }

    //validar nombre
    if(nombre == "")
        {
            errors.push("El campo nombre es obligatorio");
            isValid = false;
        }
    
    if(!validarSoloLetras(nombre))
        {
            errors.push("El campo nombre solo puede contener letras ");
            isValid = false;
        }

    if(!validarMaximoCaracteres(nombre,15))
        {
            errors.push("El campo nombre no debería tener más de 15 caractéres")
            isValid = false;
        }
    

    //validar apellido
    if(apellido == "")
        {
            errors.push("El campo apellido es obligatorio");
            isValid = false;
        }
    
    if(!validarSoloLetras(apellido))
        {
            errors.push("El campo apellido solo puede contener letras ");
            isValid = false;
        }

    if(!validarMaximoCaracteres(apellido,30))
        {
            errors.push("El campo apellido no debería tener más de 30 caractéres")
            isValid = false;
        }

    //validar dirección
    if(direccion == "")
        {
            errors.push("El campo dirección es obligatorio");
            isValid = false;
        }

    //validar ciudad
    if(ciudad == "")
        {
            errors.push("El campo ciudad es obligatorio");
            isValid = false;
        }
    
    if(!validarSoloLetras(ciudad))
        {
            errors.push("El campo ciudad solo puede contener letras ");
            isValid = false;
        }

    if(!validarMaximoCaracteres(ciudad,20))
        {
            errors.push("El campo ciudad no debería tener más de 20 caractéres")
            isValid = false;
        }
    
    //validar codigo postal
    if(codigoPostal == "")
        {
            errors.push("El campo Código Postal es obligatorio");
            isValid = false;
        }
    
    if(!validarNumeros(codigoPostal,5))
        {
            errors.push("El campo Código Postal debe tener exactamente 5 números");
            isValid = false;
        }
    
    //validar email
    if(email == "")
        {
            errors.push("El campo Email es obligatorio");
            isValid = false;
        }
    if(!validarEmail(email))
        {
            errors.push("El campo Email debe tener una @");
            isValid = false;
        }

    //validar teléfono
    if(telefono == "")
        {
            errors.push("El campo Teléfono es obligatorio");
            isValid = false;
        }
    
    if(!validarNumeros(telefono,9))
        {
            errors.push("El campo Teléfono debe tener 9 números");
            isValid = false;
        }

    //mensaje de error
    //se utiliza la libreria SweetAlert para crear un mensaje de error más estético
    if(isValid == false)
        {
        Swal.fire({
            icon: 'error',
            title: 'Error en el formulario',
            html: errors.join('<br>')
        });
        return;
        }
    
    window.location.href = "/carrito/thankyou/";

});

//
function validar()
{

    //previene al formulario de su comportamiento habitual evitando que envie los datos
    //esto se hace para evitar problemas con las urls
    event.preventDefault();

    let isValid = true;
    let errors = [];

    const nombre = document.getElementById('c_fname').value.trim();
    const apellido = document.getElementById('c_lname').value.trim();
    const email = document.getElementById('c_email_address').value.trim();
    const mensaje = document.getElementById('message').value.trim();
    
    //validar nombre
    if(nombre == "")
        {
            errors.push("El campo nombre es obligatorio");
            isValid = false;
        }
    
    if(!validarSoloLetras(nombre))
        {
            errors.push("El campo nombre solo puede contener letras ");
            isValid = false;
        }

    if(!validarMaximoCaracteres(nombre,15))
        {
            errors.push("El campo nombre no debería tener más de 15 caractéres")
            isValid = false;
        }
    

    //validar apellido
    if(apellido == "")
        {
            errors.push("El campo apellido es obligatorio");
            isValid = false;
        }
    
    if(!validarSoloLetras(apellido))
        {
            errors.push("El campo apellido solo puede contener letras ");
            isValid = false;
        }

    if(!validarMaximoCaracteres(apellido,30))
        {
            errors.push("El campo apellido no debería tener más de 30 caractéres")
            isValid = false;
        }
    
    //validar email
    if(email == "")
        {
            errors.push("El campo Email es obligatorio");
            isValid = false;
        }
    if(!validarEmail(email))
        {
            errors.push("El campo Email debe tener una @");
            isValid = false;
        }
    if(mensaje == "")
        {
            errors.push("Escribe algo en el mensaje");
            isValid = false;
        }
    //mensaje de error
    //se utiliza la libreria SweetAlert para crear un mensaje de error más estético
    if(isValid == false)
        {
        Swal.fire({
            icon: 'error',
            title: 'Error en el formulario',
            html: errors.join('<br>')
        });
        return;
        }
    
    //mensaje de éxito
    Swal.fire({
        icon: 'success',
        title: 'Mensaje enviado!',
        text: 'Hemos recibido tu mensaje, nos pondremos en contacto contigo con la mayor brevedad posible'
        });

}