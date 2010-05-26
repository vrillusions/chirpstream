# Chirpstream

Chirpstream is a xmpp (jabber) bot that connects to twitter's user stream api.

## Current Status

Currently the user stream api is in beta with limited capability.  This should only be used for development until twitter finally releases it from beta later this year.

## Features

This is intended to be a single-user bot as of right now.  There won't be a central bot that allows multiple people to connect.  Will be designed to make that option fairly easy to implement in the future, hopefully.

Other features:
* works with twitter's lists (ie only follow people in your "friends" list)
* posting, including handling url shortening

Future features under consideration:
* posting. Initial version will be more of just a consumer instead of publishing
* (post v1) support identi.ca in some way (possibly branch to new project)

## Purpose

This is going to be my biggest python project yet and using it as a learning exercise.  This means everything will be built from scratch so no forking of existing twitter libraries or anything.

## Requirements

* Python v2.6
* [Twisted](http://twistedmatrix.com/trac/) - specifics will be mentioned once  I figure it out myself

