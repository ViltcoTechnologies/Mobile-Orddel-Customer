import stripe as s

s.api_key = "sk_test_51IVGKwDfezRTPDs3rwZEwqnKVGp6o9ehpuOIQyCJ5opnwQ6Bwi6O9HBVx2x48sTpjRkDZt4e2EPuSUrfKtfpLyKj00g1s0RcGH"

response = s.PaymentMethod.create(
  type="card",
  card={
    "number": "4242424242424242",
    "exp_month": 3,
    "exp_year": 2022,
    "cvc": "314",
  },
)
print(response)
# stripe.PaymentIntent.create(
#   amount=2000,
#   currency="gbp",
#   payment_method_types=["card"],
# )

response = s.Subscription.create(
  customer="cus_J8uG0Z40cyJa7U",
  items=[
    {"price": "price_1IWcSI2x6R10KRrh5aZYfN3y"},
  ],
)