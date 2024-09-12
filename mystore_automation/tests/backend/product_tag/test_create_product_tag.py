from src.api_helpers.ProductsTagAPIHelper import ProductsTagAPIHelper
import pytest
import random
from src.utilities.genericUtilities import generate_random_string
@pytest.mark.ecombe110
def test_create_product_tag():
  random_str=generate_random_string(length=5)
  data = {
    "name": random_str
  }
  product_tag = ProductsTagAPIHelper.call_create_product_tag(payload=data)

  import pdb; pdb.set_trace()