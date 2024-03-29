// Handles quantity input for products
// Adapted from Code Institute's Boutique Ado Walkthrough
$(document).ready(function() { console.log('Document Ready'); 
console.log('loaded');

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`.id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});


$('.increment-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var allInputs = $(`.input-group-${itemId} input`);
    var currentValue = parseInt($(closestInput).val());
    $(allInputs).val(currentValue + 1);
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var allInputs = $(`.input-group-${itemId} input`);
    var currentValue = parseInt($(closestInput).val());
    $(allInputs).val(currentValue - 1);
    handleEnableDisable(itemId);
});

})