# Define some Tropy API methods

import requests
import json
from itertools import repeat

# Set API endpoint
api_url_base = 'http://localhost:2019'

# Get all Tropy items from the current project
def get_all_items():   
    call = '%s/project/items/' % api_url_base
    res = requests.get(call)
    if res.status_code != 200:
        return
    items_dict = json.loads(res.text)
    itemIDs = [ k['id'] for k in items_dict]
    return itemIDs

# Get a Tropy item:   
def get_item(itemID):
    call = '%s/project/items/%s' % (api_url_base, itemID)
    res = requests.get(call)
    if res.status_code != 200:
        return
    item_info = json.loads(res.text)
    return item_info

# Get Tropy item data
def get_item_data(itemID):
    call = '%s/project/data/%s' % (api_url_base, itemID)
    res = requests.get(call)
    if res.status_code != 200:
        return
    item_data = json.loads(res.text)
    return item_data

# Get a Tropy item's list of photos
def get_item_photos(itemID):
    call = '%s/project/items/%s/photos' % (api_url_base, itemID)
    res = requests.get(call) 
    if res.status_code != 200:
        return
    item_dict = json.loads(res.text)
    photos = [ k['path'] for k in item_dict]
    return photos

# Get a Tropy item's tags
def get_item_tags(itemID):
    call = '%s/project/items/%s/tags' % (api_url_base, itemID)
    res = requests.get(call) 
    if res.status_code != 200:
        return
    item_dict = json.loads(res.text)
    tags = [ k['path'] for k in item_dict]
    return tags

# Create a Tropy tag
def create_tag(name, color=''):
    # if tag already exists return existing tag ID
    tags = get_tags()
    for tag in tags:
        if tag['name'].lower() == name.lower():
            return tag['id']
    params = [('name', name), ('color', color)]
    call = '%s/project/tags' % api_url_base
    res = requests.post(call, data=params)
    if res.status_code != 200:
        return
    tag_json = json.loads(res.text)
    return tag_json['id']
    
# Get a Tropy tag by its name
def get_tag_by_name(name):
    tags = get_tags()
    tag_id = None
    for tag in tags:
        if tag['name'].lower() == name.lower():
            tag_id = tag['id']
            return get_tag_by_id(tag_id)
        else:
            break

# Get a Tropy tag by its ID
def get_tag_by_id(tag_id):
    call = '%s/project/tags/%s' % (api_url_base, tag_id)
    res = requests.get(call)
    if res.status_code != 200:
        return
    return json.loads(res.text)
    
# Get all Tropy tags
def get_tags():
    call = '%s/project/tags' % api_url_base
    res = requests.get(call)
    if res.status_code != 200:
        return
    return json.loads(res.text)

# Tag a Tropy item by tag names
def tag_item_by_tag_name(itemID, tag_names):
    tag_IDs = []
    for tag_name in tag_names:
        tag_IDs.append(create_tag(tag_name))
    params = list(zip(repeat('tag'), tag_names))
    call = '%s/project/items/%s/tags' % (api_url_base, itemID)
    res = requests.post(call, data=params)
    return

# Tag a Tropy item by tag ID
def tag_item_by_tag_ID(itemID, tag_IDs):
    params = list(zip(repeat('tag'), tag_IDs))
    call = '%s/project/items/%s/tags' % (api_url_base, itemID)
    res = requests.post(call, data=params)
    return

# Remove tags from an item by ID
def untag_item_by_tag_ID(itemID, tag_IDs):
    params = list(zip(repeat('tag'), tag_IDs))
    call = '%s/project/items/%s/tags' % (api_url_base, itemID)
    res = requests.delete(call, data=params)
    return

# Remove tags from an item by name
def untag_item_by_tag_name(itemID, tag_names):
    params = list(zip(repeat('tag'), tag_names))
    call = '%s/project/items/%s/tags' % (api_url_base, itemID)
    res = requests.delete(call, data=params)
    return
