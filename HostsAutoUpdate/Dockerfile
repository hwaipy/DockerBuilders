FROM python:3.12

COPY hostsAuto.py hostsAuto.py
COPY hosts /auto/hosts
RUN pip install requests

ENTRYPOINT python hostsAuto.py
