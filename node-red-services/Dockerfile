FROM nodered/node-red

RUN npm install node-red-contrib-cloudantplus node-red-node-watson node-red-contrib-play-audio

ADD flows.json flows.json

EXPOSE 1880

CMD ["node-red", "flows.json"]
