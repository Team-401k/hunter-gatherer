# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_client.models.balances_response import BalancesResponse

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class BalancesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def balances_get(
        self,
        as_of_time: Annotated[Optional[Annotated[str, Field(min_length=20, strict=True, max_length=64)]], Field(description="List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.")] = None,
        currency_code: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]], Field(description="Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BalancesResponse:
        """List all balances

        List all balances. Specify date time to list balances for that time that appear in the response.<blockquote><strong>Notes:</strong> <ul><li>It takes a maximum of three hours for balances to appear in the list balances call.</li><li>This call lists balances upto the previous three years.</li></ul></blockquote>

        :param as_of_time: List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.
        :type as_of_time: str
        :param currency_code: Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._balances_get_serialize(
            as_of_time=as_of_time,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BalancesResponse",
            '400': "Error400",
            '403': "Error403",
            '500': "Error500",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def balances_get_with_http_info(
        self,
        as_of_time: Annotated[Optional[Annotated[str, Field(min_length=20, strict=True, max_length=64)]], Field(description="List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.")] = None,
        currency_code: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]], Field(description="Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BalancesResponse]:
        """List all balances

        List all balances. Specify date time to list balances for that time that appear in the response.<blockquote><strong>Notes:</strong> <ul><li>It takes a maximum of three hours for balances to appear in the list balances call.</li><li>This call lists balances upto the previous three years.</li></ul></blockquote>

        :param as_of_time: List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.
        :type as_of_time: str
        :param currency_code: Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._balances_get_serialize(
            as_of_time=as_of_time,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BalancesResponse",
            '400': "Error400",
            '403': "Error403",
            '500': "Error500",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def balances_get_without_preload_content(
        self,
        as_of_time: Annotated[Optional[Annotated[str, Field(min_length=20, strict=True, max_length=64)]], Field(description="List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.")] = None,
        currency_code: Annotated[Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]], Field(description="Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all balances

        List all balances. Specify date time to list balances for that time that appear in the response.<blockquote><strong>Notes:</strong> <ul><li>It takes a maximum of three hours for balances to appear in the list balances call.</li><li>This call lists balances upto the previous three years.</li></ul></blockquote>

        :param as_of_time: List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided.
        :type as_of_time: str
        :param currency_code: Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency.
        :type currency_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._balances_get_serialize(
            as_of_time=as_of_time,
            currency_code=currency_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BalancesResponse",
            '400': "Error400",
            '403': "Error403",
            '500': "Error500",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _balances_get_serialize(
        self,
        as_of_time,
        currency_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if as_of_time is not None:
            
            _query_params.append(('as_of_time', as_of_time))
            
        if currency_code is not None:
            
            _query_params.append(('currency_code', currency_code))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/reporting/balances',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


