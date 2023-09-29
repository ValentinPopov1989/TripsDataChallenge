FROM postgres:latest
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=trips_challenge

COPY create_db.sql /docker-entrypoint-initdb.d/create_db.sql