from examples.district_model_4_markets import main as model_4_markets
from examples.power_plants_model import main as model_power_plants

if __name__ == '__main__':
    
    model_4_markets(year=2019, days=30)
    model_power_plants(year=2019, days=30)
    
    pass