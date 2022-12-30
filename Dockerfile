FROM python:latest
COPY . /WD
RUN pip install tweepy && pip install python-dotenv && pip install requests && pip install beautifulsoup4
WORKDIR /WD
CMD python main.py