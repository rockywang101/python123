'''
Created on 2019年4月24日
@author: rocky
'''
import logging.handlers
import traceback
 
class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.
 
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                            self.fromaddr,
                            ','.join(self.toaddrs),
                            self.getSubject(record),
                            formatdate(), msg)
            
            smtp = smtplib.SMTP(self.mailhost, self.mailport)            
            smtp.ehlo() # for tls add this line
            smtp.starttls() # for tls add this line
            smtp.ehlo() # for tls add this line
            smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()
            self.handleError(record)