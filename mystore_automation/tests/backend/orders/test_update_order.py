import pytest
from src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from src.generichelpers.generic_order_helpers import GenericOrderHelpers
pytestmark = [pytest.mark.orders, pytest.mark.regression]
from src.utilities.genericUtilities import generate_random_string
@pytest.mark.parametrize('newstatus', 
                         [
                           pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke,pytest.mark.ecombe55]),
                           pytest.param('completed',marks=[pytest.mark.tcid56,pytest.mark.ecombe56]),
                           pytest.param('on-hold', marks=[pytest.mark.tcid57,pytest.mark.ecombe57])
                         ])

def test_update_order_status(newstatus):
  generic_order_helper = GenericOrderHelpers()
  order_api_helper = OrdersAPIHelper()
  if newstatus == 'completed':
    generic_order_helper.create_order({'status':'pending'})

  else:
    order = generic_order_helper.create_order()
    cur_status = order['status']
    assert cur_status!=newstatus

    order_id =  order['id']
    payload={'status':newstatus}

    updated_order = order_api_helper.update_order(order_id=order_id, payload=payload)

    assert updated_order['status'] == newstatus



@pytest.mark.ecombe58
@pytest.mark.tcid58
@pytest.mark.ecombe58
def test_update_order_status_to_random_string():
    """
        Test case to verify the update of an order's status to a random string fails.
    """
    new_status = generate_random_string(length=5)
    generic_order_helper = GenericOrderHelpers()
    order_api_helper = OrdersAPIHelper()
    order = generic_order_helper.create_order()
    order_id = order['id']
    payload = {'status':new_status}

    updated_order = order_api_helper.update_order(order_id=order_id, payload=payload, status_code=400)

    assert updated_order['code'] == 'rest_invalid_param'
    assert updated_order['message'] == 'Invalid parameter(s): status'

@pytest.mark.tcid59
@pytest.mark.ecombe59
def test_update_order_customer_note():
    """
        Test case to verify the update of an order's customer note.

    """
    customer_note = generate_random_string(length=10)
    generic_order_helper = GenericOrderHelpers()
    order_api_helper = OrdersAPIHelper()
    order = generic_order_helper.create_order()
    order_id = order['id']
    payload = {'customer_note':customer_note}

    updated_order = order_api_helper.update_order(order_id=order_id, payload=payload)

    assert updated_order

    new_order = order_api_helper.retrive_order(order_id=order_id)

    assert new_order['id'] == order_id
    assert new_order['customer_note'] == customer_note


