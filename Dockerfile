FROM python:3.10.0-alpine3.15
WORKDIR /app
# COPY requirements.txt
RUN pip install click==8.0.3
RUN pip install colorama==0.4.4
RUN pip install Flask==2.0.2
RUN pip install itsdangerous==2.0.1
RUN pip install Jinja2==3.0.3
RUN pip install MarkupSafe==2.0.1
RUN pip install Werkzeug==2.0.2
 
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT ["python","./src/app.py"]