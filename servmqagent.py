#!/usr/bin/env python

import os
import sys

import pika
import json
import random
import codecs
import commands
import time
import threading
import random
import smtplib
import multiprocessing 
import traceback
import requests
import cmd

from email.mime.text import MIMEText
from email.header import Header
from multiprocessing import Process, Value, Array
from copy import deepcopy


## ===============================
## | GLOBAL DEFINITIONS          |
## ===============================

EXECPARAMS = {
   'env'             : 'PRD',
   'data-directory'  : '.',
   'lab-vespa-host'  : 'vespa.lab.etzone.net',
   'lab-rmq-hosts'   : [ '172.21.15.41', '172.21.15.42', '172.21.15.43' ],
   'lab-b2eapi-host' : 'dev-bpbe01.etzone.net',
   'lab-smtp-host'   : '',
   'vespa-host'      : 'falcon01.ugo.et2o',
   'rmq-hosts'       : ['10.60.15.51', '10.60.15.52', '10.60.15.53' ],
   'b2eapi-host'     : '10.60.15.24',
   'smtp-host'       : '10.60.11.19',
   'store-data-only' : False,
   'self-monitor'    : False,
   'interactive'     : False,
   'debug'           : False
}

msgrecvtime = 0
msgsendtime = 0



def json_loads_with_noexception(body):

   line = body.split('\n')[-1]
   print '=======', body, '======='
   try:
      jres = json.loads(line)
   except:
      print '[!!] json parsing error, body is : ', line 
      jres = json.loads('{"ErRoR":"not a valid json format"}')   

   #print '[==] jres ==> ', jres
   return jres


def itemopen(dirname, filename, mode):
   global msgrecvtime, msgsendtime

   itemf    = None
   datedir  = time.strftime("%Y%m%d", time.localtime(msgrecvtime))
   millis   = str(msgrecvtime - int(msgrecvtime))[2:8]
   senddate = time.strftime("%j%H%M%S", time.localtime(msgsendtime))

   itemdir  = dirname + '/' + datedir
   itemname = '%s/%s-%s-%s.json' % (itemdir, filename, senddate, millis)

   print '[==] itemname ==>', itemname

   if os.path.exists(itemdir) == True:
      if os.path.isdir(itemdir) == True:
         itemf = codecs.open(itemname, mode, 'utf-8')
      else:
         print '[!!] %s is a filename, something wrong!' % dirname

         itemname = '%s/%s-%s-%s.json' % (dirname, filename, senddate, millis)
         itemf = codecs.open()
   else:
      os.makedirs(itemdir)
      itemf = codecs.open(itemname, mode, 'utf-8')

   return itemname, itemf
   

def tryread_attribute_value(mapo, key):
   if key in mapo.keys():
      return mapo[key]
   else:
      return 0


## ===============================
## | CHANNEL OPERATION FUNCTIONS |
## ===============================

