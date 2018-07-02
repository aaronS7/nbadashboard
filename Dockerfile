FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY mvp.csv ./
ADD seasons ./
COPY plotlynba.py ./

CMD ["gunicorn", "plotlynba:server", "-b", "0.0.0.0:8050"]