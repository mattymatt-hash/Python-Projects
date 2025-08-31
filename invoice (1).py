"""
* Name         : program name   Class Assignment
* Author       : Matthew Stevens
* Created      : Creation Date 7-1
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is manage customer invoice data. The input is invoice id and customer id.The output is a printed invoice for the list items
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""


class Invoice:
 def __init__(self, invoice_id, customer_id):
        self._invoice_id = invoice_id                           # Implement __init__ method. Remove pass when finished.
        self._customer_id = customer_id
        self.ditems = {}
   
def invoice_id(self):
        return self._invoice_id                                  # Implement add_item method. 

def invoice_id(self, value):
        self._invoice_id = value                                    

def print_invoice(self):
        print(f"CUSTOMER: {self.customer_id}")                    # Implement print_invoice method.
        print(f"INVOICE: {self.invoice_id}")
        for item, price in sorted(self.ditems.items(), key=lambda x: x[1]):
            print(f"{item}: {price:.2f}")
        print()  
                                                                    # Implement __str__ special method.
def __str__(self):
        return f"Invoice[{self.invoice_id}] for Customer[{self.customer_id}] with {len(self.ditems)} items."




def main():

    invoices_list = [
        {"invoice_id": "A554GFT-117", "customer_id": "98676867", "items": [("ipad", 499.99), ("mouse", 29.97), ("monitor", 229.08)]},
        {"invoice_id": "J244GFT-283", "customer_id": "77594872", "items": [("router", 267.78), ("hdmi-cable", 24.77)]},
        {"invoice_id": "R943RXC-476", "customer_id": "54092341", "items": [("laptop", 1399.54), ("warranty", 199.94), ("snickers", 2.49)]},
        {"invoice_id": "J712WQR-888", "customer_id": "43908134", "items": [("amplifier", 749.00), ("speaker-cable", 42.75)]}
    ]

    for record in invoices_list:
        inv = Invoice(record["invoice_id"], record["customer_id"])                        # Iterate over invoices_list. After items have been added to instance dictionary,
        for item_name, price in record["items"]:                                        # call print_invoice.
            inv.add_item(item_name, price)
        inv.print_invoice()
    

if __name__ == "__main__":

    main()