def b2e_product_onoffshelf(body):
   global msgsendtime, EXECPARAMS

   print '[==] =================================='
   print '[@@] Processing onoffshelf message ...|'
   print '[==] =================================='
   
   jsonobj = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime: ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message readbody:\n', body[:100], '.....'

   shelftpl = 'curl --silent \"http://%s:8080/document/v1/ehs-search/%s/docid/%s\"'
   puttpl  = '''
      { "put" : "id:ehs-search:%s::%s", 
        "fields" : {
           "available" : %s,
           "emergencyOff": 1
        }
      }'''   

   # NOTEICE: Here we assume that re-onshelfing one item also means 
   #          it is not a hidden item anymore. 
  
   jsonfmt  = '''
      { "%s" : "id:ehs-search:%s::%s", 
        "fields" : {
           "available"    : { "assign" : %s },
           "emergencyOff" : { "assign" : %s }
        }
      }'''


   # :: eProduct document ::

   en, itemf = itemopen(EXECPARAMS['data-directory'], 'Eonoffshelf', 'w')

   # check this item is onshelf or not

   shelfcmd = shelftpl % (EXECPARAMS['vespa-host'], 'eProduct', jsonobj['FugoSaleNo'])
   print '[==] shelf command = ', shelfcmd
   output   = commands.getoutput(shelfcmd)
   jres     = json_loads_with_noexception(output)

   if 'ErRoR' in jres.keys():
      print '[!!] query vespa cluster failed!'
      jsondata = '{ "ErRoR": "Query vespa cluster failed!" }'
   else:
      if 'fields' not in jres.keys(): # means this is a new item in vespa cluster
         if jsonobj['EOnOffShelf'] == 1:
            jsondata = puttpl % ('eProduct', jsonobj['FugoSaleNo'], 0)
         else:
            jsondata = '''
               { 
                  "ErRoR"  : "Invalid operation: OffShelf a nonexisted item",
                  "RawMsg" : "%s"
               }
            '''

            jsondata = jsondata % jres
      else:
         avb0 = jsonobj['EOnOffShelf']
         avb1 = tryread_attribute_value(jres['fields'], 'available')
         emeg = tryread_attribute_value(jres['fields'], 'emergencyOff')
         
         method = 'update' 
         avab   = 1 if (avb0 == 1 and avb1 == 1) else 0
         
         jsondata = jsonfmt % (method, 'eProduct', jsonobj['FugoSaleNo'], avab, emeg)

   itemf.write('[')
   itemf.write(jsondata)
   itemf.write(']')
   itemf.close()

   # :: uProduct docment ::

   un, itemf = itemopen(EXECPARAMS['data-directory'], 'Uonoffshelf', 'w')

   shelfcmd = shelftpl % (EXECPARAMS['vespa-host'], 'uProduct', jsonobj['FugoSaleNo'])
   output   = commands.getoutput(shelfcmd)
   jres     = json_loads_with_noexception(output)

   if 'ErRoR' in jres.keys():
      print '[!!] query vespa cluster failed!'
      jsondata = '{ "ErRoR":"Query Vespa cluster failed!" }'
   else:
      if 'fields' not in jres.keys(): # means this is a new item in vespa cluster
         if jsonobj['UOnOffShelf'] == 1:
            jsondata = puttpl % ('uProduct', jsonobj['FugoSaleNo'], 0)
         else:
            jsondata = '''
               { 
                  "ErRoR"  : "Invalid operation: OffShelf a nonexisted item",
                  "RawMsg" : "%s"
               }
            '''

            jsondata = jsondata % jres
      else: # very rare case, but not zero percent possibility
         avb0 = jsonobj['UOnOffShelf']
         avb1 = tryread_attribute_value(jres['fields'], 'available')
         emeg = tryread_attribute_value(jres['fields'], 'emergencyOff')         
         
         method = 'update' 
         avab   = 1 if (avb0 == 1 and avb1 == 1) else 0
         
         jsondata = jsonfmt % (method, 'uProduct', jsonobj['FugoSaleNo'], avab, emeg)


   itemf.write('[')
   itemf.write(jsondata)
   itemf.write(']')
   itemf.close()

   #print('[@#]' + en)  # notify the next pipe to processing this line
   #print('[@#]' + un)  # notify the next pipe to processing this line

   # Feed data into vespa
   cmdtpl = 'java -jar vespa-http-client-jar-with-dependencies.jar --file %s --host %s --port %s'
   #cmd0   = cmdtpl % (en, EXECPARAMS['vespa-host'], '8080')
   cmd0   = ''
   cmd1   = cmdtpl % (un, EXECPARAMS['vespa-host'], '8080')

   if EXECPARAMS['store-data-only']  == False:
      #print '[==] cmds ==> ', [cmd0, cmd1]
      print '[==] feedcmd = ', cmd1
      #rc,output0 = commands.getstatusoutput(cmd0)
      rc,output1 = commands.getstatusoutput(cmd1)
      print '[==] feed output = ', output1
      #print output0, output1
   else:
      print '[==] ', cmd0 + ';' + cmd1 

   print '[@@] Processing End.'
   return


