"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging
import time

def main():
    """
        This is the entry point in the program

        The default function is getting the puzzle, trying to out
    """
    logging.basicConfig(level=logging.INFO)

    options = parse_args()

    input_file = options.input


    try:
        t1_start = time.process_time()
        output_one = part_one(input_file)
        t1_stop = time.process_time()
        logging.info(f"Part 1 solution is : {min(output_one)}, processed in {t1_stop - t1_start} s")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
        t1_start = time.process_time()
        output_two = part_two(input_file)
        t1_stop = time.process_time()
        logging.info(f"Part 2 solution is : {min(output_two)[0]}, processed in {t1_stop - t1_start} s")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")


def part_one(input_file):
    """
        This is a pre_coded line parser in case it is needed
    """
    with open(input_file) as file:
        # Line 1 are the seeds

        seeds = list()

        first_line = file.readline()
        seeds = [int(seed) for seed in first_line[:-1].split(" ")[1:]]

        seed_to_soil = dict()
        # Then is seed to soil map
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [soil, seed, number] = line[:-1].split(" ")
            seed_to_soil[(int(seed),int(seed) + int(number)-1)] = int(soil) # type:ignore
            line = file.readline()

        soil_to_fertilizer = dict()
        # Then is soil_to_fertilizer map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [fertilizer, soil, number] = line[:-1].split(" ")
            soil_to_fertilizer[(int(soil),int(soil) + int(number)-1)] = int(fertilizer) # type:ignore
            line = file.readline()

        fertilizer_to_water = dict()
        # Then is fertilizer to water map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [water, fertilizer, number] = line[:-1].split(" ")
            fertilizer_to_water[(int(fertilizer),int(fertilizer) + int(number)-1)] = int(water) # type:ignore
            line = file.readline()

        water_to_light = dict()
        # Then is water to light map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [light, water, number] = line[:-1].split(" ")
            water_to_light[(int(water),int(water) + int(number)-1)] = int(light) # type:ignore
            line = file.readline()

        light_to_temperature = dict()
        # Then is light to temperature map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [temperature, light, number] = line[:-1].split(" ")
            light_to_temperature[(int(light),int(light) + int(number)-1)] = int(temperature) # type:ignore
            line = file.readline()

        temperature_to_humidity = dict()
        # Then is temperature to humidity map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [humidity, temperature, number] = line[:-1].split(" ")
            temperature_to_humidity[(int(temperature),int(temperature) + int(number)-1)] = int(humidity) # type:ignore
            line = file.readline()

        humidity_to_location = dict()
        # Then is humidity to location map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [location, humidity, number] = line[:-1].split(" ")
            humidity_to_location[ (int(humidity),int(humidity) + int(number)-1)] = int(location) # type:ignore
            line = file.readline()

        output = []
        #output.append(humidity_to_location[temperature_to_humidity[light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]])
        for dictionary in seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location:
            output = []
            for seed in seeds:
                no_match = True
                for (minimum,maximum) in dictionary.keys():
                    if seed >= minimum and seed <= maximum:
                        output.append(dictionary[(minimum,maximum)] + seed - minimum)
                        no_match = False
                if no_match:
                    output.append(seed)
            seeds = output

        return output



def part_two(input_file: str):
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    with open(input_file) as file:
        # Line 1 are the seeds, in pairs of seed and range

        first_line = file.readline()
        seed = None
        seeds = list()
        for data in first_line[:-1].split(" ")[1:]:
            if seed is None:
                seed = data
            else:
                seeds.append((int(seed), int(seed)+int(data)))
                seed = None

        seed_to_soil = dict()
        # Then is seed to soil map
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [soil, seed, number] = line[:-1].split(" ")
            seed_to_soil[(int(seed),int(seed) + int(number))] = int(soil) # type:ignore
            line = file.readline()

        soil_to_fertilizer = dict()
        # Then is soil_to_fertilizer map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [fertilizer, soil, number] = line[:-1].split(" ")
            soil_to_fertilizer[(int(soil),int(soil) + int(number))] = int(fertilizer) # type:ignore
            line = file.readline()

        fertilizer_to_water = dict()
        # Then is fertilizer to water map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [water, fertilizer, number] = line[:-1].split(" ")
            fertilizer_to_water[(int(fertilizer),int(fertilizer) + int(number))] = int(water) # type:ignore
            line = file.readline()

        water_to_light = dict()
        # Then is water to light map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [light, water, number] = line[:-1].split(" ")
            water_to_light[(int(water),int(water) + int(number))] = int(light) # type:ignore
            line = file.readline()

        light_to_temperature = dict()
        # Then is light to temperature map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [temperature, light, number] = line[:-1].split(" ")
            light_to_temperature[(int(light),int(light) + int(number))] = int(temperature) # type:ignore
            line = file.readline()

        temperature_to_humidity = dict()
        # Then is temperature to humidity map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [humidity, temperature, number] = line[:-1].split(" ")
            temperature_to_humidity[(int(temperature),int(temperature) + int(number))] = int(humidity) # type:ignore
            line = file.readline()

        humidity_to_location = dict()
        # Then is humidity to location map
        line = file.readline()
        line = file.readline()
        while line[:-1] != "":
            [location, humidity, number] = line[:-1].split(" ")
            humidity_to_location[ (int(humidity),int(humidity) + int(number))] = int(location) # type:ignore
            line = file.readline()

        output = list()
        #output.append(humidity_to_location[temperature_to_humidity[light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]])
        for dictionary in seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location:
            output = list()
            while seeds:
                start, end = seeds.pop()
                no_match = True
                for (minimum,maximum) in dictionary.keys():
                    # print(start, end)
                    # print(minimum,maximum)
                    if start >= minimum and start < maximum:
                        # print(f"{start} between {minimum} and {maximum}")
                        if end > minimum and end <= maximum:
                            #print(f"{end} between {minimum} and {maximum}")
                            output.append((dictionary[(minimum,maximum)] + start - minimum, dictionary[(minimum,maximum)] + end - minimum))
                            #print(f"output is {(dictionary[(minimum,maximum)] + start - minimum, dictionary[(minimum,maximum)] + end - minimum)}")
                            no_match = False
                            break
                        else:
                            #print(f"{end} not between {minimum} and {maximum}")
                            output.append((dictionary[(minimum,maximum)] + start - minimum, dictionary[(minimum,maximum)] + maximum - minimum))
                            #print(f"output is {(dictionary[(minimum,maximum)] + start - minimum, dictionary[(minimum,maximum)] + maximum - minimum)}")
                            #print(f"appending back is {maximum, end}")
                            seeds.append((maximum, end))
                            no_match = False
                            break
                    elif end > minimum and end <= maximum:
                        #print(f"{start} not between {minimum} and {maximum}")
                        #print(f"{end} between {minimum} and {maximum}")
                        output.append((dictionary[(minimum,maximum)], dictionary[(minimum,maximum)] + end - minimum))
                        #print(f"output is {(dictionary[(minimum,maximum)], dictionary[(minimum,maximum)] + end - minimum)}")
                        #print(f"appending back is {start, minimum}")
                        seeds.append((start,minimum))
                        no_match = False
                        break
                if no_match:
                    output.append((start, end))
            seeds = output

        return output



def parse_args():
    """
        This is an argument parser in case another input is necessary

        In the skeleton, by default, the parsed file is the input file in the day's folder
    """

    import datetime

    default_value=f"Input/day_{datetime.datetime.today().strftime('%d')}/input"
    parser = argparse.ArgumentParser(description='Process Day 5 input')
    parser.add_argument('input',
                        help='',
                        default="Input/day_05/input",
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()