# 0x1A. Application server
`DevOps` `SysAdmin`

**Concepts**
* [Web Server](https://intranet.alxswe.com/concepts/17)
* [Server](https://intranet.alxswe.com/concepts/67)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)

![Application server](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240819T110858Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e45aa051826c376ef1c064fdce033db1f9061a24a5e7cab12cfaa2473c2d8014)

## Background context
My web infrastructure is already serving web pages via Nginx that I installed in my first web stack project.
While a web server can also serve dynamic content, this task is usually given to an application server.
In this project I will add this piece to my infrastructure, plug it to my `Nginx` and make is serve my Airbnb clone project.

## Resources
**Read or watch:**
* [Application server vs web server](https://www.f5.com/glossary)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) *As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally*
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/3.0.x/)
* [Upstart documentation](https://doc.ubuntu-fr.org/upstart)