def b2e_product_prodspecform(body):
   global msgsendtime, EXECPARAMS

   print '[==] ===================================='
   print '[@@] Processing prodspecform message ...|'
   print '[==] ===================================='

   jsnf = open('datawork/specforms.json', 'a')

   try:
      jsonobj = json.loads(body)
      msgsendtime = jsonobj['UnixTimestamp']

      print '[==] message sendtime: ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
      print '[==] mesgage body    : ', body[:180], ' ...'

      jsnf.write(body)
   except:
      print '[!!] Exception happens!'

   jsnf.close()
   print '[@@] Processing End.'
   return


def b2e_product_hiddenstate(body):
   global msgsendtime, msgsendtime, EXECPARAMS

   print '[==] ===================================='
   print '[@@] Processing hiddenstate message ... |'
   print '[==] ===================================='

   jsonobj = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime: ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body    : ', body
   #print '[==] json ==> ', jsonobj

   # !! B2E changed the message name, but we need to keep consistent with 
   # !! product.sd

   jsonfmt = '''
      { "%s" : "id:ehs-search:%s::%s", 
        "fields" : {
           "emergencyOff" : { "assign" : %s }
        }
      }'''
 

   # OPEN FILE FOR WRITING

   nm0, f0 = itemopen(EXECPARAMS['data-directory'], 'EHiddenStat', 'w')
   nm1, f1 = itemopen(EXECPARAMS['data-directory'], 'UHiddenStat', 'w')

   f0.write('[')
   f1.write('[')

   for i,l in enumerate(jsonobj['List']):
      m = 'update' # 'put' if l['Display'] == '1' else 'update' ; why do i use 'put' for 1?  
      j = jsonfmt % (m, 'eProduct', l['FugoSaleNo'], l['Display'])
      q = jsonfmt % (m, 'uProduct', l['FugoSaleNo'], l['Display'])
      n = ',\n' if (i+1) < len(jsonobj['List']) else '\n'

      f0.write(j + n)
      f1.write(q + n)

   f0.write(']')
   f1.write(']')
   f0.close()
   f1.close()

   #print('[@#]' + nm0) # notify the next pipe to processing this line
   #print('[@#]' + nm1) # notify the next pipe to processing this line

   cmdtpl = 'java -jar vespa-http-client-jar-with-dependencies.jar --file %s --host %s --port %s'

   cmd0   = cmdtpl % (nm0, EXECPARAMS['vespa-host'], '8080')
   cmd1   = cmdtpl % (nm1, EXECPARAMS['vespa-host'], '8080')

   if EXECPARAMS['store-data-only']  == False:
      #rc,output0 = commands.getstatusoutput(cmd0)
      rc,output1 = commands.getstatusoutput(cmd1)

      print '[==] output ===>', output1 
      #print [output0, output1]
   else:
      print '[==] shell commands ===> '
      print [cmd0, cmd1]

   print '[@@] Processing End.'
   return


def b2e_product_category(body):
   global msgsendtime, EXECPARAMS

   print '[==] ========================================'
   print '[@@] Processing product_category message ...|'
   print '[==] ========================================'

   jsonobj  = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime : ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body     : ', body

   # open json file with utf-8 encoding for writing
   cn, jsnf = itemopen(EXECPARAMS['data-directory'], 'EUcategoris', 'w')

   jsnf.write('[')
   jsnf.write(unicode(body, 'utf-8'))
   jsnf.write(']')
   jsnf.close()

   if EXECPARAMS['store-data-only']  == False:
      trantpl  = 'python datatrans.py %s datadone %s %s' 
      feedtpl  = 'java -jar vespa-http-client-jar-with-dependencies.jar --file %s --host %s --port %s'

      # translate category data into feedables
      tran0 = trantpl % (EXECPARAMS['data-directory'], 'Ecategory', cn.split('/',1)[1]) # remove datawork/ from filepath
      tran1 = trantpl % (EXECPARAMS['data-directory'], 'Ucategory', cn.split('/',1)[1]) # remote datawork/ from filepath

      print '[==] translation command:  ==> \n %s\n %s\n' % (tran0, tran1)

      rc,output0 = commands.getstatusoutput(tran0)
      rc,output1 = commands.getstatusoutput(tran1)

      print '[==] translation output ==>\n', output0, output1 

      # feed translated data
      cmd0 = feedtpl % ('datadone/EcategoryNameIds.json', EXECPARAMS['vespa-host'], '8080')
      cmd1 = feedtpl % ('datadone/UcategoryNameIds.json', EXECPARAMS['vespa-host'], '8080')
      cmd2 = feedtpl % ('datadone/Eclasstreetrails.json', EXECPARAMS['vespa-host'], '8080')
      cmd3 = feedtpl % ('datadone/Uclasstreetrails.json', EXECPARAMS['vespa-host'], '8080')

      print '[==] Start feeding:'   
      #output0 = commands.getoutput(cmd0)
      print '[==] Feeding Ucategory data ==> \n',  commands.getoutput(cmd1)
      #output2 = commands.getoutput(cmd2)
      print '[==] Feeding Uclasstreetrails data ==> \n', commands.getoutput(cmd3)

      #print output0, output1, output2, output3
   else:
      print '[==] store data only ...'


   print '[@@] Processing End.'
   return


