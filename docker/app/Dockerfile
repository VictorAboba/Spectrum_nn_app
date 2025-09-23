FROM pytorch/pytorch:2.7.1-cuda12.6-cudnn9-devel
WORKDIR /app

COPY . /app/

RUN chmod u+rx entrypoints/entrypoint.sh

RUN pip --no-cache-dir install -r requirements.txt

RUN sed -i 's/\r$//' /app/entrypoints/entrypoint.sh

ENTRYPOINT [ "entrypoints/entrypoint.sh" ]