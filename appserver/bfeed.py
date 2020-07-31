import constants


STYPE_MANTHANUSER = "STYPE_MANTHANUSER"
STYPE_MANTHANAUTOGEN = "STYPE_MANTHANAUTOGEN"

SORG_MANTHAN = "SORG_MANTHAN"

class bfeed:
    @staticmethod
    def from_dict(source):
        # ...
        a=10

    def to_dict(self):
        retconv = {
         u'uid' = self.uid
         u'topic' = self.topic


         u'sourcetype' = self.sourcetype
         u'sourceuseruid' = self.sourceuseruid
         u'sourceusersid' = self.sourceusersid


         u'sourceorg' = self.sourceorg
         u'sourceorgname' = self.sourceorgname
         u'sourceorgpic' = self.sourceorgpic
         u'sourceurl' = self.sourceurl

         u'relcountry' = self.relcountry
         u'reldomain' = self.reldomain
         u'reltags' = self.reltags
         u'convos' = self.convos
         u'defenduids' = self.defenduids
         u'calloutuids' = self.calloutuids

         Date ts = self.ts
        }
        return retconv

    def __iter__(self):
        return vars(self).items()


    def __init__(self,uid,topic,sourcename):
        self.uid = uid
        self.topic = topic

        self.sourcetype = STYPE_MANTHANAUTOGEN
        self.sourceuseruid = "ArR1BJ8zHsM0sL6DmfnHvtHD10R2"
        self.sourceusersid = "@letusmanthan"

        self.sourceorg = "Twitter"
        self.sourceorgname = "Twitter"
        self.sourceorgpic = "https://app.manthanapp.com/static/Twitter_Logo_Blue.png"
        self.sourceurl = "https://www.twitter.com"

        self.relcountry = []
        self.reldomain = []
        self.reltags = []
        self.convos = []
        self.defenduids = []
        self.calloutuids = []

        self.ts = datetime.datetime.now();
