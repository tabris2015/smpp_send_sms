import logging
import sys

import smpplib.gsm
import smpplib.client
import smpplib.consts



# if you want to know what's happening
logging.basicConfig(level='DEBUG')

import smpplib
import settings

client = None
try:
        client = smpplib.client.Client(settings.SMS_SYSTEM_HOSTNAME, settings.SMS_SYSTEM_PORT)
        client.connect()
        try:
                client.bind_transmitter(system_id=settings.SMS_SYSTEM_ID, password=settings.SMS_SYSTEM_PASSWORD)

                client.send_message(source_addr_ton=smpplib.consts.SMPP_TON_INTL,
                        source_addr='9535134654',
                        dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                        destination_addr='9535134654',
                        short_message='hola sms'.encode())
        finally:
                #print "==client.state====", client.state
                if client.state in [smpplib.consts.SMPP_CLIENT_STATE_BOUND_TX]:
                        #if bound to transmitter
                        try:
                                client.unbind()
                        except smpplib.exceptions.UnknownCommandError as ex:
                                #https://github.com/podshumok/python-smpplib/issues/2
                                try:
                                        client.unbind()
                                except smpplib.exceptions.PDUError as ex:
                                        pass
finally:
        if client:
                #print "==client.state====", client.state      
                client.disconnect()
                #print "==client.state====", client.state