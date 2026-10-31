def generate_keywords(client, data):
    result = client.generate('Generate SEO keywords relevant to this blog. Return a concise comma-separated list.', data)
    return result
