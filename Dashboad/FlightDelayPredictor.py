import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from FlightDelayPredictorConfig import *

class FlightDelayPredictor:

    def __init__(self):
        self.engine = create_engine(databaseURL)
        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        self.dash_v_orig_states = Base.classes.airports
        self.dash_v_dest_states = Base.classes.dash_v_dest_states

    def get_origin_states(self):

        session = Session(self.engine)

        origin_states_list = session.query(func.distinct(self.airports.state)).order_by(self.airports.state).all()

        session.close()

        return origin_states_list

    def get_origin_state_airports(self, origin_state_code):

        session = Session(self.engine)

        origin_state_airports_list = session.query(self.airports.city, self.airports.code).\
            filter(self.airports.state == origin_state_code).\
            order_by(self.airports.city).all()
        
        session.close()

        return origin_state_airports_list

    def get_dest_states(self, origin_airport_code):

        session = Session(self.engine)

        dest_states_code_list = session.query(self.dash_v_dest_states.dest_state_option_name, ).\
            filter(self.dash_v_dest_states.origin_airport_code == origin_airport_code)
        
        session.close()
   
        return dest_states_code_list

    def get_dest_state_airports(self, date, origin_state_code, dest_state_code):

        dest_state_airports_list = []
        
        return dest_state_airports_list

    def get_dest_flight_info(self, date, origin_airport, dest_airport_code):

        dest_flight_info = []

        return dest_flight_info