def collectmsgs(workdir, datedir, start, end):
   allmsgs = os.listdir('%s/%s' % (workdir, datedir))
   results = []

   for i,mo in enumerate(allmsgs):
      tm = mo.split('-')[1]

      if len(tm) != 9:
         continue 

      if tm >= start and tm <= end:
         results.append(mo)

   return results


def geteventtype(msgname):
   if 'onoffshelf' in msgname:
      return 'OnOffShelf'
   elif 'HiddenStat' in msgname:
      return 'HiddenState'
   elif 'EUcategoris' in msgname:
      return 'Category'
   elif 'ProductSpec' in msgname:
      return 'ProdSpecForm'
   elif 'ProductInfo' in msgname:
      return 'ProductInfo'
   elif 'Dcompletion' in msgname:
      return 'DataCompletion'
   elif 'ProductLogs' in msgname:
      return 'ProductLog'
   else:
      return 'Unknown'


def getgoodid(joarray):
   if len(joarray) > 1:
      return 'many' 
   else:
      jo = joarray[0]

   if 'put' in jo.keys():
      return jo['put'].split(':')[4]
   elif 'update' in jo.keys():
      return jo['update'].split(':')[4]
   elif 'ECategories' in jo.keys():
      return jo['ECategories'][0]['FugoSaleNo']
   else:
      return 'NotFound'
   return


def getepochtime(datedir, msgname):
   tm = time.strptime(datedir + msgname.split('-')[1][3:], '%Y%m%d%H%M%S')   

   return int(time.mktime(tm))


def collect_recv_messages(startdt, enddt):
   global EXECPARAMS

   workdir  = EXECPARAMS['data-directory']
   datelist = os.listdir(workdir)

   datelist.sort()

   date0 = time.strftime('%Y%m%d', startdt)
   date1 = time.strftime('%Y%m%d', enddt)

   print '[==] collect date: %s -> %s' % (date0, date1)

   datelist = [d for d in datelist if d >= date0 and d <= date1 ] 
   recvmsgs = []

   for do in datelist:
      msgs = []

      if do == date0 and do == date1: # the same day 
         time0 = time.strftime('%j%H%M%S', startdt)
         time1 = time.strftime('%j%H%M%S', enddt)
      elif do == date0: # the first day
         time0 = time.strftime('%j%H%M%S', startdt)
         time1 = time.strftime('%j235959', enddt)
      elif do == date1: # the latest day
         time0 = time.strftime('%j000000', startdt)
         time1 = time.strftime('%j%H%M%S', enddt)
      else: # interm day, collect all messages
         time0 = time.strftime('%j000000', startdt)
         time1 = time.strftime('%j235959', enddt)

      msgs = collectmsgs(workdir, do, time0, time1)
      msgs = sorted(msgs, key = lambda x: x.split('-')[1])

      print '[==] collected msgs : ', msgs

      for mo in msgs:
         fields = mo.split('-')

         mf = open('%s/%s/' % (workdir, do) + mo)
         md = mf.read()
         jo = json.loads(md)

         epoch  = getepochtime(do, mo)
         evttp  = geteventtype(mo)
         itemid = getgoodid(jo) # for array data, wil return 'many'
       
         if evttp not in ['ProductLog','Unknown']:
            recvmsgs.append('%s,%s,%s' % (itemid, evttp, epoch))

   return recvmsgs

