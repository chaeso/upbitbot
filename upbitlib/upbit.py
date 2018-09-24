import requests
import jwt
import time
import platform
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

PROTOCOL = 'https'
HOST = 'api.upbit.com'
VERSION = 'v1'

class Upbit(object):
    """
    Python wrapper for the Upbit API
    """

    def __init__(self, access_key, secret_key):
        self.host_url = '{0:s}://{1:s}/{2:s}/'.format(PROTOCOL, HOST, VERSION)
        self.access_key = str(access_key) if access_key is not None else ''
        self.secret_key = str(secret_key) if secret_key is not None else ''

    def __api_query(self, authorization=False, path=None, method='get', query_params=None):
        with requests.Session() as s:
            headers = {'User-Agent': platform.platform()}
            url = '{0:s}{1:s}'.format(self.host_url, path)
            if authorization:
                payload = {
                        'access_key': self.access_key,
                        'nonce': str(int(time.time() * 1000))
                }
                if query_params is not None:
                    payload['query'] = query_params
                    url = '{0:s}?{1:s}'.format(url, query_params)
                token = jwt.encode(payload, self.secret_key, algorithm='HS256')
                headers['Authorization'] = 'Bearer {0:s}'.format(token.decode('utf-8'))
                req = requests.Request(method, url, headers=headers)
            else:
                req = requests.Request(method, url, headers=headers, params=query_params)
            prepped = s.prepare_request(req)
            response = s.send(prepped)
        return response.json() if response.status_code is 200 or response.status_code is 201 else None

    def get_markets(self):
        return self.__api_query(path='market/all', method='get')

    def get_candles_per_minutes(self, minute, market, to='', count=1, cursor=0):
        if minute not in {1, 3, 5, 15, 10, 30, 60, 240}:
            raise Exception('{0:d}-minute interval is not available.'.format(minute))
        query_params = {'market': market,
                        'to': to,
                        'count': count,
                        'cursor': cursor}
        return self.__api_query(path='candles/minutes/{0:d}'.format(minute), method='get', query_params=query_params)

    def get_candles_daily(self, market, to='', count=1):
        query_params = {'market': market,
                        'to': to,
                        'count': count}
        return self.__api_query(path='candles/days', method='get', query_params=query_params)

    def get_candles_weekly(self, market, to='', count=1):
        query_params = {'market': market,
                        'to': to,
                        'count': count}
        return self.__api_query(path='candles/weeks', method='get', query_params=query_params)

    def get_candles_monthly(self, market, to='', count=1):
        query_params = {'market': market,
                        'to': to,
                        'count': count}
        return self.__api_query(path='candles/months', method='get', query_params=query_params)

    def get_trading_history(self, market, to='', count=1, cursor=''):
        query_params = {'market': market,
                        'to': to,
                        'count': count,
                        'cursor': cursor}
        return self.__api_query(path='trades/ticks', method='get', query_params=query_params)

    def get_ticker(self, markets):
        query_params = {'markets': markets}
        return self.__api_query(path='ticker', method='get', query_params=query_params)

    def get_accounts(self):
        return self.__api_query(authorization=True, path='accounts', method='get')

    def get_order_chance(self, market):
        query_params = urlencode({'market': market})
        return self.__api_query(authorization=True, path='orders/chance', method='get', query_params=query_params)

    def get_order_list(self, market, state='wait', page=1, order_by='asc'):
        query_params = urlencode({'market': market,
                                  'state': state,
                                  'page': page,
                                  'order_by': order_by})
        return self.__api_query(authorization=True, path='orders', method='get', query_params=query_params)

    def get_order(self, uuid):
        query_params = urlencode({'uuid': uuid})
        return self.__api_query(authorization=True, path='order', method='get', query_params=query_params)

    def place_order(self, market, side, volume, price, ord_type='limit'):
        query_params = urlencode({'market': market,
                                  'side': side,
                                  'volume': volume,
                                  'price': price,
                                  'ord_type': ord_type})
        return self.__api_query(authorization=True, path='orders', method='post', query_params=query_params)

    def cancel_order(self, uuid):
        query_params = urlencode({'uuid': uuid})
        return self.__api_query(authorization=True, path='order', method='delete', query_params=query_params)

    def get_withdraw_list(self, currency, state, limit=100):
        query_params = urlencode({'currency': currency,
                                  'state': state,
                                  'limit': limit})
        return self.__api_query(authorization=True, path='withdraws', method='get', query_params=query_params)

    def get_withdraw(self, uuid):
        query_params = urlencode({'uuid': uuid})
        return self.__api_query(authorization=True, path='withdraw', method='get', query_params=query_params)

    def get_withdraw_chance(self, currency):
        query_params = urlencode({'currency': currency})
        return self.__api_query(authorization=True, path='withdraws/chance', method='get', query_params=query_params)

    def withdraw_crypto(self, currency, amount, address):
        query_params = urlencode({'currency': currency,
                                  'amount': amount,
                                  'address': address})
        return self.__api_query(authorization=True, path='withdraws/coin', method='post', query_params=query_params)

    def withdraw_krw(self, amount):
        query_params = urlencode({'amount': amount})
        return self.__api_query(authorization=True, path='withdraws/krw', method='post', query_params=query_params)

