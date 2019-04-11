def distance_to_metres(distance,use_metric):
    if use_metric:
        return round(distance*1000,0)
    else:
        return round(distance*1609.344,0)