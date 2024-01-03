# 0x15. API
`Python` `Scripting` `Back-end` `API`

## Background Context
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bashis perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources
* [Friends don't let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
* [What is an API](https://www.webopedia.com/definitions/api/)
* [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API](https://www.sitepoint.com/rest-api/)
* [What are microservices](https://smartbear.com/learn/api-design/microservices/)

## Learning Objectives
* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

##  API
An API, or Application Programming Interface, is a set of protocols, tools, and routines for building software applications. APIs provide a way for different software applications to communicate with each other, allowing developers to integrate external services into their own applications.

## RESTful API
REST, or Representational State Transfer, is a software architectural style that defines a set of constraints to be used when creating web services. A RESTful API is an API that conforms to these constraints.

### Key Concepts
* API: An interface that allows applications to communicate with each other.
* REST: An architectural style that defines a set of constraints for building web services.
* RESTful API: An API that conforms to the constraints defined by the REST architectural style.
* Resources: Data objects that can be accessed and manipulated through the API.
* HTTP Methods: Verbs used to interact with resources, including GET, POST, PUT, PATCH, and DELETE.

#### RESTful API Design Principles
To design a RESTful API, developers should consider the following principles:
* Client-Server Architecture: Separating the user interface concerns from data storage concerns.
* Statelessness: Each request from client to server must contain all of the information necessary to understand the request, and cannot rely on any context stored on the server.
* Cacheability: Responses to requests must be able to be cached or not cached by clients.
* Layered System: A client cannot tell whether it is connected directly to the end server or to an intermediary along the way.
* Uniform Interface: The same resource should be accessible through a consistent interface, regardless of the type of resource or the location of the resource.

#### RESTful API Best Practices
To create a well-designed RESTful API, developers should follow these best practices:
* Use nouns instead of verbs in endpoints.
* Use HTTP methods correctly, such as GET for reading data and POST for creating data.
* Use HTTP status codes correctly, such as 200 for a successful response and 404 for a resource not found.
* Support versioning to allow future changes without breaking existing clients.
* Provide comprehensive documentation for the API.
