FROM python:3
ADD device.py /
RUN pip install faker
RUN pip install argparse
ARG run_min
ENTRYPOINT [ "python", "./device.py"]
CMD ["--run_min", $run_min]