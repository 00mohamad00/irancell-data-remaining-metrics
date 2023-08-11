FROM docker.repos.balad.ir/python:3.10

WORKDIR /home/cost-monitoring

ADD ./requirements.txt .
RUN python3 -m pip install -r ./requirements.txt

COPY . .

ENTRYPOINT ["python3", "src/main.py"]
