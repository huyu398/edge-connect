FROM huyu398/deep_learning_env:cuda10_python3.7

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace

RUN apt update \
 && apt -y install gfortran liblapack-dev libopencv-dev curl unzip \
 && apt -y clean \
 && rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt   ./requirements.txt
ADD ./scripts              ./scripts
ADD ./config.yml.example   ./config.yml.example
RUN bash ./scripts/download_model.sh
RUN pip install -r requirements.txt
RUN python -c "from torchvision import models; models.vgg19(pretrained=True)"

RUN pip install ipdb
