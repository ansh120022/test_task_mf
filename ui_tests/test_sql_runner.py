import pytest
from query_page import QueryPage


query_1 = "SELECT address FROM customers WHERE ContactName = 'Giovanni Rovelli';"
query_2 = "SELECT count(*) FROM customers WHERE city='London';"


@pytest.mark.parametrize(
    "query, expected_result", [(query_1, "Via Ludovico il Moro 22"), (query_2, "6")]
)
def test_select_data(bro, query, expected_result):
    QueryPage(bro).send_query(query)
    assert (
        QueryPage(bro).wait_for_expected_result(expected_result) == "Found"
    ), f"Expected result {expected_result} not found "


update_query_1 = (
    "INSERT INTO Customers (CustomerName, City, Country) VALUES ('Test Customer', "
    "'Test city', 'Test country');"
)
verification_query_1 = (
    "SELECT count(*) FROM Customers WHERE CustomerName='Test Customer' AND "
    "city='Test city' AND country='Test country';"
)
update_query_2 = (
    "INSERT INTO Customers (CustomerName, City, Country) VALUES ('Test Customer', "
    "'Test city', 'Test country');"
)
verification_query_2 = (
    "SELECT count(*) FROM Customers WHERE CustomerName='Test Customer' AND "
    "city='Test city' AND country='Test country'"
)


@pytest.mark.parametrize(
    "update_query, verification_query, expected_result",
    [
        (update_query_1, verification_query_1, 1),
        (update_query_2, verification_query_2, 1),
    ],
)
def test_update_data(bro, update_query, verification_query, expected_result):
    QueryPage(bro).send_query(update_query)
    assert (
        QueryPage(bro).check_update_status() == "Found"
    ), f"The data was not updated correctly"
    QueryPage(bro).send_query(verification_query)
    assert (
        QueryPage(bro).wait_for_expected_result(expected_result) == "Found"
    ), f"Expected result {expected_result} not found "
