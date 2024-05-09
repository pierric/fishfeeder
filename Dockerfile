ARG BUILD_FROM
FROM $BUILD_FROM
RUN apk add --no-cache python3 py3-pip py3-smbus i2c-tools
COPY test.py /
CMD ["python3", "/test.py"]