def issue_resend_call(session, url, diffs):
   response = session.post(url, json=diffs)
   
   print '[!!] E2B API responses: content = [%s], status code = %d' % (response.content, response.status_code)
   print '[==] The diffs = ', diffs

   session.close()

   send_alert_mail('mqagent-item-missed', comment = diffs)

   print '[@@] Processing End.'
   return


def b2e_product_productlog(body):
   global msgsendtime, EXECPARAMS

   print '[==] ================================='
   print '[@@] Processing product log messages |'
   print '[==] ================================='

   jsonobj = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime : ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body     : ', body[:130], '...'

   # SORTING ITEM LIST BY TIME
   # '1547101886,onoffshelf,2205452;'
   sendmsgs = jsonobj['Data'].split(';') # temp use, should be splitted by ';'

   #for i,m in enumerate(sendmsgs):
   #   m = 
   # locate the time period for diff ( plus and minus one hour)   
   timemax = int(max(sendmsgs).split(',')[2]) + 600  # plus 10 minutes
   timemin = int(min(sendmsgs).split(',')[2]) - 600  # minus 10 minutes

   # GENERATE MSG LIST 

   recvmsgs = []

   startdt  = time.localtime(timemin)
   enddt    = time.localtime(timemax)

   datedir  = time.strftime('%Y%m%d', startdt)
   itemdir  = '%s/%s' % (EXECPARAMS['data-directory'], datedir)

   recvmsgs = collect_recv_messages(startdt, enddt)

   # COMPARE SEND/RECEIVE LIST

   lostmsgs = []

   print '[==] sendmsgs :', sendmsgs
   print '[==] recvmsgs :', recvmsgs 

   for m in sendmsgs:
      if m not in recvmsgs:
         lostmsgs.append(m) 

   # ISSUE RESEND API CALL IF NEEDS

   if len(lostmsgs) == 0:
      print '[@@] The diff list is completely the same, congratulations!'
      return

   # MESSAGE MISSED, CALL B2E REFETCH API (100 per batch)
   print '[!!] The diff list is different, start refetching call'

   jsfmt = '{"FugoSaleNo":"%s", "MsgType":"%s", "Timestamp":"%s"},'
   diffs = '['

   for i,m in enumerate(lostmsgs):
     # convert lostmsgs from csv to json format
     fields = m.split(',')
     diffs += jsfmt % (fields[0], fields[1], fields[2])  

   diffs = diffs.rstrip(',') + ']'
   diffs = eval(diffs) # convert to dict object

   session  = requests.Session()
   userpwd  = { "UserName":"userforvespa", "Password":"123456", "Platform":"B2E" }

   response = session.post('http://%s/o/api/Jwt/GetJWT' % EXECPARAMS['b2eapi-host'], json=userpwd)

   if response.status_code != 200:
      print '[!!] Asking token from api server failed ! code = %d, reason = %s' % (response.status_code, response.reason)
      session.close()
 
      print '[@@] Processing End.'
      return


   print '[==] api server response: ', response.content

   rejo = json.loads(response.content)
   auth = 'bearer ' + rejo['data']
   url  = 'http://%s/o/api/RMQ/Refetch' % EXECPARAMS['b2eapi-host']

   session.headers.update({'Authorization':auth })

   # To prevent B2E API hangs servmqagent, so we use thread calling  
   # B2E API.
   worker = threading.Thread(target = issue_resend_call, args = (session, url, diffs))

   worker.start()
   time.sleep(1)

   return


def b2e_product_datacompletion(body):
   global msgsendtime, EXECPARAMS

   print '[==] ========================================'
   print '[@@] Processing data completion messages ...|'
   print '[==] ========================================'

   jsonobj = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime : ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body     : ', body[:130], '...'

   print '[@@] Processing End.'
   return


