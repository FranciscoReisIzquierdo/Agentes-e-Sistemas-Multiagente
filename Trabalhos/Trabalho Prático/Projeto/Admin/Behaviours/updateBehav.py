from spade.behaviour import PeriodicBehaviour
from spade.message import Message
from messages import ReportInfo, GaresInfo
from config import config
from prettytable import PrettyTable
import os

class UpdateBehav(PeriodicBehaviour):

    async def run(self):

        # Request planes info to tower
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "request_report")
        await self.send(msg)

        msg = await self.receive(timeout=1000)
        (planes, aborts) = ReportInfo(msg.body)

        # Request gares info to GareManager
        msg = Message(to=f"gare_manager@{config.host}")
        msg.set_metadata("performative", "request_report")
        await self.send(msg)

        msg = await self.receive(timeout=1000)
        gares = GaresInfo(msg.body)

        # Create gares table
        gare_table = PrettyTable()
        gare_table.field_names = ["ID", "Type", "Free"]

        for gare in gares:
            gare_table.add_row(
                [gare.id, gare.type, gare.free]
            )

        # Create planes table
        plane_table = PrettyTable()
        plane_table.field_names = ["ID", "Origin", "Destination", "Company", "Type", "State", "Gare", "Runway"]

        for key in planes:
            plane = planes[key]
            plane_table.add_row(
                [plane.id, plane.origin, plane.destination, plane.company, plane.type, plane.state,
                 plane.gare.id if plane.gare else None, plane.runway.id if plane.runway else None]
            )
        
        # Create aborts table
        abort_table = PrettyTable()
        abort_table.field_names = ["ID", "Origin", "Destination", "Company", "Type", "State"]
        
        for plane in aborts:
            abort_table.add_row(
                [plane.id, plane.origin, plane.destination, plane.company, plane.type, "aborted"]
            )

        # Clear console and show tables
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gares")
        print(gare_table)
        print("Weather state:", ["Sun", "Rain", "Fog", "Storm"][config.weather_state])
        print("Planes")
        print(plane_table)
        if len(abort_table.rows) > 0:
            print("Aborts")
            print(abort_table)
