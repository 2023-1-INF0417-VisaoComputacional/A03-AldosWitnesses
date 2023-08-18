FROM python

ENV CAPTIONING_SERVER=192.168.1.3:1881

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 -y && \
    pip install -U flask requests katna

#RUN git clone https://github.com/GabrielvanderSchmidt/Image2TextServer.git

#WORKDIR Image2TextServer

RUN mkdir videos

ADD main.py main.py

EXPOSE 1882

CMD ["python3", "-u", "main.py"]
