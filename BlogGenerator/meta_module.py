def generate_meta(client, data):
    result = client.generate('Write one SEO meta description of at most 160 characters. Return only the description.', data)
    if len(result)>160:
        result=result[:157].rstrip()+"..."
    return result
