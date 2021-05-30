[PythonによるWebスクレイピング 〜Webアプリケーション編〜](https://www.udemy.com/share/101ZsUAkcZdVZUQHg=/) の成果物

## Development

```
docker-compose build
docker-compose run --rm web python setup.py
docker-compose up
```

## Deploy

```
git push heroku master

# inisiazize
heroku create sample-soruma
heroku buildpacks:set heroku/python
heroku run python setup.py
```