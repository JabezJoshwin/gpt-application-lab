def explain(items):return "\n".join(f"{i}. {item['name']}: {item['reason']}" for i,item in enumerate(items,1))
