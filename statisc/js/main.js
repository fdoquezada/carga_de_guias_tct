// Ejemplo de validación de formulario
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const inputs = form.querySelectorAll('input, textarea');
            let isValid = true;

            inputs.forEach(function(input) {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert('Por favor, complete todos los campos.');
            }
        });
    }
});