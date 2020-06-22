import constants

RESULT_WIN_FOR = "FORWINS"
RESULT_WIN_AG = "AGWINS"

PARTISTATUS_WAITING = "WAITING"
PARTISTATUS_ACCEPTED = "ACCEPTED"
PARTISTATUS_REJECTED = "REJECTED"
PARTISTATUS_NORESPONSE = "NORESPONSE"

class debate:



    # @staticmethod
    # def from_dict(source):
    #     # ...

    @staticmethod
    def from_dict(source):
        # ...
        a=10

    def to_dict(self):
        retconv = {
            u'uid':self.uid,
            u'inviteruid' : self.inviteruid,
            'topic' : self.topic,
            u'actualstartts' : self.actualstartts,
            u'actualendts' : self.actualendts,
            u'scheduledstartts' : self.scheduledstartts,

            u'flagactivestate' :  self.flagactivestate,

            u'debater_for_uid' :  self.debater_for_uid,
            u'debater_ag_uid' :  self.debater_ag_uid,
            u'moderatoruid' :  self.moderatoruid,

            u'debater_for_sid' :  self.debater_for_sid,
            u'debater_ag_sid' :  self.debater_ag_sid,
            u'moderatorsid' :  self.moderatorsid,

            u'debater_for_name' :  self.debater_for_name,
            u'debater_ag_name' :  self.debater_ag_name,
            u'moderator_name' :  self.moderator_name,

            u'debater_for_pic' :  self.debater_for_pic,
            u'debater_ag_pic' :  self.debater_ag_pic,
            u'moderator_pic' :  self.moderator_pic,
            u'participants' : self.participants,

            #////////////STATUS//////////////////////////


            u'debater_for_status' : self.debater_for_status,
            u'debater_ag_status' : self.debater_ag_status,
            u'moderatorstatus' : self.moderatorstatus,

            #////////////STATISTICS//////////////////////////
            u'debstatcurrentviewership' : self.debstatcurrentviewership,
            u'debstatpeakviewership' : self.debstatpeakviewership,

            u'debstattotalargs' : self.debstattotalargs,
            u'debstattotalpoints' : self.debstattotalpoints,
            u'debstattot_fallacies' : self.debstattot_fallacies,
            u'debstattot_clinchers' : self.debstattot_clinchers,
            u'debstattot_iagree' : self.debstattot_iagree,
            u'overallresult' : self.overallresult,
            u'deballtags': self.deballtags,


            #////////////RUNTIME//////////////////////////
            u'turn' : self.turn,

            u'activekeyargguid' : self.activekeyargguid,
            u'activekeyargindex' : self.activekeyargindex
        }
        return retconv

    def __iter__(self):
        return vars(self).items()


    def __init__(self,uid,topic,ts):

        self.uid = uid;
        self.inviteruid = None;
        self.topic = topic;
        self.actualstartts = None;
        self.actualendts =None;
        self.scheduledstartts =None;

        self.flagactivestate = constants.DEBACTIVSTATE_WAITINGJOIN;

        self.debater_for_uid = None;
        self.debater_ag_uid = None;
        self.moderatoruid = None;

        self.debater_for_sid = None;
        self.debater_ag_sid = None;
        self.moderatorsid = None;

        self.debater_for_name = None;
        self.debater_ag_name = None;
        self.moderator_name = None;

        self.debater_for_pic = None;
        self.debater_ag_pic = None;
        self.moderator_pic = None;
        self.participants = [];

        #////////////STATUS//////////////////////////


        self.debater_for_status = PARTISTATUS_WAITING;
        self.debater_ag_status = PARTISTATUS_WAITING;
        self.moderatorstatus = PARTISTATUS_WAITING;

        #////////////STATISTICS//////////////////////////
        self.debstatcurrentviewership =0;
        self.debstatpeakviewership =0;

        self.debstattotalargs =0;
        self.debstattotalpoints =0;
        self.debstattot_fallacies =0;
        self.debstattot_clinchers =0;
        self.debstattot_iagree =0;
        self.overallresult = "";
        self.deballtags = None;


        #////////////RUNTIME//////////////////////////
        self.turn = constants.TURN_FOR;

        self.activekeyargguid=None;
        self.activekeyargindex = 0;
