from pathlib import Path, PurePath
import json

# Path to the directory containing the brand files
BRAND_DATA_DIR = "brand_data"

class Brand:
  """
  Brand class. Holds name, description, and product names
  """
  def __init__(self, name, description, products):
      self.name = name
      self.description = description
      self.products = products

  def __str__(self):
      return f"{self.name}: {self.description}\nProducts: {[p['name'] for p in self.products]}"

def get_brands():
  """
  Pulls a list of brands from the brands.json file.
  """
  with Path(PurePath('DB', BRAND_DATA_DIR, 'brands.json')).open(mode='r') as f:
    brands = json.load(f)

  brand_list = []
  for brand in brands:
    products = []
    for product in brand["products"]:
      products.append(product)
    brand_list.append(Brand(brand["name"], brand["description"], products))

  return brand_list

def get_sublist(brand):
  """
  Get a list of subreddits for a given brand. TODO: implement
  """
  sublist = ['buzzmasters']
  return sublist

def get_timecode(dt):
  """
  Generate a timecode from a datetime object.
  """
  return dt.hour