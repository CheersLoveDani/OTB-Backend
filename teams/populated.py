from teams.serializers import TeamSerializer
from jwt_auth.populated import PopulatedUserSerializer

class PopulatedTeamSerializer(TeamSerializer):

    dps_1 = PopulatedUserSerializer()
    dps_2 = PopulatedUserSerializer()

    tank_1 = PopulatedUserSerializer()
    tank_2 = PopulatedUserSerializer()

    support_1 = PopulatedUserSerializer()
    support_2 = PopulatedUserSerializer()
