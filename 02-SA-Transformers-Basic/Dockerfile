FROM tensorflow/tensorflow:2.3.0-gpu

# install generic dependencies (tensorflow, etc.)
ENV TRANSFORMERS_CACHE=/workspaces/transformers/cache
COPY ./dependencies/pip-requirements.txt /tmp/pip-tmp/
RUN pip3 install --upgrade pip
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/pip-requirements.txt \
    && rm -rf /tmp/pip-tmp


# Install Jupyter (to run notebooks locally)
RUN pip install --no-cache-dir jupyter matplotlib
# Pin ipykernel and nbformat; see https://github.com/ipython/ipykernel/issues/422
RUN pip install --no-cache-dir jupyter_http_over_ws ipykernel==5.1.1 nbformat==4.4.0
RUN jupyter serverextension enable --py jupyter_http_over_ws
RUN python3 -m ipykernel.kernelspec

EXPOSE 8888
