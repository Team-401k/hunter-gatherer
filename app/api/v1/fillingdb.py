from app.api.v1.external_apis.pp_api import PayPalAPI
from app.api.v1.external_apis.stripe_api import StripeAPI
from app.api.v1.external_apis.sqsp_api import SquareSpaceAPI

#would call this function with dates to get all three for that month
#notice how for each API, only have to create the object and then call the search_parse function
#also, all now take the same date format, so this fill_db function's parameters can just be passed to each api's seach_parse function to get the orders from that month
def fill_db(start_date: str, end_date: str):
    # First get the parsed orders from paypal
    paypal_api = PayPalAPI()
    pp_orders = paypal_api.search_parse(start_date, end_date)

    #get the parsed orders from stripe
    stripe_api = StripeAPI()
    stripe_orders_data = stripe_api.search_parse(start_date, end_date)
    stripe_orders = stripe_orders_data.data

    #get the parsed orders from squarespace
    sqsp_api = SquareSpaceAPI()
    sqsp_orders_result = sqsp_api.search_parse(start_date, end_date)
    sqsp_orders = sqsp_orders_result.result


    ### Then would try to match stripe and paypal with squarespace to get all info, and then put in database. See below for example of how to access parsed fields.  ####

    ##### EXAMPLE OF HOW TO ACCESS PARSED FIELDS #######
    #look at external_apis/schemas.py to see what are the fields for each that you can access
    #the ones labeled main model are the what the parsing creates a list of, so that model's fields are immediately accessible like the example below

    for order in stripe_orders:
        print(order.amount)

    for order in pp_orders:
        print(order.transaction_amount)

    for order in sqsp_orders:
        print(order.grandTotal.value)
        
#currently doesn't fill the db actually, but does call all three apis for orders within the dates passed, parses their response, and then prints the amounts of each order within that month from each api
fill_db('2024-02-16T00:00:00Z', '2024-03-10T23:59:59Z')
