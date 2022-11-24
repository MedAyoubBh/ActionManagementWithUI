FROM python:3.10
COPY . /ActionManagement
WORKDIR /ActionManagement
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic
EXPOSE 8000

