"""
散列表
适用于：模拟映射关系、防止重复、缓存数据
"""
cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
