FROM python:2.7
COPY ./ /redis/
RUN pip install itchat
WORKDIR /redis/ChatRecords
CMD ["python", "syncgroupchat.py"]
