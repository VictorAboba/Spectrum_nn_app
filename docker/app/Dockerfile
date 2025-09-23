FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime

WORKDIR /app

COPY . /app/

RUN chmod u+rx entrypoints/entrypoint.sh

RUN pip --no-cache-dir install -r requirements.txt

RUN sed -i 's/\r$//' /app/entrypoints/entrypoint.sh

ENTRYPOINT [ "entrypoints/entrypoint.sh" ]