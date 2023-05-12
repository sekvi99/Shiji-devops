# Shiji-devops
A repository for the storage of files pertaining to a Shiji-related project. Project: devops automation the future.

# Django application
Project has been divided into two seperated applications:

**Login Application**
1. User Authentication,
2. User Registration,
3. User login/ logout functionality.

Implemented solution in *login_app* directory.

**Graph Integration App**
Application creates api calls for endpoint: https://www.bankier.pl/new-charts/get-data?symbol={currency}PLN&intraday=false&type=area&max_period=true. Based on wanted currency type we are supposed to pass propper key between {} and replace currency with one of declared below keys. Based on fetched data from endpoint, new data that does not have its instance in declared models is saved to models application.

Endpoint keys:
1. EUR - Returns timeseries data about value of Euro currency compared to PLN,
2. USD - Returns timeseries data about value of USD currency compared to PLN,
3. GBP - Returns timeseries data about value of GBP currency compared to PLN.

Application is also responsible for creating interactive graphs declared in file: *graph_utils.py*. In this project i've used plotly module to send interactive graph to view.


# How to set up project?
Based on provided *docker-compose.yml* file we're supposed to run below commands, and solution should be build if _docker_ and _docker-compose_ are availabe in given OS. Below command will build three containers:
1. **app** - instance on application working on port 8000,
2. **prometheus** - instance of prometheus monitoring working on port 9090,
3. **grafana** - instance of grafana, for plotting metrics collected from prometheus working on port 3000. 

```
docker-compose -f docker-compose.yml up -d
```
.
