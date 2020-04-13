FROM nvcr.io/nvidia/tensorflow:19.04-py3


RUN apt-get update \
    && pip3 install fire regex

ADD gpt-2 /workspace/gpt-2

USER root
WORKDIR /workspace/gpt-2/
EXPOSE 80

CMD ["python3","./src/interactive_conditional_samples.py","--top_k","40"]