def b2e_product_productinfo(body):
   global msgsendtime, EXECPARAMS

   print '[==] ===================================='
   print '[@@] Processing ProductInfo messages ...|'
   print '[==] ===================================='

   jsno = json.loads(body)
   msgsendtime = jsno['UnixTimestamp']

   print '[==] message sendtime : ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body     : ', body[:60]
   print '[==]     GOOD_NM - ', jsno['GOOD_NM']
   print '[==]     INTER_PROPERTY  - %s .....' % jsno['INTER_PROPERTY'][:100]
   print '[==]     INTER_GIFT_DESC - %s .....' % jsno['INTER_GIFT_DESC'][:100]
   print '[==]     SMS - ', jsno['SMS1'], jsno['SMS2'], jsno['SMS3']

   print '[@@] Processing End.'
   return
    

def b2e_product_others(body):
   global msgsendtime, EXECPARAMS

   print '[==] =================================='
   print '[@@] Processing unhandled messages ...|'
   print '[==] =================================='

   jsonobj = json.loads(body)
   msgsendtime = jsonobj['UnixTimestamp']

   print '[==] message sendtime : ', time.strftime('%y%H%M%S', time.localtime(msgsendtime))
   print '[==] message body     : ', body[:130], '...'

   print '[@@] Processing End.'
   return


def ANNO_callback(ch, method, props, body):
   global msgrecvtime, EXECPARAMS

   print '[@@] Announcement: ', body
   sys.exit(0)
   return

def B2E_callback(chann, method, props, body):
   global msgrecvtime, EXECPARAMS, SHVSLEEPTIME

   routes = [
      [ "B2E.Product.Category",       b2e_product_category ],
      [ "B2E.Product.OnOffShelf",     b2e_product_onoffshelf ],
      [ "B2E.Product.ProdSpecForm",   b2e_product_prodspecform ],
      [ "B2E.Product.HiddenState",    b2e_product_hiddenstate ],
      [ "B2E.Product.ProductInfo",    b2e_product_productinfo ],
      [ "B2E.Product.ProductLog",     b2e_product_productlog ],
      [ "B2E.Product.DataCompletion", b2e_product_datacompletion ]
   ]

   msgrecvtime = time.time()

   for processing in routes:
      if processing[0] in str(method):

         try:
            processing[1](body) 

            if SHVSLEEPTIME.value != 0:
               chann.sleep(SHVSLEEPTIME.value * 60)

         except Exception, err:
            print '[!!] Exception happened as processing events'
            print '[!!] Dump raw event for alert :', body

            if EXECPARAMS['debug'] == True:
               traceback.print_exc()
         finally:
            chann.basic_ack(delivery_tag=method.delivery_tag)

      else:
         continue


   return


## ===============================
## | SUBROUTINE DEFINITIONS      |
## ===============================

def read_execution_params(sysparams):
   global EXECPARAMS

   for spm in sysparams:
      if '--data-directory' in spm:
         EXECPARAMS['data-directory'] = spm.split('=')[1]
      elif '--store-data-only' == spm:
         EXECPARAMS['store-data-only'] = True
      elif '--vespa-host' in spm:
         EXECPARAMS['vespa-host'] = spm.split('=')[1]
      elif '--rmq-host' in spm:
         hosts = spm.split('=')[1].split(',')
         EXECPARAMS['rmq-host'] = hosts
      elif '--self-monitor' in spm:
         EXECPARAMS['self-monitor'] = True
      elif '--env' in spm:
         EXECPARAMS['env'] = spm.split('=')[1]
      elif '--debug' in spm:
         EXECPARAMS['debug'] = True
      else:
         continue

   if EXECPARAMS['env'] == 'LAB':
      EXECPARAMS['vespa-host']  = EXECPARAMS['lab-vespa-host']
      EXECPARAMS['rmq-hosts']   = EXECPARAMS['lab-rmq-hosts']
      EXECPARAMS['b2eapi-host'] = EXECPARAMS['lab-b2eapi-host']
      EXECPARAMS['smtp-host']   = EXECPARAMS['lab-smtp-host']

   return
 

