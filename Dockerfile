FROM python:2.7
COPY ./ /redis/
COPY ./.git* /root/
RUN pip install itchat
WORKDIR /redis/ChatRecords
CMD ["python", "syncgroupchat.py"]
