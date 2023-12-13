import sys
test_files = [
    './2023/day5/part2/inputs_simple.txt',
    './2023/day5/part2/inputs_full.txt'
]

# TODO: We need to do range mapping here instead of brute force checks
#


def get_transformed_ranges(mapping, source_range):
    # print(source_range)
    # print(mapping)
    (src_start, src_length) = source_range
    for i in range(len(mapping)):
        (dest, source, length) = mapping[i]
        if source <= src_start and source + length >= src_start + src_length:
            # fully embedded return mapping
            return [(dest + src_start-source, src_length)]
        if source >= src_start + src_length or src_start >= source + length:
            # no overlap, possible, skip mapping
            continue

        if source > src_start:
            # start is behind source so we split into [start, source] and process([source+1, start + src_length])
            return get_transformed_ranges(mapping, (src_start, source - src_start - 1)) + get_transformed_ranges(mapping, (source, src_length - (source - src_start)))

        if source + length < src_start + src_length:
            return get_transformed_ranges(mapping, (src_start, source + length - src_start)) + get_transformed_ranges(mapping, (source + length + 1, src_length - (source + length - src_start)))

    return [source_range]


def get_transformed_ranges_all(mapping, source_ranges):
    ranges = []
    for r in source_ranges:
        ranges.extend(get_transformed_ranges(mapping, r))

    return ranges


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
    seeds_ranges = []

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
                    seeds_ranges.append((start, length))
                    # for j in range(length):
                    #     seeds.append(start+j)
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

        soil = get_transformed_ranges_all(seed_to_soil, seeds_ranges)
        fert = get_transformed_ranges_all(soil_to_fertilizer, soil)
        water = get_transformed_ranges_all(fertilizer_to_water, fert)
        light = get_transformed_ranges_all(water_to_light, water)
        temp = get_transformed_ranges_all(light_to_temperature, light)
        humd = get_transformed_ranges_all(temperature_to_humidity, temp)
        locs = get_transformed_ranges_all(humidity_to_location, humd)

        min_loc = locs[0][0]
        for loc in locs:
            min_loc = min(loc[0], min_loc)
        print(min_loc)
