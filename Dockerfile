FROM python:3.9.0

WORKDIR /usr/src/app

# For safety reason, create an user with lower privileges than root and run from there
RUN useradd -m -d /home/acc-bot -s /bin/bash acc-bot && \
    mkdir /usr/src/acc-bot && \
    chown -R acc-bot /usr/src/acc-bot

USER acc-bot

COPY requirements.txt ./
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