def start_rmq_service():
   global EXECPARAMS

   onrunning = True
   mqservers = EXECPARAMS['rmq-hosts']

   while onrunning:
      try:
         print '[GG] ::::: CONNECTING TO RMQ SERVER ::::: '

         random.shuffle(mqservers)

         userpwd = pika.PlainCredentials('docker', 'swarm')   

         param = pika.ConnectionParameters(host=mqservers[0], port=5672, credentials=userpwd, heartbeat=300)
         conne = pika.BlockingConnection(param)
         chann = conne.channel()

         chann.basic_qos(prefetch_count=50)

         result = chann.queue_declare(exclusive=True)
         qname  = 'Product'

         exchange = 'B2EProduct'
         binding  = 'B2E.Product.#'

         chann.queue_bind(exchange=exchange, queue=qname, routing_key=binding)
         chann.basic_consume(B2E_callback, queue=qname, consumer_tag='falconagent', no_ack=False) # Set no_ack=False to enable prefetch_count

         print '[@@] ::::: START CONSUMING EVENTS ::::: '

         try:
            chann.start_consuming()
         except KeyboardInterrupt:
            print '[!!] Keyboard interrupt happened ! message consuming ends.'
            
            # send_alert_mail()
            
            chann.stop_consuming()
            conne.close()
            print '[@@] the rest of events is processed, '
            break
      except pika.exceptions.ConnectionClosed as error:
         print '[!!] connect is reset by server, consuming the rest of messages ...'
         continue
      except pika.exceptions.AMQPChannelError as error:
         print '[!!] Caught an AMQP channel error: %s, stopping ...' % error
         break
      except pika.exceptions.AMQPConnectionError as error:
         print '[!!]Caught an AMQP connection error: %s, stopping ... ' % error
         continue


def execute_rmq_actions(actcmd):
   ## 1. Initialize account and password
   userpwd = pika.PlainCredentials('docker', 'swarm')   

   # 2. Connect to RabbitMQ server
   param = pika.ConnectionParameters(host=EXECPARAMS['rmq-host'], port=5672, credentials=userpwd, heartbeat=300)
   conne = pika.BlockingConnection(param)
   chanE = conne.channel()
   chanV = conne.channel()  

   ## 3. Create channel for executing mqagent actions

   chanE.exchange_declare(exchange='B2EProduct', exchange_type='topic', durable=True)
   chanV.exchange_declare(exchange='VespaAnnounce', exchange_type='fanout')

   ## 4. Execute agent actions

   if sys.argv[1] == 'publish':
      chanV.basic_publish(exchange='VespaAnnounce', routing_key='', body=sys.argv[2])   

   elif sys.argv[1] == 'listen':
      result = chanV.queue_declare(exclusive=True)
      qname  = 'VespaAnnounceQ'
      
      chanV.queue_bind(exchange='VespaAnnounce', queue=qname)
      chanV.basic_consume(ANNO_callback, queue=qname, no_ack=True)
      chanV.start_consuming()

   elif sys.argv[1] == 'emit':
      routingkey = 'V2E.Product.DataRefetch'
      msg        = sys.argv[2]

      chanE.basic_publish(exchange='B2EProduct', routing_key=routingkey, body=msg)

   elif sys.argv[1] == 'devel':
      print 'this action is not supported yet.'

   else:
      print('Unknown commands: ', sys.argv)

   return


def monitor_mqagent_process(pid):
   while True:
      processes = [ p for p in os.listdir('/proc') if p.isdigit() ]
      found = False

      for lp in processes:
         fp = open('/proc/%s/cmdline' % lp, 'r')
         df = fp.read()
         ld = df.split('\0')

         if lp == str(pid) and 'servmqagent.py' in ld:
            time.sleep(1)
            found = True 
            break

      if found == False:
         print '[!!] mqagent process (%d) is dead ! ' % pid
         break

   return


