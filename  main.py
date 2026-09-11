# Receipt Generator

from pyscript import display, document


def generate_receipt(e):

    subtotal = 0

    receipt = "Your Receipt "


    if document.getElementById('cake').checked:
        subtotal = subtotal + 180
        receipt = receipt + "Love-lock Cheesecake - ₱180"

    if document.getElementById('donut').checked:
        subtotal = subtotal + 50
        receipt = receipt + "Tongue-twister Sourdough Donut - ₱50"

    if document.getElementById('pizza').checked:
        subtotal = subtotal + 220
        receipt = receipt + "The Romantic Cheezy Pizza - ₱220"

    if document.getElementById('cola').checked:
        subtotal = subtotal + 100
        receipt = receipt + "Love-shot Cola - ₱100"

    if document.getElementById('icecream').checked:
        subtotal = subtotal + 120
        receipt = receipt + "Soulmate Duo Ice Cream - ₱120"

    vat = subtotal * 0.12

    total_amount = subtotal + vat

    receipt = receipt + f"Subtotal: ₱{subtotal}"
    receipt = receipt + f"VAT (12%): ₱{vat}"
    receipt = receipt + f"Total Amount:₱{total_amount}"

   

    display(receipt, target='result')

