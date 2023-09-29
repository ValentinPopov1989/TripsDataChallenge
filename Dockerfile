FROM python:latest
WORKDIR /code
ADD . /code/results
COPY . .
RUN pip install -r ./requirements.txt
RUN pip install -e ./trips_processor_package

CMD ["python", "-u", "./trips_processor_package/trips_processor"]