def send_alert_mail(errstr, comment = ''):
   global EXECPARAMS

   server = smtplib.SMTP()
   errmesgs = {
      'mqagent-process-crashed' : '[CRITICAL] mqagent crashes !! ',
      'mqagent-item-missed'     : '[ALERT] mqagent lost some messages from B2EProduct channel'
   }

   try:
      if errstr in errmesgs.keys():
         errmsg = MIMEText(errmesgs[errstr] + '\n' + comment, 'plain', 'utf-8')

         errmsg['From']    = Header('MqAgent Monitor', 'utf-8')
         errmsg['To']      = Header('FalconAlert@TeamsChannel')
         errmsg['Subject'] = Header('MqAgent Alert Message', 'utf-8')

         server.sendmail( '3edb09d2.eitc.com.tw@apac.teams.ms',
                          ['1136f3ef.eitc.com.tw@apac.teams.ms'],
                          errmsg.as_string())
         server.close()
         print '[==] Send alert mail to Teams successfully.'
      else:
         print '[==] No corresponding error message, alert mail cancelled.'
   except smtplib.SMTPException:
      print '[!!] Sending alert mail failed!'

   return


## =================================
## |     MQ MANAGEMENT CONSOLE     |  
## =================================

SHVSLEEPTIME = multiprocessing.Value('i', 0)

class mqmngtconsole(cmd.Cmd):
   def do_hello(self, line):
      print 'hello !'

   def pause(self, line):
      global SHVSLEEPTIME

      try:
         SHVSLEEPTIME.value = int(line)
      except:
         print '[!!] mq console error!'

      return


   def do_exit(self, line):
      print '[@@] Quit MQ management console.'
      return True


def start_console_process():
   global EXECPARAMS, SHVSLEEPTIME

   mqmngtconsole().cmdloop()
   return

## ========================
## |     MAIN PROGRAM     |  
## ========================


helpmsg = '''
   Usage: python servmqagent.py [Actions][ExeOptions | ActOptions] msg-body   

   Actions:
      publish     Send event(msg-body) to Announcement channel.
      listen      Read event from Announcement channel.
      emit        Send event(msg-body) to B2E.Product.DataRefetch via B2EProduct exchange.
      receive     Read events coming from B2E.#@B2EProduct.

      devel       For internal developing use.
      help        Print out this messge.

   ExeOptions:
      -v, -vv     Print verbose message, -vv for more details.
      -d          Execute self-diagnose.
      -p          Print agent version and default option values.
      --debug     Execute on debug mode, easy for debugging.

   ActOptions:
      receive options:

      --data-directory    directory for storing sink data.
      --vespa-host        specify where the vespaconfig is.
      --rmq-host          specify where the RabbitMQ server is.
      --store-data-only   store the sinked data, no feeding.
      --self-monitor      enable self-monitoring function.
      --interactive       enter interactive console for more operations.

'''



## 1. PARSE EXECUTION ARGUMENTS ##

read_execution_params(sys.argv)

## 2. PRINT HELP MESSAGE IF NEEDS ##

if len(sys.argv) == 1 or sys.argv[1] == 'help':
   print(helpmsg)
   sys.exit(0)


## 3. FORK CHILD PROCESS FOR MQAGENT EXECUTION

if EXECPARAMS['debug'] == True:
   print '[@@] ::::: RUN ON DEBUG MODE ! ::::: '

   if sys.argv[1] == 'receive':
      start_rmq_service()
   else:
      execute_rmq_actions(sys.argv[1])
else:
   times = 1

   while times <= 3:
      print '[@@] Agent process fork times = ', times

      pid = os.fork()

      if pid == 0: # child mqagent process
         print '[==] This is child mqagent process, envargs = ', sys.argv
         print '[==] parent pid and child pid is ', (os.getppid(), os.getpid())

         if sys.argv[1] == 'receive':
            start_rmq_service()
            print '[!!] servmqagent process ends.'
            sys.exit(-1)
         else:
            execute_rmq_actions(sys.argv[1])
            sys.exit(0)
      else: # mqagent parent process
         time.sleep(3)

         if EXECPARAMS['interactive'] == True:
            console = multiprocessing.Process(target = start_console_process)

            console.start()

         if EXECPARAMS['self-monitor'] == True:
            monitor_mqagent_process(pid)
            times += 1
            continue
         else:
            break

print '[@@] ::::: PARENT PROCESS ENDS. :::::'
sys.exit(0)

