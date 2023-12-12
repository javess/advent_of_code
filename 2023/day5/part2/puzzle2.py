import sys
test_files = [
    './2023/day5/part2/inputs_simple.txt',
    './2023/day5/part2/inputs_full.txt'
]


def get_mapping(mapping, value):
    for i in range(len(mapping)):
        (dest, source, length) = mapping[i]
        if (value >= source and value < source + length):
            return dest + (value - source)
    return value


for test_file in test_files:
    print(test_file)
    total = 0
    seeds = []

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    active_map = None

    with open(test_file) as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            if line.startswith('seeds:'):
                seed_defs = [int(x)
                             for x in line.split(':')[1].strip().split(' ')]
                for i in range(len(seed_defs)//2):
                    print(f"{i}/{len(seed_defs)//2}")
                    start = seed_defs[2*i]
                    length = seed_defs[2*i + 1]
                    for j in range(length):
                        seeds.append(start+j)
                continue

            if line[0].isalpha():
                key = line.strip().split(' ')[0]
                if key == 'seed-to-soil':
                    active_map = seed_to_soil
                elif key == 'soil-to-fertilizer':
                    active_map = soil_to_fertilizer
                elif key == 'fertilizer-to-water':
                    active_map = fertilizer_to_water
                elif key == 'water-to-light':
                    active_map = water_to_light
                elif key == 'light-to-temperature':
                    active_map = light_to_temperature
                elif key == 'temperature-to-humidity':
                    active_map = temperature_to_humidity
                elif key == 'humidity-to-location':
                    active_map = humidity_to_location
                continue

            if line[0].isdigit() and active_map is not None:
                # dest source len
                nums = [int(x) for x in line.split(' ')]
                active_map.append((nums[0], nums[1], nums[2]))

        min_loc = 100000000000

        for s in seeds:
            soil = get_mapping(seed_to_soil, s)
            fert = get_mapping(soil_to_fertilizer, soil)
            water = get_mapping(fertilizer_to_water, fert)
            light = get_mapping(water_to_light, water)
            temp = get_mapping(light_to_temperature, light)
            humd = get_mapping(temperature_to_humidity, temp)
            loc = get_mapping(humidity_to_location, humd)
            min_loc = min(loc, min_loc)
            print(f"seed: {s} loc: {loc}")
    print(min_loc)
