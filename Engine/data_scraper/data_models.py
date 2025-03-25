""" Define the models of the scrapped data """
from pydantic import BaseModel
from typing import Union

class Specification(BaseModel):
    screen_size: float
    front_camera: float
    back_camera: float
    display_type: str
    network_connectivity: str
    battery_capacity: int
    sim_card_size: str
    storage_rom: int
    memory_ram: int
    operating_system: str

class MobilePhoneSpecification(Specification):
    processor_brand: str
    processor_model: str  
    processor_speed: float
    carrier: str

class ComputerSpecification(Specification):
    cpu_processor_brand: str
    cpu_processor_model: str  
    cpu_processor_speed: float
    graphics_processor_brand: str
    graphics_processor_model: str
    graphics_processor_speed: float

class ProductItem(BaseModel):
    name: str
    brand: str
    image_url: str
    rating: float
    no_of_reviews: int
    current_price: int
    original_price: int
    discount: int
    condition: str
    specification: Union[MobilePhoneSpecification, ComputerSpecification]
    description: str
    features: str