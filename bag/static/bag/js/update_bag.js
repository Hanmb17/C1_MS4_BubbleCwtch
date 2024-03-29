// Handles form update when there are Qty changes


$(document).ready(function () {
    console.log('update form buttons');

    var timeoutId; 
    
    function submitForm() {
        clearTimeout(timeoutId); // Clear any existing timeout

        // Schedule validation after a delay of 500 milliseconds (adjust as needed)
        timeoutId = setTimeout(function () {
            // Get the value of the quantity input
            var quantityInput = $(this).closest('form').find('.qty_input');
            var quantityValue = quantityInput.val();

            // Check if the quantity value is valid
            if (
                quantityValue !== '' &&                      // Not empty
                !isNaN(quantityValue) &&                    // Is a number
                quantityValue >= 1 &&                        // At least 1
                quantityValue <= 99 &&                       // At most 99
                quantityValue.indexOf('.') === -1 &&        // No decimal point
                quantityValue.indexOf(',') === -1 &&        // No comma
                quantityValue.length <= 2                   // At most two characters
            ) {
                // If validation passes, submit the form
                $(this).closest('form').submit();
            } else {
                // Show an error message below the increment button
                var errorMessage = 'Please enter a valid quantity between 1 and 99';
                var errorElement = $(this).closest('form').find('.error-message');
                errorElement.text(errorMessage).show(); // Set error message text and show it
            }
        }.bind(this), 500); // Delay of 500 milliseconds
    }

    $('.decrement-qty').on('click', submitForm);
    $('.increment-qty').on('click', submitForm);
    $('.qty_input').on('input', submitForm);
});