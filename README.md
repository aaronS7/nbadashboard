### NBA Plotly DASHboard 

The following repo is used to create the web application at [http://nbadashboard.aaronsciroc.co/](http://nbadashboard.aaronsciroc.co/).

To build the image locally using docker, run the following command:

```bash
docker build -t nbadashboard .
docker run -d -p 8888:8050 nbadashboard
```

Navigate to [http://localhost:8888/](http://localhost:8888/) and you will see the application.

To run without docker run the following commands:

```bash
cp -a seasons/* .
pip install --no-cache-dir -r requirements.txt
python plotlynba.py
```