# TODO

0. Quick motivation
1. Start with hello world app - show deployment
	- try also a flask app that does image manipulation?
2. Talk about serverless in general
3. Explore memories.ninja
4. Using a Django app
5. summarize pros, cons, pain points
6. summarize what wasn't talked about


https://edgarroman.github.io/zappa-django-guide/walk_database/
https://edgarroman.github.io/zappa-django-guide/


# Events and Callbacks

- file upload events
- scheduled runtime to poll AWS SQS

# Deployment

```
zappa deploy dev
zappa update dev
zappa tail 		// Errors
zappa status 	// Info
```

Set up ~/.aws/credentials usings `awscli`

- Creates IAM Role + permission policy
- Creates package zip file (~35MB)
- Uploads zip file to AWS
- deploys API gateway

Takes ~5 minutes for a "hello world" package.

flask: https://xev6vkhrhe.execute-api.ap-southeast-2.amazonaws.com/dev
django: https://2wy5kpj0oc.execute-api.ap-southeast-2.amazonaws.com/dev

note that the project "dev" has a trailing "/dev"

# Pre-packaged

Zappa uses the  lambda packages project to fetch pre-compiled
binarys for the lambda environment

* PIL
* Pyscopg2

# Flask vs Django

- flask a lot simpler to set up, no dependence on a database
- flask "hello world" a lot simpler to get working out of the box

- django requires using external static files or whitenoise
* Running managment commands


# Debugging

```
zappa tail
```

logs are in ???
environment not always reproducible (PIL versions)
AWS environment a blessing and a curse
but it's easy to set up a dev/test/staging environment


# Events and scheduled tasks

!!!!!!!!!!!!!!!!!!!!!!111


# Static Files

django-storages
zappa manage dev "collectstatic --noinput"


# Possible but out of scope

* Custom domain
* Secrets
* IAM Roles

# Conclusion

Very easy to get a quick Flask app up with Zappa

You _can_ run a Django app with Zappa, but if you're going to the trouble you should probably consider just setting up a VM.

- management commands have no stdin
