from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from typing import Final
from .utils import CurrencyRatesAPIConnectorHandler
from .graph_utils import PlotlyGraphHandler
from .models import EurCurrencyModel, GBPCurrencyModel, USDCurrencyModel
from typing import Any

API_CONNECTION_STRING: Final[str] = 'https://www.bankier.pl/new-charts/get-data?symbol={currency}PLN&intraday=false&type=area&max_period=true'

@login_required(login_url='/login/')
def home(request) -> render:
    eur_graph = None
    usd_graph = None
    gbp_graph = None
    
    # ! Refresh Euro data
    eur = CurrencyRatesAPIConnectorHandler('eur')
    eur.set_api_endpoint(API_CONNECTION_STRING)
    eur.preprocess_api_output()
    
    # ! Refresh USD data
    usd = CurrencyRatesAPIConnectorHandler('usd')
    usd.set_api_endpoint(API_CONNECTION_STRING)
    usd.preprocess_api_output()
    
    # ! Refresh GBP data
    gbp = CurrencyRatesAPIConnectorHandler('gbp')
    gbp.set_api_endpoint(API_CONNECTION_STRING)
    gbp.preprocess_api_output()
    
    try:
        eur_graph = PlotlyGraphHandler.generate_graph(EurCurrencyModel.objects.values())
        usd_graph = PlotlyGraphHandler.generate_graph(USDCurrencyModel.objects.values())
        gbp_graph = PlotlyGraphHandler.generate_graph(GBPCurrencyModel.objects.values())
    except Exception as e:
        print(str(e))
    
    context: dict[str, Any] = {
            'eur_graph':eur_graph,
            'usd_graph':usd_graph,
            'gbp_graph':gbp_graph
            }
    return render(
        request,
        'pages/dashboard.html',
        context
    )
    
@login_required(login_url='/login/')
def about(request) -> render:
    
    techstack: Final[list] = [
        {'title': 'Python', 'body': 'Python is a popular high-level programming language known for its simplicity, readability, and versatility. It is used for a wide range of applications, including web development, data analysis, artificial intelligence, and more.'},
        {'title': 'Django', 'body': ' Django is a free and open-source web framework for Python, designed to help developers build web applications quickly and easily. It includes a wide range of tools and features for handling common web development tasks, such as routing, templating, authentication, and more.'},
        {'title': 'Prometheus', 'body': 'Prometheus is a free and open-source monitoring and alerting system designed for large-scale, cloud-native environments. It provides a flexible and powerful platform for collecting, storing, and visualizing metrics from a wide range of sources, making it easier to monitor and troubleshoot complex systems.'},
        {'title': 'Grafana', 'body': 'Grafana is a popular open-source dashboard and data visualization tool, used for displaying and analyzing data from a wide range of sources. It includes a wide range of features for creating and customizing dashboards, charts, and alerts, and is used by many organizations to monitor and analyze their data.'},
        {'title': 'AWS', 'body': 'Amazon Web Services (AWS) is a cloud computing platform that provides a wide range of services and tools for building, deploying, and managing applications and infrastructure in the cloud. It includes a wide range of tools and services for computing, storage, networking, database management, security, and more, making it easier for organizations to scale and manage their cloud-based applications and services.'},
    ]
    context = {
        'techstack': techstack,
    }
    return render(
        request,
        'pages/about.html',
        context
    ) 
