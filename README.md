<p style='text-align: justify;'>

## SUFIS

To build the docker image and run the container:

```
docker image build -f Dockerfile -t sufis-app .
docker run -p 8000:8000 sufis-app

```

The app is available at http://localhost:8000 in your browser. To stop the container:

```
docker stop sufis-app
docker rm sufis-app
docker system prune -f
```

### Founders
- Gordei Pribõtkin
- Filipp Petuhhov
- Mart Hint
</p>