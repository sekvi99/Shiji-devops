from prometheus_client import Counter, Histogram, CollectorRegistry

# Create a custom CollectorRegistry
registry = CollectorRegistry()

# Define your custom metrics
total_requests = Counter(
    'app_requests_total',
    'Total number of requests',
    ['method', 'endpoint'],
    registry=registry
)

request_duration = Histogram(
    'app_request_duration_seconds',
    'Request duration in seconds',
    ['method', 'endpoint'],
    registry=registry
)