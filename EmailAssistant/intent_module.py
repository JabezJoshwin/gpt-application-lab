INTENTS=["Delivery Issue","Refund Request","Product Complaint","Technical Support","Order Cancellation","General Inquiry"]
def detect_intent(client,email):return client.classify(email,INTENTS)
