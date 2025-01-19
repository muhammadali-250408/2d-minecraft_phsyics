
def make_tile_map(file):
    f = open(file, "r")
    raw_data = f.read()
    tile_map_arr = raw_data.split("\n")
    print(tile_map_arr)
    print(len(tile_map_arr[1]))
    for i in range (len(tile_map_arr)):
        tile_map_arr[i] = tile_map_arr[i].split(" ")

    print(tile_map_arr)
    return tile_map_arr


