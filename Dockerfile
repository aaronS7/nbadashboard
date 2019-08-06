FROM python:3

WORKDIR /usr/src/app

RUN echo 'nameserver 8.8.8.8' >> /etc/resolve.conf && echo 'nameserver 8.8.4.4' >> /etc/resolve.conf

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY mvp.csv ./
ADD seasons ./
COPY plotlynba.py ./

CMD ["gunicorn", "plotlynba:server", "-b", "0.0.0.0:8050"]
