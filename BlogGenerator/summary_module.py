def generate_summary(client, data):
    result = client.generate('Summarize the supplied blog in approximately 100 words. Preserve its meaning.', data)
    return result
