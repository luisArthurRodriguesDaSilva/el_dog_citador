FROM python:3.8.10
COPY . /WD
RUN pip install --upgrade pip  && pip install numpy && pip install tweepy && pip install python-dotenv && pip install requests && pip install beautifulsoup4 && pip install openai && pip install Pillow 
WORKDIR /WD
CMD python main.py