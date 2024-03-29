// Handles form update when there are Qty changes


$(document).ready(function () {
    console.log('update form buttons');

    function submitForm(e) {
        e.preventDefault();
        $(this).closest('form').submit();
    }

    $('.decrement-qty').on('click', submitForm);

    $('.increment-qty').on('click', submitForm);

    $('.qty_input').on('input', submitForm);
});