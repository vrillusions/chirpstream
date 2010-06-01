# Chirpstream

Chirpstream is a xmpp (jabber) bot that connects to twitter's user stream api.

## Current Status

Currently the user stream api is in beta with limited capability.  This should only be used for development until twitter finally releases it from beta later this year.

## Setup

* git clone git://github.com/chirpstream.git
* git submodule init
* git submodule update
* copy config.sample.ini to config.ini and edit
* twistd -y chirpstream.tac

## Features

* Streams messages from all people you are following

## Roadmap

Items that are planned to be implemented

* works with twitter's list functionality (ie only follow people in a specific list)
* posting, including handling url shortening
* (post v1) support identi.ca in some way

## Purpose

This is going to be my biggest python project yet and using it as a learning exercise.  This means everything will be built from scratch so no forking of existing twitter libraries or anything.

## Requirements

* Python v2.6 - may work in older versions but no guarantees
* [Twisted](http://twistedmatrix.com/trac/) - specifics will be mentioned once  I figure it out myself

