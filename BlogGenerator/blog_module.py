def generate_blog(client, data):
    result = client.generate('Write a complete original blog with an introduction, sections and conclusion. Follow the topic, style, tone and approximate word_count. Do not invent statistics or citations.', data)
    return result
