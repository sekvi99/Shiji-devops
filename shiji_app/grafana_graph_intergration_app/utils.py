from datetime import datetime
from django.db import models
from django.apps import apps
import requests
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Final
import re

# Constant for mapping currency name to propper django model
CURRENCY_TO_MODEL_MAPPER: Final[dict[str, str]] = dict({
    'usd': 'USDCurrencyModel',
    'euro': 'EurCurrencyModel',
    'gbp': 'GBPCurrencyModel'
})

@dataclass
class APIConnectorHandler(ABC):
    """
    Definition of APIConnectorHandler that definies interfaces (abstract methods) for required behaviours in derivative classes.
    """  
    api_endpoint: str = field(default=str, init=False) # API Endpoint to fetch data from
    url_regex: str = field(default_factory=lambda: "^(https?|ftp)://[^\s/$.?#].[^\s]*$", init=False)
    
    def format_string_url(self, input_string, currency: str) -> str:
        """
        Definition of method for propper handling string url formatting.
        Args:
            input_string (_type_): Url string representation to be formatted.

        Returns:
            str: Formatted string url.
        """
        return input_string.replace('{currency}', currency)
    
    def get_model_class(self, model_name: str) -> models.Model:
        """
        Definition of method for propper finding model class by it's name.
        Args:
            model_name (str): String representation of class model name.

        Returns:
            Model: Class for passed model_name.
        """
        try:
            model_class = apps.get_model(app_label='grafana_app', model_name=model_name)
            return model_class
        except LookupError:
            return None
    
    @abstractmethod
    def set_api_endpoint(self, url: str) -> None:
        """
        Definition of interface for setting propper url in derivative class.
        
        Args:
            url (str): String representation of url to fetch data from.
        """
        ...
        
    @abstractmethod
    def preprocess_api_output(self) -> None:
        """
        Definition of interface for propperly formatting output from url to expected format data and save it to django models.
        """
        ...
         

@dataclass
class CurrencyRatesAPIConnectorHandler(APIConnectorHandler):
    """
    Class for common methods definition for every currency rate.

    Args:
        APIConnectorHandler (_type_): Inheritence of APIConnectorHandler class.
    """
    
    currency: str
    
    def format_currency_timestamp_to_date(self, timestamp: int) -> str:
        """
        Helper method for formatting timestamps retrived from API to propper date format.
        Args:
            timestamp (int): Timestamp date representation.

        Returns:
            str: Expected string representation of date %Y-%m-%d.
        """
        timestamp = timestamp / 1000
        dt = datetime.fromtimestamp(timestamp)
        formatted_date = dt.strftime('%Y-%m-%d')
        return formatted_date
    
    def set_api_endpoint(self, url: str) -> None:
        """
        Implementation of defined interface for propper setting passed url as endpoint for given class instance.
        Args:
            url (str): String representation of url.

        Raises:
            SyntaxError: Occures when provided string does not match regex url definition.
        """
        if re.match(self.url_regex, url):
            self.api_endpoint = self.format_string_url(url, currency=(self.currency).upper())
        else:
            raise SyntaxError(f'Invalid syntax of provided url string!')
    
    def process_extracted_currency_rate_data(self, data: dict[Any], currency: str) -> None:
        """
        Method for saving new instance object to propper model based on passed currency type.

        Args:
            data (dict[Any]): Json data extracted from API request.
            currency (str): String representation of currency.
        """
        for item in data['navigator']:
            # Extracing date and value from api request
            print(item[0])
            date = self.format_currency_timestamp_to_date(item[0])
            currency_value = item[1]
            
            # Trying to extract model instance object for given date
            propper_model_class = self.get_model_class(CURRENCY_TO_MODEL_MAPPER.get(currency))
            currency_existing_instance = propper_model_class.objects.filter(date = date)
            
            if currency_existing_instance:
                ...
            else:
                new_instance = propper_model_class(date, currency_value)
                new_instance.save()
            
        
        
    def preprocess_api_output(self) -> None:
        """
        Definition of defined interface in base class.
        """
        response = requests.get(self.api_endpoint)
        data = response.json()
        self.process_extracted_currency_rate_data(data, self.currency)
            