FROM jupyter/base-notebook:python-3.11

# Copy config file
COPY jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py

# Create work directory nd permissions for it
RUN mkdir -p /home/jovyan/work && \
    chown -R jovyan:users /home/jovyan/.jupyter /home/jovyan/work

# Set Docker Working directory
WORKDIR /home/jovyan/work

# Set JupyterLab (optional)
RUN pip install --no-cache-dir jupyterlab

# Open port
EXPOSE 8888

# Start notebook with our configs
CMD ["jupyter", "notebook", "--no-browser"]
