import math

def compute_volume(r, h):
    return math.pi*(r**2)*h 

def compute_surface_area(r, h):
    return (2*math.pi)*r*(r+h)

def compute_storage_efficiency(v,sa):
    return v/sa

def main():
    volume = compute_volume(14,15)
    surface_area = compute_surface_area(14,15)
    storage_efficiency = compute_storage_efficiency(volume,surface_area)
    print(volume)
    print(surface_area)
    print(storage_efficiency)

main()