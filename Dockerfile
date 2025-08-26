# start from python base image
FROM python:3.11

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add python code
COPY ./src/ /code/src/

# expose the application port
EXPOSE 80

# specify default commands
CMD ["uvicorn", "src.Backend.app.main:app", "--host", "0.0.0.0", "--port", "80"]