/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js

    Adapted from Code Institute's Boutique Ado Walkthrough
*/


// Step 1: Retrieve Stripe public key and client secret
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Step 2: Initialize Stripe with the public key
var stripe = Stripe(stripePublicKey);

// Step 3: Create an instance of Stripe Elements
var elements = stripe.elements();

// Step 4: Define the style for the card element
var style = {
    base: {
        color: '#323232',
        fontFamily: '"Poppins", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#959595',
        }
    },
    invalid: {
        color: '#c70000',
        iconColor: '#C70000'
    }
};

// Step 5: Create the card element
var card = elements.create('card', {
    style: style,
    hidePostalCode: true
});

// Step 6: Mount the card element to the specified DOM element
card.mount('#card-element');

