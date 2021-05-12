FROM python:3.8
RUN mkdir -p /usr/src/app
COPY ./app/ /usr/src/app/
COPY ./requirements.txt /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 80

CMD streamlit run /usr/src/app/main.py
