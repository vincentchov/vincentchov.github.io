Title: My experience at Hamp Hack 2017
Date: 2017-04-17
Slug: hamp-hack-2017
Category: Hackathons
Summary: I attended another hackathon!

Hamp Hack 2017 was the third hackathon I ever attended.  On the bus ride over, I eagerly found guides on web development in Flask to provide my teammates.  My three teammates, John Bojorquez from Google, Tony Pham from Pratt and Whitney, and Julie Pham, all were newcomers to hackathons.  It was my job to show them a good time and help make their first hackathon a good one.  

Early on, we decided to write an app that helps people keep track of memorable locations and share them with their friends and family.  It offers users a way to follow the breadcrumbs of where people have been and reviewed.  Imagine Yelp, but more personalized.

I was in charge of setting up everyone's computers with a Python dev environment, which was pretty straightforward to do considering that everyone used a Unix-like OS on their laptops.  I set up the GitHub repo and the initial scaffolding of the Flask app and we were good to go.

While I have made full-stack apps before, most of my experience is with the backend and thankfully Julie had some experience with it and introduced me to Materialize CSS, this awesome framework like Bootstrap that lets you make web apps that resemble Android apps' Material Design.

We found what we thought was a quiet room to work in and started listing out tasks on a whiteboard.  I was in charge of the backend, using OAuth2 for Google Authentication, creating location pins on the map and deployment on AWS.

I say "what we thought was a quiet room" because little did we know, the reading room we were in was attached to an art gallery, where people were nailing pictures to walls all night.  On the bright side, the pictures were beautiful.

In the last hour of the hackathon, I experimented with deployment on AWS, which I never did before.  After an hour of hair pulling, I decided to deploy on Heroku.  Soon, however, I realized that the issue was that in the wsgi file, I'm supposed to import my Flask app as "application" instead of "app".  The wonders of Computer Sorcery and Engineering.

All in all, I think the hackathon was a success.  I was able to introduce 3 people to hackathons, teach them Python, and build a pretty full stack app.  We may not have won, but we learned a lot about the software development process.
