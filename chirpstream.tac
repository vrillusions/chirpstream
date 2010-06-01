#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Chirpstream Bot

XMPP bot that will listen for twitter user stream

"""
import sys
sys.path.append('wokkel')

import ConfigParser
from twisted.application import service
from twisted.words.xish import domish
from twisted.words.protocols.jabber.jid import JID
from twisted.words.protocols.jabber.xmlstream import toResponse

from wokkel import client
from wokkel.xmppim import MessageProtocol
from wokkel.xmppim import PresenceProtocol
from wokkel.xmppim import AvailablePresence
from wokkel.keepalive import KeepAlive


config = ConfigParser.RawConfigParser()
config.read('config.ini')
jid = JID(config.get('login', 'jid'))
password = config.get('login', 'password')

class PresenceAcceptingHandler(PresenceProtocol):
    """
    Presence accepting XMPP subprotocol handler.

    This handler blindly accepts incoming presence subscription requests,
    confirms unsubscription requests and responds to presence probes.

    """
    def subscribedReceived(self, presence):
        """Subscription approval confirmation was received."""
        pass

    def unsubscribedReceived(self, presence):
        """Unsubscription confirmation was received."""
        pass

    def subscribeReceived(self, presence):
        """
        Subscription request was received.

        Always grant permission to see our presence.
        
        """
        self.subscribe(presence.sender)
        self.subscribed(recipient=presence.sender,
                        sender=presence.recipient)
        self.available(recipient=presence.sender,
                       status=u"I'm here",
                       sender=presence.recipient)

    def unsubscribeReceived(self, presence):
        """
        Unsubscription request was received.

        Always confirm unsubscription requests.
        
        """
        self.unsubscribe(presence.sender)
        self.unsubscribed(recipient=presence.sender,
                          sender=presence.recipient)

    def probeReceived(self, presence):
        """
        A presence probe was received.

        Always send available presence to whoever is asking.
        
        """
        self.available(recipient=presence.sender,
                       status=u"I'm here",
                       sender=presence.recipient)


class ChirpbotProtocol(MessageProtocol):
    """Message subprotocol handler."""
    def connectionMade(self):
        print 'Client connected.'
        # Send initial presence
        self.send(AvailablePresence())
    
    def connectionLost(self, reason):
        print 'Connection lost:', reason
    
    def _sendMessage(self, msg, jid):
        response = domish.Element((None, 'message'))
        response['to'] = jid
        response['type'] = 'chat'
        response.addElement('body', content=unicode(msg))
        self.send(response)
    
    def onMessage(self, message):
        # Ignore error messages
        if message.getAttribute('type') == 'error':
            return
        
        if message.body and unicode(message.body):
            self._sendMessage(message.body, message['from'])


application = service.Application('Chirpstream')
xmppClient = client.XMPPClient(jid, password)
xmppClient.logTraffic = True
xmppClient.setServiceParent(application)
KeepAlive().setHandlerParent(xmppClient)

presenceHandler = PresenceAcceptingHandler()
presenceHandler.setHandlerParent(xmppClient)

chirpbot = ChirpbotProtocol()
chirpbot.setHandlerParent(xmppClient)
