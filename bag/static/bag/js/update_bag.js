// Handles form update when there are Qty changes


$(document).ready(function () {
    console.log('update form buttons');

    var timeoutId; 
    
    function submitForm() {
        clearTimeout(timeoutId); 


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
                
                $(this).closest('form').submit();
            } else {
                
                var errorMessage = 'Please enter a valid quantity between 1 and 99';
                var errorElement = $(this).closest('form').find('.error-message');
                errorElement.text(errorMessage).show(); 
            }
        }.bind(this), 500); 
    }

    $('.decrement-qty').on('click', submitForm);
    $('.increment-qty').on('click', submitForm);
    $('.qty_input').on('input', submitForm);
});