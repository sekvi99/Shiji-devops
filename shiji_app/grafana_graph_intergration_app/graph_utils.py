from decimal import Decimal
from plotly.offline import plot
from typing import Any
import plotly.graph_objects as go
import datetime

class PlotlyGraphHandler:
    """
    Class for managing all of plot needed methods.
    """
    
    @staticmethod
    def get_float_fields(record) -> list[Any]:
        """
        Static method for checking whether provided key of dictionary is numerical.
        Args:
            record (_type_): Slice of .json.

        Returns:
            list[Any]: List of keys that are numerical.
        """
        return [key for key, value in record.items()
                if isinstance(value, Decimal) or isinstance(value, float)]
        
    @staticmethod
    def get_timestamp_fields(record) -> str:
        """
        Static method for checking which key of provided record is datelike value.
        Args:
            record (_type_): Slice of .json

        Returns:
            str: String representation of datelike key name.
        """
        for key, value in record.items():
            if isinstance(value, datetime.date):
                return key
        return None
    
    @staticmethod
    def generate_graph(data) -> plot:
        """
        Static method for generating plotly.offline graph object.

        Args:
            data (_type_): QuerySet of django models object.

        Raises:
            ValueError: Occures when got unexpected variable type.

        Returns:
            plot: Plotly graph object.
        """
        if not data:
            raise ValueError('Lack of values to plot.')
        
        datelike_col = PlotlyGraphHandler.get_timestamp_fields(data[0])
        
        if not datelike_col:
            raise ValueError('Expected datetime column!')
        
        dates = [element.get(datelike_col) for element in data]
        graphs = [go.Scatter(x=dates, y=[element.get(numeric_col) for element in data],
         legendgroup="group1", legendgrouptitle_text = 'Available variables:', mode='lines', name=numeric_col)
         for numeric_col in PlotlyGraphHandler.get_float_fields(data[0])]
    
        layout = {'template': 'plotly_white', 'legend_groupclick': 'toggleitem'}
    
        return plot(dict({'data': graphs, 'layout': layout}), output_type='div')