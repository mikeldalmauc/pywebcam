# Use a base image with Python and OpenCV
FROM python:3



# Install dependencies
RUN apt-get update

RUN apt-get install -y ffmpeg libsm6 libxext6

RUN adduser appuser
USER appuser

# Install python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

# Define environment variable
ENV NAME World

# -- RUN 

# Run Jupyter Notebook when the container launches
# CMD ["python", "-m", "notebook"]

# CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", " --no-browser", "--allow-root"]

# Run the Python script
# CMD ["python", "./webcam/camera.py"]

# RUN waiting process

CMD ["/bin/bash", "-c", "while true; do echo 'Hit CTRL+C'; sleep 60; done"]