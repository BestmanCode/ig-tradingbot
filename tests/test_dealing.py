from trading_ig.rest import IGService
import responses
import json
import pandas as pd

"""
unit tests for dealing methods
"""


class TestDealing:

    # login v1

    @responses.activate
    def test_workingorders_happy(self):

        with open('tests/data/workingorders.json', 'r') as file:
            response_body = json.loads(file.read())

        responses.add(responses.GET,
                      'https://demo-api.ig.com/gateway/deal/workingorders',
                      headers={'CST': 'abc123', 'X-SECURITY-TOKEN': 'xyz987'},
                      json=response_body,
                      status=200)

        ig_service = IGService('username', 'password', 'api_key', 'DEMO')
        ig_service.crud_session.HEADERS["LOGGED_IN"] = {}
        result = ig_service.fetch_working_orders()

        pd.set_option('display.max_columns', 50)
        print(result)

        assert isinstance(result, pd.DataFrame)
        assert result.iloc[0]['instrumentName'] == 'Spot Gold'
        assert result.iloc[0]['exchangeId'] == 'FX_C_GCSI_ST'
        assert result.iloc[0]['marketStatus'] == 'EDITS_ONLY'
        assert result.iloc[0]['level'] == 2000.0
        assert result.iloc[0]['epic'] == 'CS.D.CFDGOLD.CFDGC.IP'
        assert result.iloc[0]['currencyCode'] == 'USD'
