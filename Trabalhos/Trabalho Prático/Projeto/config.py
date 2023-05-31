class config():
    
    # General
    host                = "192.168.56.1"
    password            = "Openfire_password1"

    airplane_types      = ["Comercial", "Merchandise"]
    cities              = ["Lisbon", "Oporto", "Madrid", "Barcelona", "London", "Manchester", "Paris", "Amestardan", "Rome", "Milan"]
    companies           = ["RyanAir", "EasyJet", "Wizz Air", "Eurowings", "Norwegian Air Shuttle", "Vueling Airlines", "TAP Air Portugal", "Air Europa", "Icelandair"]
    
    # Tower
    num_runways         = 4                   # Number of runways in the airport
    max_land_queue_size = 10                  # Max number of planes that can be in the landing queue
    
    # GareManager
    num_gares           = 10                  # Number of gares in the airport
    
    # Airplanes
    arrival_interval    = 8                   # Interval between new planes being created
    landing_time        = 7                  # How long for a plane to land
    drive_time          = 5                   # How long for a plane to drive to the gare
    parked_time         = 12                  # How long the plane stays in the airport
    max_land_wait_time  = 20                  # How long the plane is willing to wait in the landing queue

    # Admin
    update_time         = 1.0                 # Seconds between admin (UI) updates
    weather_state       = 0                   # Initial weather state -1 -> Off; 0 -> sun; 1 -> rain; 2 -> fog; 3 -> storm