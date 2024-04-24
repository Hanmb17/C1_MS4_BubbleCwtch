// Handles form update when there are Qty changes
$(document).ready(function () {
    var timeoutId;
    // Function to handle form submission after a delay
    function submitForm() {
        clearTimeout(timeoutId);
        // Set a timeout to execute validation after a delay of 500 milliseconds
        timeoutId = setTimeout(function () {
            var quantityInput = $(this).closest('form').find('.qty_input');
            var quantityValue = quantityInput.val();

            if (
                quantityValue !== '' &&                     
                !isNaN(quantityValue) &&                    
                quantityValue >= 1 &&                        
                quantityValue <= 99 &&                       
                quantityValue.indexOf('.') === -1 &&        
                quantityValue.indexOf(',') === -1 &&
                quantityValue.length <= 2                   
            ) {
                // If validation passes, submit the form
                $(this).closest('form').submit();
            } else {
                // If validation fails, display an error message
                var errorMessage = 'Please enter a valid quantity between 1 and 99';
                var errorElement = $(this).closest('form').find('.error-message');
                errorElement.text(errorMessage).show(); 
            }
        }.bind(this), 500); 
    }
    // Attach the submitForm function to the below elements
    $('.decrement-qty').on('click', submitForm);
    $('.increment-qty').on('click', submitForm);
    $('.qty_input').on('input', submitForm);
});